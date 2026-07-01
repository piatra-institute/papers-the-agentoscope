# Audit

Dated log of editorial passes and verification runs. Newest first.
See the workspace docs (run `papers docs`): writing-pipeline.md §7 and refresh-pipeline.md.

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
