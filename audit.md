# Audit

Dated log of editorial passes and verification runs. Newest first.
See the workspace docs (run `papers docs`): writing-pipeline.md §7 and refresh-pipeline.md.

## 2026-09-23 — structured-evidence migration

Structured-evidence migration (references and claims).
- references.yaml: 20 CSL entries. 12 matched in Crossref; 4 completed by hand from DOI records (friston2010, klyubin2005, maturana1980, pearl2009); 4 books entered by hand (dennett1987, guthrie1993, michotte1963, bertalanffy1968). "(von Bertalanffy, 1968)" converted by hand. The legacy reference list is replaced by the citeproc-rendered list (Chicago author-date).
- Bibliographic corrections: conant1970 record case normalized and a stray dagger removed from the title; heider1944 page range completed (243-259); levin2019 volume and article number added. No prose or numerical corrections.
- Simulation: analyses.py names the design constants it already used (N_JUMPS 6, SEG 40, DECISIVE 5.0, EQUI_REPS 100) and writes them to a new design block so the prose statements "six interventions ... 40 steps", "log Bayes factor of 5" and "100 trials" bind; the seeded run reproduces every previously stored value, and figures are byte-identical. An earlier receipt from a run before the edit is retained in verification/ as the tool keeps prior receipts.
- claims.yaml: 53 claims (39 computation, 7 source, 4 interpretation, 2 definition, 1 assumption). Computation claims bind every number in the abstract, body, captions and conclusion to simulation/output/results.json under run agentoscope. Source claims verified against abstracts: Gergely et al. 1995 (12-month-olds expect the rational means), Baker et al. inverse planning, Kass and Raftery Bayes factors, Conant and Ashby good regulator, Friston 2013 Markov blanket, Levin 2019 goal-pursuing individuals, Klyubin et al. empowerment.
- Not verified, not bound: Heider and Simmel, Michotte, Dennett, Guthrie, Barrett (hyperactive agency detection not in abstract), Barandiaran et al. (intelligence/consciousness/personhood distinction not in abstract), Rosenblueth et al. negative feedback (abstract does not state it), Pearl, von Bertalanffy equifinality, Maturana and Varela, Friston 2010.
- Execution receipt: verification/agentoscope.json (uv run python run_all.py).
- metadata claims_target: results.json -> claim-ledger.

## 2026-09-23 — prose revision

Prose rewritten against the house standards. Headings made descriptive (Abstract, 1 Introduction, 2 Human agency detection, 3 Agency as a model comparison, 4 Observational equivalence of goal-seeking and passive relaxation, 5 Detection by intervention, 6 Dynamical complexity and agency, 7 Graded agency and equifinality, 8 Limitations, 9 Conclusion). "Rather than" 14 -> 0, "this/the paper" 3 -> 0, "not X but Y" 6 -> 0, negate-pivots 3 -> 0, "merely/simply" 7 -> 0, "worth" 2 -> 0.

Corrections:
  - Ladder ordering: the text listed the goal-directed systems "in ascending order" as thermostat, chemotactic tracker, regenerator. In the ladder run the order is chemotaxis 598 > regenerator 576 (in the complexity run it is regenerator 583 > chemotaxis 550). In the battery the regenerator has no barrier, so its dynamics are identical to the chemotactic tracker's and the difference is sampling noise. The text now reports both runs and says goal-shift scores do not separate the two; only the obstruction test does.
  - Complexity correlation r = -0.63 is now stated as computed over six system means.
  - Limitations now state that the regenerator's detour is built into its dynamics, so the equifinality test (0/100 vs 100/100) shows that the criterion separates the controllers, not how detours arise.
All other numbers match results.json (AUC 0.49 and 1.0; agent max -0.06; 101 nats per intervention, curve -2.7 to 604; agent mean 589, passive -66; displacement -2.3; chaotic -527, chemotaxis 550; ladder -531, -67, -5.5, 378, 576, 598). Grid-artifact audit: no threshold or optimum is read from a grid; AUCs are exact Mann-Whitney statistics over the simulated scores.
Figures: the two generated figures were not in the manuscript; now embedded as Figures 1 and 2. Titles replaced ("Watching only", "After intervention", "The score climbs per informative intervention", "Richness is a false friend", "The agency ladder" -> descriptive); the histogram panels are drawn from an independent replicate (seed + 1), which the caption now says. results.json byte-identical after the re-run.

## 2026-07-01 — Initial implementation from seed chat
Scope: full paper built from `chats/chat.md` (a single-turn ChatGPT exchange developing the "agentoscope": an instrument that detects agency by model comparison, core signal "counterfactual goal preservation under perturbation") through the PIATRA pipeline.
Decision: the corpus already has a Bayesian agency paper (proof-of-agency, passive signal detection). To break the fingerprint, this paper's spine is INTERVENTIONAL — Pearl's ladder of causation: the headline is that agency is invisible on the observational rung and legible only under intervention, with equifinality-under-obstruction as the signature. This inverts the usual "watch and infer," which is a genuinely different result-shape from the corpus's thresholds and negative-IDs.
Changes:
  - Instrument: A(S) = log P(data|agent model)/P(data|passive model). Key theorem made computable: under a constant goal the agent model (linear in x) is a submodel of the passive linear model, so A <= 0 by construction — observation cannot detect agency.
  - Simulation (numpy + matplotlib, uv, seeded SEED=20260701): (1) OBSERVATION CONFOUNDED — AUC 0.49 (chance), max score -0.06; (2) INTERVENTION REVEALS — goal-shift gives AUC 1.0, +101 nats/informative intervention, uninformative displacement ~ -2.3; (3) RICHNESS A FALSE FRIEND — corr(complexity, agency) = -0.63, chaotic flow highest complexity / lowest agency (-527), chemotaxis low complexity / high agency (+550); (4) AGENCY LADDER — passive systems < 0 < agentic, and equifinality-under-obstruction 0.00 (plain tracker) vs 1.00 (regenerator).
  - Wrote PAPER.md (8 sections, argument-driven distinctive titles, no ceremonial intro/conclusion; claim-strength throughout; agency distinguished from intelligence/consciousness/personhood to avoid panpsychist mush; §8 folds the objections — model-relativity, the boundary/individuation problem, HADD, the un-perturbable-system limit, empowerment/active-inference alternatives).
  - 20-source bibliography, all engaged in-text, verified in a dedicated pass (JSTOR/PubMed/DOI); 1 correction (Wiener 1948 publisher) and Wiener 1948 dropped to keep the set load-bearing. 0 confabulated (refs MISSING = 0).
Verification:
  - voice: 0 errors, 5 review-candidate warns (negate-pivot / inline-contrastive, intrinsic). Lexical density low (exactly 3, honest 3); no cleanup needed.
  - refs: 0 missing, 0 unused (20 in-text keys, 20 bib entries; fixed the von-Bertalanffy key to "Bertalanffy, L. von" so the in-text surname reconciles).
  - claims: 5 prose decimals, 0 without a matching results.json value (added magnitude keys so "negative 0.06 / 2.3 / 0.63" reconcile).
  - build: clean, 0 missing-character warnings.
  - check => PASS
