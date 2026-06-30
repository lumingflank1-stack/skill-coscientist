# Search and Classification Schema

## Search Strategy Report

`search_strategy.md` should include:

- Research question.
- User constraints.
- Databases searched.
- Exact query strings.
- Search date.
- Inclusion criteria.
- Exclusion criteria.
- Known search limitations.

## Literature Matrix Columns

`paper_id,title,authors,year,journal,doi,pmid,study_type,disease_or_context,species,tissue_or_cell_type,main_axis,data_types,public_dataset_accessions,key_methods,key_results,validation_level,limitations,topic_class,representative_rank,notes`

## Topic Class Report

For each class:

```markdown
### Class N. Short Name

- Core question:
- Common mechanism or pathway:
- Typical datasets:
- Typical bioinformatics move:
- Typical validation ladder:
- Representative papers:
- Strength:
- Weakness:
- Why this class is useful for co-distill:
```

## Evidence Tier Labels

- `background`: useful context, not direct evidence.
- `association`: correlation or differential abundance/expression.
- `multi_dataset_support`: repeated association across cohorts.
- `mechanistic_inference`: pathway, network, ligand-receptor, regulon, trajectory, or CMap inference.
- `perturbation`: knockdown, knockout, inhibitor, stimulation, or rescue.
- `causal_rescue`: perturbation plus downstream rescue or phenotype reversal.

Use the weakest applicable tier when a paper mixes strong and weak claims.
