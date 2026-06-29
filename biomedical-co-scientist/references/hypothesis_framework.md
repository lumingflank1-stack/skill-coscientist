# Hypothesis Framework

Use this reference when the user asks for hypothesis generation, mechanism ranking, reviewer critique, or "co-scientist" reasoning.

## Evidence Ledger

Record the source and strength of each claim before building hypotheses.

Evidence classes:

- User observation: directly supplied by the user; preserve wording and context.
- Local data result: derived from files or analyses in the workspace.
- Public literature: cite source when available; do not overquote.
- Public database: distinguish curated annotation from inferred association.
- Computational inference: correlation, enrichment, network inference, proxy knockout, regulon, ligand-receptor, CMap, or model output.
- Perturbation evidence: knockdown, knockout, inhibitor, rescue, stimulation, animal model, or clinical intervention.
- Direct causal evidence: perturbation plus expected downstream rescue or loss of phenotype.

Use the weakest applicable wording when classes conflict.

## Hypothesis Card

For each hypothesis, use this structure:

```markdown
### H1. Short Mechanistic Name

- Core mechanism:
- Predicted molecular or cellular axis:
- Primary evidence:
- Evidence tier:
- Key predictions:
- Critical weakness:
- Alternative explanation:
- Bioinformatics tests:
- Decisive experiment:
- Falsification criteria:
- Translational angle:
- Current status: candidate / prioritized / weakened / rejected / validated
```

Generate hypotheses that compete with each other, not just variations of the same story. Include at least one null or confounding hypothesis when the data are associative.

## Reviewer Critique

For each hypothesis, ask:

- Is the central evidence cell-level correlation, donor-level association, perturbation, or direct causal rescue?
- Could disease state, treatment, sex, age, batch, donor imbalance, subtype composition, doublets, or ambient RNA explain the signal?
- Is the proposed upstream trigger present in the relevant cell type and disease context?
- Does the downstream readout measure the specific mechanism or a broad activation state?
- What result would make the hypothesis unlikely?
- What single experiment would most improve causal confidence?

End critique with:

- Major concerns
- Minor concerns
- Decisive experiment
- Publication readiness if validated

## Prioritization Rubric

Score each item from 1 to 5.

| Criterion | 1 | 3 | 5 |
| --- | --- | --- | --- |
| Novelty | Known or incremental | Fresh combination | Mechanistically surprising and plausible |
| Evidence strength | Single weak association | Multiple converging associations | Perturbation or external validation |
| Feasibility | Hard model or no readout | Feasible with caveats | Clear data and assays |
| Causal testability | Vague or indirect | Testable with controls | Direct perturbation and rescue |
| Translational value | No actionable node | Biomarker or pathway | Druggable, metabolite, or clinical path |

Prioritize the highest total score, but flag any hypothesis with high novelty and low evidence as "high-risk candidate" rather than discarding it.

## Output Table

```markdown
| Rank | Hypothesis | Novelty | Evidence | Feasibility | Causal testability | Translation | Total | Decision |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | H1 | 4 | 3 | 5 | 4 | 4 | 20 | Test first |
```
