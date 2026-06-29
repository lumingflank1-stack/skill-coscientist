# Biomedical Co-Scientist Skill / 生物医学 Co-Scientist 技能

## Overview / 概览

**English:** `biomedical-co-scientist` is a Codex skill for biomedical research reasoning. It helps Codex generate competing mechanistic hypotheses, critique them, rank them, design bioinformatics analyses, interpret results conservatively, revise hypotheses, and propose wet-lab and translational validation plans.

**中文：** `biomedical-co-scientist` 是一个用于生物医学科研推理的 Codex skill。它帮助 Codex 生成竞争性机制假说、审稿式反驳、假说排序、设计生信分析、保守解释结果、迭代修正假说，并进一步提出实验验证和转化研究方案。

## Core Workflow / 核心流程

**English:**

```text
Generate -> Debate -> Rank -> Test -> Analyze -> Revise -> Translate
```

**中文：**

```text
提出假说 -> 反驳假说 -> 排序假说 -> 设计验证 -> 分析数据 -> 修正假说 -> 转化应用
```

## When To Use / 什么时候使用

**English:** Use this skill when you want Codex to:

- Generate biomedical mechanisms from an observation.
- Compare several competing hypotheses instead of giving one answer.
- Critique correlation, confounding, and alternative explanations.
- Design single-cell, bulk RNA-seq, multi-omics, or pathway analyses.
- Interpret analysis results and revise mechanisms.
- Design wet-lab validation, perturbation, rescue, or translational experiments.
- Frame a project as a manuscript, grant, or figure plan.

**中文：** 当你希望 Codex 做下面这些事时使用：

- 根据科研现象提出机制假说。
- 同时比较多个竞争性假说，而不是只给一个结论。
- 主动质疑相关性、混杂因素和替代解释。
- 设计单细胞、bulk RNA-seq、多组学或通路分析。
- 根据分析结果解释证据，并修正机制假说。
- 设计湿实验验证、扰动、rescue 或转化实验。
- 把课题整理成论文、基金或图版逻辑。

## How To Trigger / 如何触发

**English:** In a new Codex conversation, explicitly invoke the skill:

```text
Use $biomedical-co-scientist to generate, critique, rank, and test hypotheses for my biomedical project.
```

**中文：** 在新的 Codex 对话里，可以显式触发：

```text
Use $biomedical-co-scientist 帮我围绕这个生物医学课题提出假说、反驳假说、排序并设计验证分析。
```

You can also describe the task naturally:

也可以自然语言触发：

```text
用 biomedical-co-scientist skill 分析这个现象，并提出可证伪的机制假说和生信验证方案。
```

## Recommended Test Prompt / 推荐测试 Prompt

**English:**

```text
Use $biomedical-co-scientist

Project: FICT1 in simulated inflammatory macrophage activation
Observation: In a toy single-cell dataset, the fictional gene FICT1 is upregulated in stimulated macrophages and positively correlated with MOCK2, ANTIGEN-A, and ANTIGEN-B. A proxy perturbation analysis suggests MOCK2 may be a downstream candidate.
Goal: Generate 5 competing mechanistic hypotheses. For each hypothesis, include evidence, weaknesses, alternative explanations, bioinformatics validation, falsification criteria, wet-lab validation, translational value, and a ranking table.
```

**中文：**

```text
Use $biomedical-co-scientist

Project: FICT1 in simulated inflammatory macrophage activation
Observation: 在一个虚拟单细胞数据集中，虚构基因 FICT1 在刺激后的巨噬细胞中上调，并与 MOCK2、ANTIGEN-A、ANTIGEN-B 正相关；proxy perturbation 分析提示 MOCK2 可能是下游候选。
Goal: 请生成 5 个竞争性机制假说。每个假说都要包含证据、漏洞、替代解释、生信验证、关键证伪标准、实验验证和转化价值，并给出排序表。
```

## Data Analysis Prompt / 数据分析 Prompt

**English:**

```text
Use $biomedical-co-scientist

I have a toy single-cell dataset at /path/to/data.rds. First inspect the data structure, then design and run donor-level pseudobulk, module score, partial correlation, and visualization analyses around the fictional FICT1-MOCK2-macrophage axis. After analysis, revise the original hypotheses based on the results.
```

**中文：**

```text
Use $biomedical-co-scientist

我有一个虚拟单细胞数据在 /path/to/data.rds。请先检查数据结构，然后围绕虚构的 FICT1-MOCK2-巨噬细胞轴设计并执行 donor-level pseudobulk、module score、partial correlation 和可视化分析。分析完成后，根据结果修正原始假说。
```

## Repository Layout / 仓库结构

```text
biomedical-co-scientist/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── hypothesis_framework.md
│   ├── bioinformatics_analysis.md
│   └── iteration_translation.md
└── scripts/
    └── scaffold_report.py
```

**English:**

- `SKILL.md`: Main trigger description and operating workflow.
- `references/hypothesis_framework.md`: Hypothesis cards, evidence tiers, critique, and scoring.
- `references/bioinformatics_analysis.md`: Bioinformatics analysis patterns and decision rules.
- `references/iteration_translation.md`: Result interpretation, hypothesis revision, validation, translation, and manuscript framing.
- `scripts/scaffold_report.py`: Creates a reusable report scaffold for a project.

**中文：**

- `SKILL.md`：主触发描述和工作流程。
- `references/hypothesis_framework.md`：假说卡、证据分层、反驳和评分规则。
- `references/bioinformatics_analysis.md`：生信分析模式和判断标准。
- `references/iteration_translation.md`：结果解释、假说修正、实验验证、转化和论文基金框架。
- `scripts/scaffold_report.py`：为项目生成可复用的报告骨架。

## Report Scaffold Script / 报告骨架脚本

**English:** Create a structured workspace for a new hypothesis project:

```bash
python biomedical-co-scientist/scripts/scaffold_report.py \
  --project "FICT1 macrophage toy project" \
  --out outputs/co_scientist/fict1-macrophage-toy \
  --hypotheses 5
```

**中文：** 为一个新的假说项目生成结构化输出目录：

```bash
python biomedical-co-scientist/scripts/scaffold_report.py \
  --project "FICT1 macrophage toy project" \
  --out outputs/co_scientist/fict1-macrophage-toy \
  --hypotheses 5
```

The script creates:

脚本会生成：

- `hypothesis_cards.md`
- `analysis_plan.md`
- `final_report.md`
- `evidence_ledger.csv`
- `prioritization.csv`

## Installation / 安装

**English:** This repository is designed as a Codex skill folder. To install globally, copy the skill directory into `~/.codex/skills/`:

```bash
cp -R biomedical-co-scientist ~/.codex/skills/biomedical-co-scientist
```

**中文：** 这个仓库是 Codex skill 文件夹。全局安装时，将 skill 目录复制到 `~/.codex/skills/`：

```bash
cp -R biomedical-co-scientist ~/.codex/skills/biomedical-co-scientist
```

## Validation / 验证

**English:** Validate the skill with Codex's skill creator validator:

```bash
UV_CACHE_DIR=/tmp/uv-skill-validate-cache \
uv run --with pyyaml \
python ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py biomedical-co-scientist
```

**中文：** 使用 Codex 的 skill creator validator 验证：

```bash
UV_CACHE_DIR=/tmp/uv-skill-validate-cache \
uv run --with pyyaml \
python ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py biomedical-co-scientist
```

## Scientific Guardrails / 科学约束

**English:**

- Do not treat correlation as causation.
- Always include alternative explanations.
- Always define falsification criteria.
- Separate observation, association, network inference, perturbation evidence, and causal validation.
- Prefer donor-level or sample-level evidence over cell-level-only associations.
- Treat pathway enrichment, GRN, ligand-receptor, proxy knockout, and CMap results as hypothesis-generating unless directly validated.

**中文：**

- 不把相关性当作因果关系。
- 每个假说都必须包含替代解释。
- 每个假说都必须给出证伪标准。
- 区分观察现象、相关性、网络推断、扰动证据和因果验证。
- 优先使用 donor-level 或 sample-level 证据，而不是只依赖 cell-level 相关。
- 通路富集、GRN、配体-受体、proxy KO、CMap 等结果默认作为假说生成证据，除非有直接验证。
