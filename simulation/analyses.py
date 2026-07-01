"""The Agentoscope — detecting agency by intervention, not observation.

The instrument compares two models of a system's trajectory: a PASSIVE model,
an autonomous linear dynamics x_{t+1} = A x_t + b (a point attractor, a settling
process), and an AGENT model, x_{t+1} = x_t + k (g_t - x_t), whose dynamics are
coupled to an external goal channel g_t that the experimenter controls. The
agency score is the log-likelihood ratio

    A(S) = log P(data | agent model) - log P(data | passive model).

One structural fact organizes everything. When the goal is held constant, the
agent model's dynamics are linear in x and therefore lie INSIDE the passive
model's family, so the passive model fits at least as well and A <= 0 no matter
how agentic the system is. Agency is invisible to observation. It becomes
visible only when the goal channel is intervened upon: if the system tracks the
moved goal, only the agent model (which sees g_t) can predict it, and A jumps
positive; if the system ignores the goal, the agent model's use of g_t only
hurts, and A stays at or below zero. Agency lives on Pearl's interventional
rung of the ladder, not the observational one.

Four studies:
  1. observation_confounded   watching cannot separate agents from passive
                              systems (area under the ROC ~ chance)
  2. intervention_reveals     goal interventions separate them completely;
                              informative (goal-shift) vs uninformative
                              (mere displacement) perturbations
  3. richness_false_friend    dynamical complexity is uncorrelated with agency;
                              a chaotic "hurricane" scores ~0 despite high
                              complexity, a chemotactic cell scores high
  4. agency_ladder            the ordered verdict on a battery of systems, and
                              equifinality-under-obstruction as the criterion
                              that even a set-point regulator fails

Run `uv run run_all.py`. Seeded (SEED) so every number is reproducible.
"""
from __future__ import annotations

import numpy as np

SEED = 20260701
K_TRUE = 0.3          # controller gain of the agent systems
NOISE = 0.05          # process noise
T_OBS = 120           # steps of passive observation
DIM = 2


# --------------------------------------------------------------------------- #
# Systems (true generative processes). Each returns a trajectory x[T, 2]       #
# given a goal schedule g[T, 2]; passive systems ignore g.                     #
# --------------------------------------------------------------------------- #
def _sim_agent(g, rng, k=K_TRUE, noise=NOISE):
    T = len(g)
    x = np.zeros((T, DIM)); x[0] = g[0] + rng.normal(0, 0.3, DIM)
    for t in range(T - 1):
        x[t + 1] = x[t] + k * (g[t] - x[t]) + rng.normal(0, noise, DIM)
    return x


def _sim_bowl(g, rng, center=None, k=K_TRUE, noise=NOISE):
    T = len(g); c = g[0] if center is None else center
    x = np.zeros((T, DIM)); x[0] = c + rng.normal(0, 0.3, DIM)
    for t in range(T - 1):                     # settles to a fixed center, ignores g
        x[t + 1] = x[t] + k * (c - x[t]) + rng.normal(0, noise, DIM)
    return x


def _sim_diffusion(g, rng, noise=0.25):
    T = len(g)
    x = np.zeros((T, DIM)); x[0] = g[0]
    for t in range(T - 1):
        x[t + 1] = x[t] + rng.normal(0, noise, DIM)   # random walk, ignores g
    return x


def _sim_chaotic(g, rng):
    """A Henon map embedded in the plane: deterministic chaos, rich structure,
    no set-point, ignores g."""
    T = len(g); a, b = 1.4, 0.3
    x = np.zeros((T, DIM)); p, q = 0.1, 0.1
    for t in range(T):
        x[t] = [p, q]
        p, q = 1 - a * p * p + q, b * p
    # rescale to a comparable spatial extent
    x = (x - x.mean(0)) / (x.std(0) + 1e-9)
    return x


def _sim_regenerator(g, rng, k=K_TRUE, noise=NOISE, barrier=None):
    """A goal-tracker that also routes around a barrier (equifinality): a
    potential field, attracted to g_t and repelled by the barrier."""
    T = len(g)
    x = np.zeros((T, DIM)); x[0] = g[0] + rng.normal(0, 0.3, DIM)
    for t in range(T - 1):
        pull = k * (g[t] - x[t])
        push = np.zeros(DIM)
        if barrier is not None:
            bx, half, strength = barrier          # vertical wall at bx, +/-half in y
            dx = x[t, 0] - bx
            if abs(dx) < 0.6 and abs(x[t, 1]) < half:
                push[0] += strength * np.sign(dx if dx != 0 else 1.0)
                push[1] += strength * np.sign(x[t, 1] if x[t, 1] != 0 else 1.0)
        x[t + 1] = x[t] + pull + push + rng.normal(0, noise, DIM)
    return x


# --------------------------------------------------------------------------- #
# The two models and the agency score                                          #
# --------------------------------------------------------------------------- #
def _ll_passive(x):
    """Best autonomous linear dynamics x_{t+1} = A x_t + b; summed one-step
    Gaussian log-likelihood at the OLS fit. This family CONTAINS the agent
    model's constant-goal dynamics, so it fits observation at least as well."""
    X0, X1 = x[:-1], x[1:]
    Phi = np.hstack([X0, np.ones((len(X0), 1))])          # [x_t, 1]
    W, *_ = np.linalg.lstsq(Phi, X1, rcond=None)          # (3, 2)
    resid = X1 - Phi @ W
    var = max((resid ** 2).mean(), 1e-9)
    n = resid.size
    return -0.5 * n * np.log(2 * np.pi * var) - 0.5 * (resid ** 2).sum() / var


def _ll_agent(x, g):
    """Goal-coupled model x_{t+1} = x_t + k (g_t - x_t); the ONLY extra
    information over the passive model is access to the goal channel g."""
    dx = x[1:] - x[:-1]
    u = g[:-1] - x[:-1]
    denom = (u * u).sum()
    k = (dx * u).sum() / denom if denom > 1e-12 else 0.0
    resid = dx - k * u
    var = max((resid ** 2).mean(), 1e-9)
    n = resid.size
    return -0.5 * n * np.log(2 * np.pi * var) - 0.5 * (resid ** 2).sum() / var


def agency_score(x, g):
    return _ll_agent(x, g) - _ll_passive(x)


def _auc(pos, neg):
    """Probability a random positive outranks a random negative (Mann-Whitney)."""
    pos, neg = np.asarray(pos), np.asarray(neg)
    wins = sum((pos[:, None] > neg[None, :]).sum() for _ in [0]) / (len(pos) * len(neg))
    ties = (pos[:, None] == neg[None, :]).mean()
    return float(wins + 0.5 * ties)


# --------------------------------------------------------------------------- #
# Goal schedules                                                               #
# --------------------------------------------------------------------------- #
def _const_goal(T, rng):
    c = rng.normal(0, 1, DIM)
    return np.tile(c, (T, 1))


def _intervened_goal(T, rng, n_jumps, seg=40):
    """Constant for T_OBS, then a sequence of goal jumps (do-interventions)."""
    g = np.zeros((T, DIM))
    c = rng.normal(0, 1, DIM); g[:T_OBS] = c
    t = T_OBS
    while t < T:
        c = rng.normal(0, 1.4, DIM)
        g[t:t + seg] = c
        t += seg
    return g


# --------------------------------------------------------------------------- #
# Study 1 & 2                                                                   #
# --------------------------------------------------------------------------- #
def observation_confounded(rng) -> dict:
    """Under observation only (constant goal), the agency score cannot separate
    agents from passive systems."""
    N = 300
    a_agent, a_passive = [], []
    for _ in range(N):
        g = _const_goal(T_OBS, rng)
        a_agent.append(agency_score(_sim_agent(g, rng), g))
        a_passive.append(agency_score(_sim_bowl(g, rng), g))
    a_agent, a_passive = np.array(a_agent), np.array(a_passive)
    return dict(
        N=N, auc=_auc(a_agent, a_passive),
        agent_mean=float(a_agent.mean()), passive_mean=float(a_passive.mean()),
        agent_max=float(a_agent.max()),         # <= 0 by construction (up to fit noise)
        frac_agent_positive=float((a_agent > 1.0).mean()),
        r_auc=round(_auc(a_agent, a_passive), 2),
        r_agent_mean=round(float(a_agent.mean()), 1),
        r_agent_max=round(float(a_agent.max()), 2),
        r_agent_max_abs=round(abs(float(a_agent.max())), 2),
    )


def intervention_reveals(rng) -> dict:
    """Goal interventions separate agents from passive systems; the score grows
    per informative (goal-shift) intervention and not per uninformative one."""
    N = 300
    T = T_OBS + 6 * 40
    a_agent, a_passive = [], []
    for _ in range(N):
        g = _intervened_goal(T, rng, n_jumps=6)
        a_agent.append(agency_score(_sim_agent(g, rng), g))
        a_passive.append(agency_score(_sim_bowl(g, rng), g))
    a_agent, a_passive = np.array(a_agent), np.array(a_passive)

    # score vs number of informative interventions
    curve = []
    for nj in range(0, 7):
        T_n = T_OBS + nj * 40
        vv = []
        for _ in range(80):
            g = _intervened_goal(T_n, rng, nj)
            vv.append(agency_score(_sim_agent(g, rng), g))
        curve.append(float(np.mean(vv)))
    per_intervention = (curve[-1] - curve[0]) / 6.0

    # uninformative perturbation: displace the state but hold the goal constant
    unifo = []
    for _ in range(120):
        g = _const_goal(T_OBS + 120, rng)
        x = _sim_agent(g, rng)
        x[T_OBS] += rng.normal(0, 1.5, DIM)          # a shove; agent just returns
        for t in range(T_OBS, len(g) - 1):
            x[t + 1] = x[t] + K_TRUE * (g[t] - x[t]) + rng.normal(0, NOISE, DIM)
        unifo.append(agency_score(x, g))

    return dict(
        N=N, auc=_auc(a_agent, a_passive),
        agent_mean=float(a_agent.mean()), passive_mean=float(a_passive.mean()),
        per_intervention=per_intervention,
        curve=curve,
        uninformative_mean=float(np.mean(unifo)),
        n_to_decisive=int(np.argmax(np.array(curve) > 5.0)) if (np.array(curve) > 5).any() else -1,
        r_auc=round(_auc(a_agent, a_passive), 2),
        r_agent_mean=round(float(a_agent.mean())),
        r_passive_mean=round(float(a_passive.mean()), 1),
        r_per_intervention=round(per_intervention, 1),
        r_uninformative=round(float(np.mean(unifo)), 1),
        r_uninformative_abs=round(abs(float(np.mean(unifo))), 1),
    )


# --------------------------------------------------------------------------- #
# Study 3 & 4: the battery                                                      #
# --------------------------------------------------------------------------- #
def _complexity(x):
    """Intrinsic unpredictability: entropy of the best passive one-step
    prediction, in nats per step. Chaotic trajectories score high."""
    X0, X1 = x[:-1], x[1:]
    Phi = np.hstack([X0, np.ones((len(X0), 1))])
    W, *_ = np.linalg.lstsq(Phi, X1, rcond=None)
    resid = X1 - Phi @ W
    var = max((resid ** 2).mean(), 1e-9)
    return float(0.5 * np.log(2 * np.pi * np.e * var))


def _battery(rng, reps=60):
    T = T_OBS + 6 * 40
    systems = {
        "diffusion": _sim_diffusion,
        "settling gradient": _sim_bowl,
        "chaotic flow": _sim_chaotic,
        "thermostat": lambda g, r: _sim_agent(g, r, k=0.15),
        "chemotaxis": _sim_agent,
        "regenerator": _sim_regenerator,
    }
    out = {}
    for name, fn in systems.items():
        As, Cs = [], []
        for _ in range(reps):
            g = _intervened_goal(T, rng, 6)
            x = fn(g, rng)
            As.append(agency_score(x, g)); Cs.append(_complexity(x))
        out[name] = dict(A=float(np.mean(As)), C=float(np.mean(Cs)))
    return out


def richness_false_friend(rng) -> dict:
    bat = _battery(rng)
    names = list(bat)
    A = np.array([bat[n]["A"] for n in names])
    C = np.array([bat[n]["C"] for n in names])
    corr = float(np.corrcoef(C, A)[0, 1])
    return dict(
        battery=bat,
        corr_complexity_agency=corr,
        chaotic_A=bat["chaotic flow"]["A"], chaotic_C=bat["chaotic flow"]["C"],
        chemotaxis_A=bat["chemotaxis"]["A"], chemotaxis_C=bat["chemotaxis"]["C"],
        r_corr=round(corr, 2),
        r_corr_abs=round(abs(corr), 2),
        r_chaotic_A=round(bat["chaotic flow"]["A"], 1),
        r_chaotic_C=round(bat["chaotic flow"]["C"], 1),
        r_chemotaxis_A=round(bat["chemotaxis"]["A"], 1),
        r_chemotaxis_C=round(bat["chemotaxis"]["C"], 1),
    )


def agency_ladder(rng) -> dict:
    """The ordered verdict, plus equifinality under obstruction: reaching the
    same goal when the direct path is blocked. A set-point regulator without
    replanning (chemotaxis) fails it; the regenerator passes."""
    bat = _battery(rng)
    ladder = sorted(((n, d["A"]) for n, d in bat.items()), key=lambda kv: kv[1])

    # obstruction test: goal on the far side of a wall; does the system arrive?
    def reach_rate(fn, with_barrier):
        hits = 0; reps = 100
        for _ in range(reps):
            T = 160
            goal = np.array([2.0, 0.0])
            g = np.tile(goal, (T, 1))
            start = np.array([-2.0, 0.0])
            barrier = (0.0, 1.2, 0.5) if with_barrier else None
            if fn is _sim_regenerator:
                x = _sim_regenerator(g, rng, barrier=barrier)
            else:
                x = fn(g, rng)
                if with_barrier:                      # a plain tracker is stopped by the wall
                    x = _sim_agent_walled(g, rng, barrier=(0.0, 1.2))
            if np.linalg.norm(x[-1] - goal) < 0.4:
                hits += 1
        return hits / reps

    equifinal_chemo = reach_rate(_sim_agent, with_barrier=True)
    equifinal_regen = reach_rate(_sim_regenerator, with_barrier=True)
    return dict(
        ladder=ladder,
        equifinality_chemotaxis=equifinal_chemo,
        equifinality_regenerator=equifinal_regen,
        r_equi_chemo=round(equifinal_chemo, 2),
        r_equi_regen=round(equifinal_regen, 2),
    )


def _sim_agent_walled(g, rng, barrier, k=K_TRUE, noise=NOISE):
    """A plain goal-tracker that is physically blocked by a wall (no detour):
    it cannot pass through x = bx within +/- half in y."""
    bx, half = barrier
    T = len(g)
    x = np.zeros((T, DIM)); x[0] = np.array([-2.0, 0.0]) + rng.normal(0, 0.05, DIM)
    for t in range(T - 1):
        proposed = x[t] + k * (g[t] - x[t]) + rng.normal(0, noise, DIM)
        if (x[t, 0] - bx) * (proposed[0] - bx) < 0 and abs(proposed[1]) < half:
            proposed[0] = x[t, 0]                     # blocked: cannot cross the wall
        x[t + 1] = proposed
    return x


def run() -> dict:
    rng = np.random.default_rng(SEED)
    return dict(
        seed=SEED,
        observation_confounded=observation_confounded(rng),
        intervention_reveals=intervention_reveals(rng),
        richness_false_friend=richness_false_friend(rng),
        agency_ladder=agency_ladder(rng),
    )
