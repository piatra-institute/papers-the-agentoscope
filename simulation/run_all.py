"""Orchestrator: reproduces every modelled number in the paper.

    cd simulation
    uv run run_all.py

Writes output/results.json and output/figures/. Seeded (analyses.SEED).
"""
from __future__ import annotations

import json
from pathlib import Path

from analyses import run
from figures import plot_observation_vs_intervention, plot_richness

OUT = Path(__file__).parent / "output"


def main() -> None:
    (OUT / "figures").mkdir(parents=True, exist_ok=True)
    results = run()
    (OUT / "results.json").write_text(json.dumps(results, indent=2))
    plot_observation_vs_intervention(results, str(OUT / "figures" / "observation_vs_intervention.png"))
    plot_richness(results, str(OUT / "figures" / "richness_and_ladder.png"))

    o, i = results["observation_confounded"], results["intervention_reveals"]
    f, l = results["richness_false_friend"], results["agency_ladder"]
    print("1. OBSERVATION IS CONFOUNDED")
    print(f"   AUC agent vs passive (watching)   : {o['auc']:.2f}  (chance)")
    print(f"   max agency score under observation: {o['agent_max']:.2f}  (<= 0 by construction)")
    print("2. INTERVENTION REVEALS")
    print(f"   AUC after goal interventions      : {i['auc']:.2f}")
    print(f"   agent mean / passive mean         : {i['agent_mean']:.0f} / {i['passive_mean']:.1f}")
    print(f"   per informative intervention      : +{i['per_intervention']:.0f} nats")
    print(f"   uninformative perturbation        : {i['uninformative_mean']:.1f}  (no gain)")
    print("3. RICHNESS IS A FALSE FRIEND")
    print(f"   corr(complexity, agency)          : {f['corr_complexity_agency']:.2f}")
    print(f"   chaotic flow  A / complexity      : {f['chaotic_A']:.0f} / {f['chaotic_C']:.1f}")
    print(f"   chemotaxis    A / complexity      : {f['chemotaxis_A']:.0f} / {f['chemotaxis_C']:.1f}")
    print("4. THE AGENCY LADDER")
    for n, a in l["ladder"]:
        print(f"   {n:20s} : {a:8.1f}")
    print(f"   equifinality (reach goal past a wall): chemotaxis {l['equifinality_chemotaxis']:.2f} "
          f"vs regenerator {l['equifinality_regenerator']:.2f}")


if __name__ == "__main__":
    main()
