# Analysis and Experiment Plan Schema

## Analysis Plan

```markdown
# Analysis Plan

## Active Claim

## Input Data

## Required Metadata

## Preprocessing and QC

## Main Comparison or Model

## Covariates and Confounders

## Decision Rules

## Expected Tables

## Expected Figures

## Failure Modes
```

## Dataset Manifest Columns

`dataset_id,source_database,accession,title,species,tissue_or_cell_type,data_type,comparison,required_metadata,download_status,local_path,analysis_role,expected_signal,minimum_success_condition,notes`

Download status values:

- `needs_search`
- `needs_download`
- `downloaded`
- `blocked`
- `not_suitable`

## Experiment Plan

```markdown
# Experiment Plan

## Node Discovery Experiment

- Biological question:
- Starting contrast or perturbation:
- Model or sample:
- Discovery assay:
- Data type:
- Candidate node selection rule:
- Expected downstream molecule/mechanism/phenotype node:
- Required controls:
- Failure or ambiguity mode:

## Decisive Experiment

- Model:
- Samples:
- Perturbation:
- Conditional knockout or tissue/cell-specific knockout:
- Mass-spectrometry detection or confirmation:
- Rescue:
- Direct interaction assay:
- SPR/BLI/ITC molecular interaction assay:
- Stimulation:
- Controls:
- Time points:
- Readouts:
- Expected support result:
- Falsification result:
- Sample size logic:
- Technical risks:
- Backup plan:
```

Node discovery and validation are different evidence jobs:

- Node discovery finds the downstream molecule, mechanism node, or phenotype-linked mediator. Examples include RNA-seq/scRNA-seq/spatial omics after perturbation, proteomics, phosphoproteomics, secretomics, metabolomics, IP-MS/pull-down-MS, CRISPR/RNAi screen, perturb-seq, target fishing, and phenotype-linked imaging or flow screens.
- Validation tests the selected node. Important examples include conditional knockout or tissue/cell-specific knockout, knockdown/overexpression, rescue, neutralization, inhibitor/agonist, mass-spectrometry detection or confirmation such as targeted MS/PRM/SRM, Co-IP-MS, IP-MS or pull-down-MS confirmation, SPR/BLI/ITC molecular interaction assays, Co-IP, CETSA/DARTS, reporter assays, and phenotype rescue.

节点发现和验证是两个不同证据功能：

- 节点发现负责找到下游分子、机制节点或表型关联介质，例如扰动后的 RNA-seq/scRNA-seq/空间组学、蛋白组、磷酸化组、分泌组、代谢组、IP-MS/pull-down-MS、CRISPR/RNAi screen、perturb-seq、target fishing，以及表型关联成像或流式筛选。
- 验证负责检验被选中的节点，重要例子包括条件性敲除或组织/细胞特异性敲除、敲低/过表达、rescue、中和、抑制剂/激动剂、质谱检测或确认如 targeted MS/PRM/SRM、Co-IP-MS、IP-MS 或 pull-down-MS 确认、SPR/BLI/ITC 分子互作检测、Co-IP、CETSA/DARTS、报告基因和表型 rescue。

## Virtual Result Prompt

Use only when the user explicitly wants simulated or virtual results.

Before writing this prompt, perform or require a compact literature/public-data feasibility and novelty scan unless the user has fixed the result axis. Select the positive result axis that is both highly plausible and maximally innovative, with no directly equivalent prior study found in the scanned literature. Save the reasoning in `virtual_result_rationale.md` or `assumed_result_explanation.md`.

只有用户明确要求虚拟或模拟结果时才使用本模板。撰写 prompt 前，除非用户已经固定结果轴，否则先做或要求一轮简洁的文献/公共数据可行性和创新性扫描；选择既高度可能成立、又最有创新性，且在已扫描文献中未见直接同构研究的阳性结果轴，并将理由保存到 `virtual_result_rationale.md` 或 `assumed_result_explanation.md`。

```markdown
# Virtual Result Prompt

You are generating virtual planning data for manuscript drafting. Write downstream manuscript-facing prose in conventional Results style, and record virtual source status only in the report or source ledger unless the user asks for visible labels.

Research topic:
Active hypothesis:
Desired result mode: positive / negative / ambiguous / mixed
Assays to simulate:
Node-discovery experiments to simulate:
Validation experiments to simulate:
Required decisive validation assays: conditional knockout / mass spectrometry / SPR-BLI-ITC / rescue / phenotype readout / other
Groups:
Replicates:
Expected direction:
Required tables:
Required figure summaries:
Constraints:
Output format:
Source-status requirement: record virtual status in the report or source ledger; do not repeat labels in every table, figure caption, or result paragraph unless requested.
Rationale requirement: save a separate rationale file explaining the literature search, public-data feasibility check, novelty scan, closest prior work, selected plausible-and-innovative positive result axis, why it is not a direct repeat, and remaining uncertainty.
```

## Decision Rules

Pre-register support levels:

- Strong support: sample-level or perturbation evidence matches prediction and controls major confounders.
- Moderate support: same direction across multiple datasets but no perturbation evidence.
- Weak support: cell-level-only association or indirect enrichment.
- Neutral: inconsistent or underpowered result.
- Contradictory: decisive readout moves opposite to prediction.
- Not interpretable: missing metadata, failed QC, or inappropriate unit of replication.
