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

## Decisive Experiment

- Model:
- Samples:
- Perturbation:
- Rescue:
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
