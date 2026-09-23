---
title: |
  The Agentoscope:\
  Why Agency Must Be Perturbed to Be Seen
author: PIATRA . INSTITUTE
date: July 2026
---

## Abstract

Humans detect agency without instruments, reading pursuit in a tiger and intention in a baby quickly, involuntarily, and often wrongly, as in a storm or a moving triangle. Treating this competence as a prototype, as the eye was for the lens, raises the question of what the detector computes and whether it can be calibrated into an instrument, an agentoscope, applicable to systems such as living tissue. The detector is modelled as a model comparison: the agency score is the log-likelihood ratio between a model with a goal and a deviation-correcting policy and a passive model of forces and noise. When the goal is fixed, the goal model is a special case of the passive linear model, so the score cannot be positive under observation; in simulation, 300 goal-seekers and 300 passive attractors are separated at an area under the ROC of 0.49, and no agent scores above zero. Agency therefore belongs to the interventional rung of Pearl's causal hierarchy. When the goal is moved and the system tracks it, the score rises by about 101 nats per intervention and the populations separate at an AUC of 1.0; displacing the state with the goal fixed leaves the score near zero. Across six systems, agency and dynamical complexity are negatively correlated ($r = -0.63$), with a chaotic flow scoring lowest. The score is graded, negative for passive systems and positive for goal-directed ones, and equifinality under obstruction separates a set-point tracker, which reaches a walled-off goal in none of 100 trials, from a regenerator that reaches it in all of them.

## 1. Introduction

Every optical instrument had a biological prototype. The lens of the microscope was at work in the eye before anyone ground glass, and the microscope extracted and enlarged a function already implemented in tissue. Agency detection has the same status. Humans run a detector well enough to see agency in a baby, a tiger, a dog, or an adversary, and badly enough to see it in a thunderstorm, a sunspot, or two triangles chasing each other across a screen. Since agency is detected constantly, the open questions are what the detector computes, whether it can be separated from the human case and calibrated, and whether it can then be applied to systems not ordinarily read as agents, such as a slime mould, an organoid, or a regenerating liver.

The instrument cannot detect agency as a substance, a hidden essence that some things have and others lack, because such an essence offers nothing to measure and no useful way to be wrong. It detects a modelling fact: whether a system's behaviour becomes more compressible and more controllable when treated as pursuing, preserving, or regulating something, compared with treating it as moved by external forces. On this reading agency is inferred, from patterns of pursuit, correction, and self-maintenance, as the better of two competing explanations.

This reframing makes the project tractable and yields the main result. If agency is the advantage of a goal model over a passive model, detecting it requires the two models to make different predictions, and under ordinary observation they usually do not. A system holding its state looks the same whether it is falling into an attractor or defending a set-point. The difference, and therefore the agency, appears only when the system is perturbed in the right way, so the instrument must act on the system as well as record it.

## 2. Human agency detection

The human detector is a stack of cues, most of which cognitive science has named. At the base is animacy perception, the reading of self-propelled and contingent motion as alive, shown most clearly by Heider and Simmel: people watching simple shapes move narrate chasing, hiding, and bullying, with motives, from trajectories alone (Heider and Simmel, 1944). Above it is the perception of causality, Michotte's finding that when one object's motion reliably launches another's, the causing is perceived directly (Michotte, 1963). Above that is goal attribution, the reading of behaviour as efficient toward an end, which infants perform in the first year, expecting an agent to take the shorter path to its target and showing surprise when it does not (Gergely et al., 1995; Gergely and Csibra, 2003). Cognitive science has modelled this layer as inverse planning, recovering an agent's goals by inverting a model of how goals produce rational action (Baker, Saxe, and Tenenbaum, 2009), the same structure philosophers describe as the intentional stance, a predictive strategy of ascribing beliefs and desires without claiming to discover an inner substance (Dennett, 1987).

Two properties of the human detector matter for building a better one. Its deepest cue is future-directedness: a trajectory reads as agentic when it seems governed by where the system is going as well as by where it has been. And the detector is known to be miscalibrated. Under ambiguity, threat, or noise, people over-attribute agency, seeing faces in clouds and intentions in weather, a bias described as a hyperactive agency detection device and proposed as a cognitive root of supernatural belief (Barrett, 2000; Guthrie, 1993). An instrument that extracts the human competence must also correct this error, and the comparison between passive and agentic models, applied under intervention, supplies the correction.

## 3. Agency as a model comparison

Let a system produce a trajectory of states, and compare two models of it. A passive model explains the trajectory by autonomous dynamics: forces, relaxation toward equilibrium, and noise, without reference to any goal. An agent model explains the same trajectory as the pursuit of a goal, a policy that reduces the gap between the current state and a target. The agency score is the log-likelihood ratio,

$$A(S) = \log \frac{P(\text{data} \mid \text{agent model})}{P(\text{data} \mid \text{passive model})},$$

a Bayes factor in the standard sense, positive when the goal model predicts the data better and negative when the passive model does (Kass and Raftery, 1995). The instrument reports that the system's behaviour is better compressed by a model containing a latent goal and by how much, a quantity open to argument from evidence.

In the simulations the passive model is the best-fitting autonomous linear dynamics $x_{t+1} = A x_t + b$, and the agent model is $x_{t+1} = x_t + k(g_t - x_t)$, coupled to a goal channel $g_t$ that the experimenter controls; both are fitted by least squares and scored by their one-step Gaussian log-likelihood. The word agency carries more than this score measures. Agency in this sense excludes intelligence, consciousness, and personhood. A system can score high by defending a set-point without solving novel problems (intelligence), without there being anything it is like to be it (consciousness), and without any claim to moral or legal standing (personhood) (Barandiaran, Di Paolo, and Rohde, 2009). A thermostat has a small degree of agency and no intelligence; a liver may have organ-level agency and no experience. Keeping these distinct prevents the instrument from drifting toward panpsychism: it measures the degree to which a goal is the better model and says nothing about the rest.

## 4. Observational equivalence of goal-seeking and passive relaxation

Under observation alone the agency signal is absent, and this follows from a simple structural fact.

A goal-seeker that reduces its distance to a fixed target relaxes toward the target and then holds. A passive point attractor, such as a ball settling in a bowl centred on the same point, follows the same mathematical form, linear relaxation toward a centre. With a constant goal, $x_t + k(g - x_t) = (1-k)x_t + kg$ is a member of the passive family, so the passive model fits every constant-goal trajectory at least as well as the agent model and the agency score cannot be positive. In a simulation of 300 goal-seekers and 300 passive attractors observed with fixed goals, the separation between the two populations is an area under the ROC of 0.49, indistinguishable from chance; across all 300 agents the score never exceeds zero, with a maximum of $-0.06$. The failure is a property of the data and would affect any observer.

The good-regulator theorem gives the underlying reason: any system that effectively regulates a variable must contain a model of what it regulates, so a well-run controller and the system it controls come to mirror each other (Conant and Ashby, 1970). That mirroring is internal. From outside, a system holding a variable steady and a system in which the variable is at rest look identical. Regulation is a fact about what the system would do if the variable were pushed, and without a push it is invisible. This is why animacy perception relies so heavily on motion and contingency, and why still or steady systems, however alive, do not trigger it.

## 5. Detection by intervention

If agency is a fact about how a system responds to disturbance, detecting it is an interventional problem, located on the higher rungs of Pearl's ladder of causation, where questions are settled by acting on a system (Pearl, 2009). The agentoscope's basic operation is a deliberate perturbation, a do-operation applied to the system's putative goal or its path, followed by a reading of the response. This is the modern form of the cybernetic idea that purposeful behaviour is organized around a goal by negative feedback and is demonstrated by disturbing the system and observing its correction (Rosenblueth, Wiener, and Bigelow, 1943).

In the simulation the same goal-seekers and passive attractors that were indistinguishable at rest are subjected to six interventions, each moving the goal to a new location for 40 steps. The goal-seeker tracks each moved target, a response only the agent model, which has access to the goal variable, can predict; the autonomous passive model fails at every jump. The mean score rises by about 101 nats per intervention, from $-2.7$ with none to 604 with six, and the populations separate at an area under the ROC of 1.0. The agents reach a mean score of 589, while the passive systems, which ignore the goal perturbations, average $-66$. A single intervention already lifts the mean score past a log Bayes factor of 5 (Figure 1).

![Agency scores under observation and under intervention. Left: score distributions for goal-seekers and passive attractors with a fixed goal; the reported AUC is 0.49 and no agent scores above zero. Middle: score distributions after six goal interventions; the reported AUC is 1.0. Right: mean agency score against the number of goal interventions, rising by about 101 nats per intervention; the dotted line marks the mean score ($-2.3$) when the state is displaced with the goal fixed. The distributions in the left and middle panels are an independent replicate of the reported runs.](../simulation/output/figures/observation_vs_intervention.png){width=100%}

Not every disturbance is informative, and this determines which perturbations to perform. If the state is displaced while the goal stays fixed, both a passive attractor and a goal-seeker return, so the recovery is shared and the score remains near $-2.3$ in the simulation, no better than observation. The perturbations that reveal agency dissociate the goal from the mechanism: moving the target so that tracking it and staying put come apart, or blocking the direct path so that reaching the goal requires leaving the default trajectory. Resilience alone does not indicate agency, since a rock rolled uphill also returns. The signature is counterfactual goal preservation: the system continues to reach or hold the same target across changes of path, obstacle, and starting point that a passive process would not survive.

## 6. Dynamical complexity and agency

The characteristic error of the human detector is to read agency into complexity, perceiving the churn of a storm or the flicker of a fire as striving. The model comparison protects the instrument from this error, because complexity and agency are different measurements that co-occur in familiar animals.

A battery of six systems, a diffusion, a settling gradient, a chaotic flow (a rescaled Hénon map), a thermostat, a chemotactic tracker, and a regenerator, is scored for agency under goal intervention and, separately, for dynamical complexity, the entropy of the best passive one-step prediction. Across the battery the two scores are negatively correlated, $r = -0.63$ over the six system means. The chaotic flow has the highest complexity in the battery and the lowest agency score, about $-527$, because when its putative goal is moved it does nothing goal-like and the goal model is penalized for expecting a response. The chemotactic tracker, whose trajectory is simple, follows its moved target and scores about 550. This quantifies the intuition that a hurricane is a false positive while a liver is a genuine candidate. A hurricane maintains structure and displays rich dynamics but preserves no internal variable against intervention. A liver holds its regime, corrects its outputs, and rebuilds toward a target after injury, and would respond to perturbation as an agent does. Dynamical richness does not indicate agency; a goal-preserving response to intervention does.

## 7. Graded agency and equifinality

Measured this way, agency is graded, and the instrument orders systems along a scale. Below zero are the passive systems: the chaotic flow (about $-531$ in the ladder run), the settling gradient ($-67$), and the diffusion ($-5.5$). Above zero are the goal-directed systems: the thermostat, with a lower controller gain (378), and the chemotactic tracker and regenerator (598 and 576). Without an obstacle the regenerator's dynamics coincide with the tracker's, and the order of these two scores reverses between independent battery runs (550 and 583 in the complexity run), so goal-shift scores alone do not separate them. The ordering follows from how strongly each system's behaviour is coupled to a goal it defends under perturbation (Figure 2).

![Agency score, dynamical complexity, and the ordering of systems. Left: mean agency score under goal intervention against dynamical complexity (entropy of the best passive one-step prediction) for six systems; the correlation is $-0.63$. Right: mean agency score by system in an independent run; passive systems score below zero and goal-directed systems above.](../simulation/output/figures/richness_and_ladder.png){width=100%}

The top of the scale requires a further criterion, since tracking a goal is not the strongest capacity an agent can display. The stronger property is equifinality, reaching the same end by different means, which von Bertalanffy identified as the mark of an open system pursuing a goal (von Bertalanffy, 1968). It is tested by placing a wall between a system and its target. A plain set-point tracker that moves only down the gradient toward its goal is stopped by the wall and reaches the target in none of 100 trials. A regenerator that detours around the obstacle reaches it in all 100. Under simple goal shifts the two are nearly equal and both clearly agentic; only the obstruction separates them, completely. This is the operational core of the liver and embryo cases, in which a disturbed system navigates to a target configuration by a route it would not otherwise take, the behaviour that the basal-cognition literature reads as goal-directedness in anatomical and physiological space (Levin, 2019; Friston et al., 2015). It is also why the agentoscope's most promising applications are in tissue and morphogenesis and not in weather, which so reliably misleads unaided perception.

## 8. Limitations

The score is relative to the models compared, a limitation inherent to the method. It is high or low only against a specific passive alternative, and a sufficiently elaborate passive model can absorb any given behaviour at the cost of complexity and lost generality. The instrument reports the margin by which a goal model out-predicts the best passive model written down, so its output is a score against a named alternative at a stated scale and never a binary verdict. The good-regulator theorem applies here as well: a sufficiently good passive model of a regulated system must resemble the agent's own model, so the two families converge in the limit, and the score measures how far the current passive account falls short of that limit.

The instrument requires a boundary it does not supply. Before scoring, the candidate unit must be specified, where the system ends and the environment begins, and this individuation remains unsolved, whether posed as drawing a Markov blanket around a self-organizing region or as identifying the self-producing closure of an autopoietic system (Friston, 2013; Maturana and Varela, 1980). With the wrong boundary a regulating organ can look like passive plumbing, and a passive aggregate can look like a striving whole.

The instrument can err in both directions, and its correction has a cost. A naive agentoscope run in observation mode would inherit the human over-attribution bias, since without intervention the score is uninformative and any decision threshold on it produces false positives. Intervention removes this over-attribution, which is the method's main advance over the human prototype and over passive statistical agency detection. Intervention is not always available, however: the sun's goal cannot be moved to test whether it tracks, and for systems that cannot be perturbed the instrument returns no score. Other operationalizations of the same idea exist, including empowerment, an agent's control over its future sensory states, and active inference, the minimization of expected surprise; the model-comparison score is one member of this family (Klyubin, Polani, and Nehaniv, 2005; Friston, 2010).

The simulations are minimal. The passive family is linear, the systems are two-dimensional, the complexity correlation rests on six system means, and the regenerator's detour around the wall is part of its specified dynamics, so the equifinality test shows that the criterion separates the two controllers and does not show how detours arise.

## 9. Conclusion

The agentoscope converts a competence that humans exercise automatically and unreliably, the reading of goals into motion, into a procedure with a number and a scale. Under observation, goal-seeking and passive relaxation are indistinguishable (AUC 0.49); under goal interventions the score rises by about 101 nats per intervention and separates them completely (AUC 1.0). Complexity and agency are scored separately and are negatively related across the battery, and equifinality under obstruction distinguishes a regenerator from a set-point tracker. Applied to organoids, wounds, and regenerating organs, the instrument reports where, at what scale, and under which interventions a goal is the better account of a system's behaviour.

## References

Baker, C. L., Saxe, R., and Tenenbaum, J. B. (2009). Action understanding as inverse planning. *Cognition*, 113(3), 329–349.

Barandiaran, X. E., Di Paolo, E., and Rohde, M. (2009). Defining agency: individuality, normativity, asymmetry, and spatio-temporality in action. *Adaptive Behavior*, 17(5), 367–386.

Barrett, J. L. (2000). Exploring the natural foundations of religion. *Trends in Cognitive Sciences*, 4(1), 29–34.

Conant, R. C., and Ashby, W. R. (1970). Every good regulator of a system must be a model of that system. *International Journal of Systems Science*, 1(2), 89–97.

Dennett, D. C. (1987). *The Intentional Stance*. MIT Press.

Friston, K. (2010). The free-energy principle: a unified brain theory? *Nature Reviews Neuroscience*, 11(2), 127–138.

Friston, K. (2013). Life as we know it. *Journal of the Royal Society Interface*, 10(86), 20130475.

Friston, K., Levin, M., Sengupta, B., and Pezzulo, G. (2015). Knowing one's place: a free-energy approach to pattern regulation. *Journal of the Royal Society Interface*, 12(105), 20141383.

Gergely, G., and Csibra, G. (2003). Teleological reasoning in infancy: the naïve theory of rational action. *Trends in Cognitive Sciences*, 7(7), 287–292.

Gergely, G., Nádasdy, Z., Csibra, G., and Bíró, S. (1995). Taking the intentional stance at 12 months of age. *Cognition*, 56(2), 165–193.

Guthrie, S. E. (1993). *Faces in the Clouds: A New Theory of Religion*. Oxford University Press.

Heider, F., and Simmel, M. (1944). An experimental study of apparent behavior. *American Journal of Psychology*, 57(2), 243–259.

Kass, R. E., and Raftery, A. E. (1995). Bayes factors. *Journal of the American Statistical Association*, 90(430), 773–795.

Klyubin, A. S., Polani, D., and Nehaniv, C. L. (2005). Empowerment: a universal agent-centric measure of control. In *Proceedings of the 2005 IEEE Congress on Evolutionary Computation* (pp. 128–135). IEEE.

Levin, M. (2019). The computational boundary of a "self": developmental bioelectricity drives multicellularity and scale-free cognition. *Frontiers in Psychology*, 10, 2688.

Maturana, H. R., and Varela, F. J. (1980). *Autopoiesis and Cognition: The Realization of the Living*. D. Reidel.

Michotte, A. (1963). *The Perception of Causality* (T. R. Miles and E. Miles, Trans.). Basic Books. (Original work published 1946.)

Pearl, J. (2009). *Causality: Models, Reasoning, and Inference* (2nd ed.). Cambridge University Press.

Rosenblueth, A., Wiener, N., and Bigelow, J. (1943). Behavior, purpose and teleology. *Philosophy of Science*, 10(1), 18–24.

Bertalanffy, L. von (1968). *General System Theory: Foundations, Development, Applications*. George Braziller.
