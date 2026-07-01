"""Figures for The Agentoscope."""
from __future__ import annotations

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from analyses import (_sim_agent, _sim_bowl, _const_goal, _intervened_goal,
                      agency_score, T_OBS)


def plot_observation_vs_intervention(results: dict, path: str) -> None:
    """Score distributions under observation (overlap) vs intervention (separated),
    and the score climbing with each informative intervention."""
    o, i = results["observation_confounded"], results["intervention_reveals"]
    rng = np.random.default_rng(results["seed"] + 1)
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(13.5, 4.2))

    # observation-only distributions
    ao, po = [], []
    for _ in range(300):
        g = _const_goal(T_OBS, rng)
        ao.append(agency_score(_sim_agent(g, rng), g))
        po.append(agency_score(_sim_bowl(g, rng), g))
    lo = min(min(ao), min(po)); hi = max(max(ao), max(po))
    bins = np.linspace(lo, hi, 30)
    ax1.hist(po, bins, alpha=0.6, color="#7f8c8d", label="passive")
    ax1.hist(ao, bins, alpha=0.6, color="#c0392b", label="agent")
    ax1.axvline(0, color="#2c3e50", lw=1)
    ax1.set_title(f"Watching only: AUC = {o['auc']:.2f} (chance)", fontsize=10)
    ax1.set_xlabel("agency score A"); ax1.set_ylabel("count")
    ax1.legend(fontsize=8)

    # intervention distributions
    T = T_OBS + 6 * 40
    ai, pi = [], []
    for _ in range(300):
        g = _intervened_goal(T, rng, 6)
        ai.append(agency_score(_sim_agent(g, rng), g))
        pi.append(agency_score(_sim_bowl(g, rng), g))
    ax2.hist(pi, 30, alpha=0.6, color="#7f8c8d", label="passive")
    ax2.hist(ai, 30, alpha=0.6, color="#c0392b", label="agent")
    ax2.axvline(0, color="#2c3e50", lw=1)
    ax2.set_title(f"After intervention: AUC = {i['auc']:.2f}", fontsize=10)
    ax2.set_xlabel("agency score A"); ax2.legend(fontsize=8)

    # score vs number of informative interventions
    ax3.plot(range(len(i["curve"])), i["curve"], "o-", color="#1b3a5b")
    ax3.axhline(5, color="#27ae60", ls="--", lw=1, label="decisive (log-BF 5)")
    ax3.axhline(i["uninformative_mean"], color="#e67e22", ls=":", lw=1,
                label="uninformative perturbation")
    ax3.set_title("The score climbs per informative intervention", fontsize=10)
    ax3.set_xlabel("number of goal interventions"); ax3.set_ylabel("agency score A")
    ax3.legend(fontsize=8)

    fig.tight_layout(); fig.savefig(path, dpi=140); plt.close(fig)


def plot_richness(results: dict, path: str) -> None:
    """Complexity does not predict agency; the ladder of systems."""
    f, l = results["richness_false_friend"], results["agency_ladder"]
    bat = f["battery"]
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.4))

    for n, d in bat.items():
        col = "#c0392b" if d["A"] > 0 else "#7f8c8d"
        ax1.scatter(d["C"], d["A"], s=55, color=col, zorder=5)
        ax1.annotate(n, (d["C"], d["A"]), textcoords="offset points",
                     xytext=(6, 4), fontsize=8)
    ax1.axhline(0, color="#2c3e50", lw=1)
    ax1.set_xlabel("dynamical complexity  (unpredictability, nats/step)")
    ax1.set_ylabel("agency score A")
    ax1.set_title(f"Richness is a false friend: corr = {f['corr_complexity_agency']:.2f}",
                  fontsize=10)
    ax1.grid(alpha=0.25)

    names = [n for n, _ in l["ladder"]]
    vals = [a for _, a in l["ladder"]]
    cols = ["#c0392b" if a > 0 else "#7f8c8d" for a in vals]
    ax2.barh(names, vals, color=cols)
    ax2.axvline(0, color="#2c3e50", lw=1)
    ax2.set_xlabel("agency score A")
    ax2.set_title("The agency ladder", fontsize=10)
    ax2.grid(alpha=0.25, axis="x")

    fig.tight_layout(); fig.savefig(path, dpi=140); plt.close(fig)
