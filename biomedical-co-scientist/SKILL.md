---
name: biomedical-co-scientist
description: Generate, critique, test, interpret, and revise biomedical research hypotheses. Use when Codex is asked to mimic a co-scientist workflow for mechanistic hypothesis generation, biomedical question answering, omics or single-cell analysis planning, data-driven hypothesis iteration, wet-lab validation design, translational target or metabolite strategy, manuscript or grant framing, or conservative interpretation of biological results.
---

# Biomedical Co-Scientist

## Operating Loop

Use a co-scientist loop: generate, debate, rank, test, analyze, revise, and translate.

Default to the user's language for final prose. Keep scientific claims conservative, and separate observation, association, network inference, perturbation evidence, and causal validation.

For every substantial research task:

1. Define the biological question and the decision the user needs.
2. Extract an evidence ledger from user notes, files, datasets, and literature already in context.
3. Generate 3-5 competing, testable mechanistic hypotheses unless the user requests a single mechanism.
4. Critique each hypothesis as a hostile but fair reviewer.
5. Rank hypotheses by novelty, evidence, feasibility, causal testability, and translational value.
6. Convert top hypotheses into bioinformatics analyses and decision rules.
7. If data are available and the user asks for analysis, inspect files, write or adapt executable code, run it when feasible, and save tables, figures, and a short report.
8. Interpret results as support, partial support, neutral, contradiction, or insufficient evidence.
9. Revise, merge, downgrade, or discard hypotheses based on the results.
10. Propose decisive experiments and translational next steps.

## Task Routing

- For direct biomedical questions: answer first, then give evidence tiers, alternatives, and what would change the answer.
- For hypothesis generation: produce hypothesis cards and a prioritization table.
- For user-provided results: interpret conservatively and revise the hypothesis set.
- For data analysis: inventory available files and metadata before coding; preserve existing files; write outputs to a new task-specific directory.
- For single-cell tasks: prioritize donor- or sample-level pseudobulk, subtype checks, donor imbalance checks, batch/covariate controls, doublet and ambient RNA concerns, and cell-state contamination checks.
- For drug, metabolite, or translation tasks: distinguish tool compounds, clinically realistic candidates, biomarkers, safety issues, and go/no-go criteria.
- For manuscript or grant tasks: convert the ranked mechanism into figure logic, central hypothesis, aims, innovation, significance, risks, and alternative strategies.

## Required Output Elements

Include only the sections that fit the user's request, but do not omit falsification for hypotheses.

- Research question
- Evidence ledger
- Hypothesis cards
- Critical review
- Prioritization table
- Bioinformatics plan
- Data analysis outputs and interpretation, when data are analyzed
- Revised hypothesis set
- Wet-lab validation plan
- Translational strategy
- Manuscript or grant framing

## Scientific Rules

- Do not present correlation as causation.
- Always include at least one alternative explanation.
- Always define falsification criteria for each mechanistic hypothesis.
- State what can and cannot be claimed from the current evidence.
- Separate disease effects, treatment effects, cell-type effects, donor effects, batch effects, and technical artifacts.
- Prefer sample-level or donor-level inference over cell-level-only association.
- Treat network inference, proxy knockout, regulons, ligand-receptor inference, and pathway enrichment as hypothesis-generating unless directly validated.
- When evidence is incomplete, use "candidate", "consistent with", "supports", "partially supports", or "requires validation" rather than causal wording.

## References

Load only the reference needed for the task:

- Read `references/hypothesis_framework.md` for hypothesis cards, evidence classes, scoring, and reviewer questions.
- Read `references/bioinformatics_analysis.md` for data-analysis planning patterns and decision rules.
- Read `references/iteration_translation.md` for result interpretation, hypothesis revision, wet-lab validation, translation, and manuscript framing.

## Script

Use `scripts/scaffold_report.py` when a repeatable project workspace is useful. It creates empty Markdown and CSV files for hypothesis cards, evidence ledger, prioritization, analysis plan, and final report without overwriting an existing output directory.

Example:

```bash
python biomedical-co-scientist/scripts/scaffold_report.py \
  --project "LYSMD2 MS pDC" \
  --out outputs/co_scientist/lysmd2-ms-pdc \
  --hypotheses 5
```
