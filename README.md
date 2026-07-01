# the-agentoscope

Humans detect agency automatically (a baby, a tiger) and unreliably (a storm, a moving triangle). Like the eye prefigured the lens, that competence prefigures an "agentoscope." This paper argues the instrument is a model comparison: a system is agentic to the degree its behavior is better predicted by a goal-model (a target, a policy that corrects deviations) than by a passive model of forces and noise, scored as A(S) = log P(data|agent)/P(data|passive). The central result is a reversal: agency is unreadable from observation. When the goal is constant the goal-model is a submodel of the passive model, so A <= 0 and a detector separates 300 goal-seekers from 300 passive attractors at AUC 0.49 (chance). Agency lives on Pearl's interventional rung: move the goal or block the path and the system that tracks/reroutes is predicted only by the goal-model — the score climbs ~101 nats per informative intervention and AUC goes to 1.0, while a mere displacement (both recover) informs nothing. Two guards against the human prototype's bias: dynamical richness is a false friend (agency vs complexity correlate -0.63; a chaotic "hurricane" scores lowest despite highest complexity — a false positive), and agency is graded into a ladder (passive < 0 < agentic), with equifinality-under-obstruction (reach the same goal by a different path: 0.00 vs 1.00) separating a set-point regulator from a replanner. The instrument certifies no soul, consciousness, or personhood, is relative to the models compared, needs a boundary it does not supply, and is silent where you cannot perturb (the sun); its honest frontier is downward, into organoids, wounds, and regenerating tissue. Ships a runnable simulation whose output carries every modelled number.

## Build

```bash
uv run build.py          # -> paper/PAPER.pdf  (vendored canonical recipe)
```

Requires `pandoc` and `xelatex` on PATH. From the workspace you can also run
`papers build the-agentoscope`.

## Simulation

```bash
cd simulation && uv run run_all.py   # -> output/results.json, output/figures/
```

Part of [piatra-papers](https://github.com/piatra-institute). See the workspace
docs for the research and writing pipelines.
