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

`paper_id,title,authors,year,journal,doi,pmid,study_type,disease_or_context,species,tissue_or_cell_type,main_axis,data_types,public_dataset_accessions,node_discovery_experiments,validation_experiments,key_methods,key_results,validation_level,limitations,topic_class,representative_rank,notes`

## Topic Class Report

For each class:

```markdown
### Class N. Short Name

- Core question:
- Common mechanism or pathway:
- Typical datasets:
- Typical bioinformatics move:
- Typical node-discovery experiment:
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

When classifying validation ladders, explicitly capture decisive assays such as conditional knockout, tissue/cell-specific knockout, mass-spectrometry detection or confirmation, SPR/BLI/ITC molecular interaction assays, Co-IP, CETSA/DARTS, rescue, and phenotype readouts.

分类验证阶梯时，要明确记录关键验证实验，例如条件性敲除、组织/细胞特异性敲除、质谱检测或确认、SPR/BLI/ITC 分子互作检测、Co-IP、CETSA/DARTS、rescue 和表型读出。

Use the weakest applicable tier when a paper mixes strong and weak claims.
