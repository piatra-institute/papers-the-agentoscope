# The Agentoscope

Why Agency Must Be Perturbed to Be Seen.

Humans detect agency without instruments, reading pursuit in a tiger and intention in a baby quickly, involuntarily, and often wrongly, as in a storm or a moving triangle. Treating this competence as a prototype, as the eye was for the lens, raises the question of what the detector computes and whether it can be calibrated into an instrument, an agentoscope, applicable to systems such as living tissue. The detector is modelled as a model comparison: the agency score is the log-likelihood ratio between a model with a goal and a deviation-correcting policy and a passive model of forces and noise. When the goal is fixed, the goal model is a special case of the passive linear model, so the score cannot be positive under observation; in simulation, 300 goal-seekers and 300 passive attractors are separated at an area under the ROC of 0.49, and no agent scores above zero. Agency therefore belongs to the interventional rung of Pearl's causal hierarchy. When the goal is moved and the system tracks it, the score rises by about 101 nats per intervention and the populations separate at an AUC of 1.0; displacing the state with the goal fixed leaves the score near zero. Across six systems, agency and dynamical complexity are negatively correlated ($r = -0.63$), with a chaotic flow scoring lowest. The score is graded, negative for passive systems and positive for goal-directed ones, and equifinality under obstruction separates a set-point tracker, which reaches a walled-off goal in none of 100 trials, from a regenerator that reaches it in all of them.

## Build

```bash
uv run build.py          # -> paper/PAPER.pdf  (vendored canonical recipe)
```

Requires `pandoc` and `xelatex` on PATH. From the workspace you can also run `papers build the-agentoscope`.

## Simulation

```bash
cd simulation && uv run run_all.py   # -> output/results.json, output/figures/
```

Part of [piatra-papers](https://github.com/piatra-institute). See the workspace docs for the research and writing pipelines.
