# Routine Distillation Schema

## Routine Distillation Report

```markdown
# Routine Distillation

## Source Set

## One-Sentence Routine

In [disease/context], identify [candidate node/state] through [public-data or omics move], discover [downstream molecule/mechanism/phenotype node] through [node-discovery experiment], validate the node through [validation ladder], and test mechanism through [experiment ladder], leading to [manuscript claim].

## Reusable Routine

1. Entry problem:
2. Public-data discovery:
3. Node-discovery experiment:
4. Candidate prioritization:
5. Cross-dataset validation:
6. Cell-type or tissue specificity:
7. Mechanistic inference:
8. Validation experiment:
9. Experimental perturbation:
10. Rescue or causality:
11. Translational angle:

## What To Copy

## What Not To Copy

## Reviewer Risks
```

## Figure Logic Table Columns

`figure,panel,panel_job,input_data_or_assay,comparison,claim_supported,evidence_tier,common_design_pattern,reusable_for_new_topic,notes`

## Dataset and Assay Inventory Columns

`item_id,source_paper,data_or_assay_type,accession_or_reagent,organism,tissue_or_cell_type,comparison,role_in_routine,node_discovery_or_validation,reusable_requirement,notes`

## Node Discovery Experiment Map

Track how each source paper discovers the downstream molecule, mechanism node, or phenotype-linked mediator:

```markdown
| Paper | Upstream perturbation or condition | Discovery assay | Data type | Node found | Why this node matters | Follow-up validation |
|---|---|---|---|---|---|---|
```

Typical node-discovery experiments include:

- differential transcriptomics after disease, treatment, knockout, knockdown, overexpression, or conditional knockout;
- proteomics, phosphoproteomics, secretomics, metabolomics, ubiquitinomics, acetylomics, or spatial omics;
- IP-MS, pull-down-MS, thermal proteome profiling, DARTS/CETSA-MS, or target-fishing assays;
- CRISPR/RNAi screen, reporter screen, pooled perturb-seq, or CMap-style perturbation matching;
- phenotype-linked imaging, flow, spatial neighborhood, ligand-receptor, or cell-cell communication screens.

Validation experiments are separate and should be extracted explicitly. Important validation examples include conditional knockout or tissue/cell-specific knockout, knockdown/overexpression, rescue, neutralization, inhibitor/agonist, mass-spectrometry detection or confirmation such as targeted MS/PRM/SRM, Co-IP-MS, IP-MS or pull-down-MS confirmation, SPR/BLI/ITC molecular interaction assays, Co-IP, CETSA/DARTS, reporter assays, and phenotype rescue.

验证实验必须单独提取。重要验证实验包括条件性敲除或组织/细胞特异性敲除、敲低/过表达、rescue、中和、抑制剂/激动剂、质谱检测或确认如 targeted MS/PRM/SRM、Co-IP-MS、IP-MS 或 pull-down-MS 确认、SPR/BLI/ITC 分子互作检测、Co-IP、CETSA/DARTS、报告基因和表型 rescue。

## Novelty and Gap Map

Track three layers:

- `known`: already established in source papers.
- `transferable_gap`: same routine could answer a different disease, cell type, node, or intervention.
- `danger_zone`: too close to source papers or unsupported by available data.

## Replication Template

The template should be abstract enough to reuse:

```markdown
1. Select disease/context with unmet mechanism.
2. Retrieve public dataset type A.
3. Identify candidate node by contrast B.
4. Run or reuse node-discovery experiment C to find downstream molecule/mechanism/phenotype mediator.
5. Validate across dataset type D.
6. Test cell-type specificity.
7. Link to pathway or mediator.
8. Validate the node by perturbation or direct interaction.
9. Add rescue or downstream phenotype readout.
10. Write Results in figure order.
```
