# Research

Findings, tiered by source proximity. See the workspace docs (`papers docs`): research-pipeline.md §2.
T1 primary · T2 authoritative secondary · T3 reference · T4 general web (leads only).
A claim that reaches the paper rests on a T1 or T2 source.

## Findings

Simulation (own computation, T1 — simulation/analyses.py, seeded SEED=20260701):
- [T1] Observation confounded: under a constant goal the agent model x_{t+1}=x_t+k(g-x_t) is linear in x, hence a submodel of the passive linear model x_{t+1}=A x_t+b, so A(S) <= 0 identically. 300 agents vs 300 passive attractors watched at rest: AUC = 0.49 (chance), max agent score -0.06. — §4.
- [T1] Intervention reveals: goal-shift interventions give AUC = 1.0; agent mean ~589 vs passive ~ -66; +101 nats per informative intervention; one intervention already crosses decisive (log-BF 5). Uninformative perturbation (displace state, hold goal) ~ -2.3 (no gain). — §5.
- [T1] Richness a false friend: across a battery, corr(complexity, agency) = -0.63; chaotic flow highest complexity (C=1.0) and lowest agency (A ~ -527); chemotaxis low complexity, A ~ +550. — §6.
- [T1] Agency ladder: chaotic (-531) < settling gradient (-67) < diffusion (-5.5) < thermostat (+378) < regenerator (+575) < chemotaxis (+598); equifinality-under-obstruction (reach goal past a wall) chemotaxis 0.00 vs regenerator 1.00. — §7.

Human detector / cognition (T1/T2):
- [T1] Heider & Simmel (1944, Am. J. Psychol. 57:243): intention read into moving shapes. Michotte (1963/1946): perceived causality. — §2.
- [T1] Gergely, Nádasdy, Csibra & Bíró (1995, Cognition 56:165); Gergely & Csibra (2003, TICS 7:287): infant teleological stance. Baker, Saxe & Tenenbaum (2009, Cognition 113:329): inverse planning. — §2-3.
- [T2] Dennett (1987): intentional stance. Barrett (2000, TICS 4:29); Guthrie (1993): HADD / over-attribution. — §2, §8.

Cybernetics / control / teleology (T1/T2):
- [T1] Rosenblueth, Wiener & Bigelow (1943, Phil. Sci. 10:18): purpose = feedback toward a goal, shown by disturbance/correction. — §5.
- [T1] Conant & Ashby (1970, Int. J. Syst. Sci. 1:89): good-regulator theorem — a regulator embodies a model, latent until the variable is perturbed. — §4.
- [T2] von Bertalanffy (1968): equifinality — same end by different paths; top-of-ladder criterion. — §7.

Formal agency / causality (T1/T2):
- [T1] Pearl (2009, Causality, 2nd ed.): ladder of causation; agency an interventional property. — §5, spine.
- [T2] Kass & Raftery (1995, JASA 90:773): Bayes factors; decisive-evidence thresholds. — §3, §5.
- [T2] Barandiaran, Di Paolo & Rohde (2009, Adaptive Behavior 17:367): defining agency; the distinction from consciousness/personhood. — §3, §8.
- [T2] Friston (2010, Nat. Rev. Neurosci. 11:127); Klyubin, Polani & Nehaniv (2005, IEEE CEC): active inference / empowerment as alternative operationalizations. — §8.

Boundary / basal cognition (T2):
- [T2] Friston (2013, JRSI 10:20130475): Markov blankets. Maturana & Varela (1980): autopoiesis. — §8 (individuation problem).
- [T2] Levin (2019, Front. Psychol. 10:2688); Friston, Levin, Sengupta & Pezzulo (2015, JRSI 12:20141383): scale-free/basal cognition; goals in anatomical space; regeneration. — §7, the downward frontier.

Verification: 23 candidates verified against JSTOR/PubMed/DOI; 1 correction (Wiener 1948 publisher; Wiener 1948 subsequently dropped). 0 confabulated.
