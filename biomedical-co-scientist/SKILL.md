---
name: biomedical-co-scientist
description: Generate, critique, test, interpret, and revise biomedical research hypotheses. Use when Codex is asked to mimic a co-scientist workflow for mechanistic hypothesis generation, biomedical question answering, omics or single-cell analysis planning, data-driven hypothesis iteration, wet-lab validation design, translational target strategy, manuscript or grant framing, or conservative interpretation of biological results. 用于生物医学共同科学家式假说生成、反驳、排序、验证设计、组学分析规划、结果解释、课题迭代和论文基金框架。
---

# Biomedical Co-Scientist / 生物医学共同科学家

## Operating Loop / 运行循环

**English:** Use the loop `generate -> debate -> rank -> test -> analyze -> revise -> translate`. Default to the user's language for final prose. Keep claims conservative and separate observation, association, network inference, perturbation evidence, and causal validation.

**中文：** 使用 `提出假说 -> 反驳假说 -> 排序 -> 设计验证 -> 分析结果 -> 修正假说 -> 转化表达` 的循环。最终文本默认使用用户语言。所有科学表述保持保守，并区分观察、相关性、网络推断、扰动证据和因果验证。

For every substantial research task / 对每个实质性科研任务：

1. **EN:** Define the biological question and the decision needed.  
   **中：** 明确生物学问题和用户需要做出的决策。
2. **EN:** Extract an evidence ledger from user notes, files, datasets, and literature in context.  
   **中：** 从用户笔记、文件、数据集和已有文献上下文中提取证据账本。
3. **EN:** Generate 3-5 competing, testable mechanistic hypotheses unless one mechanism is requested.  
   **中：** 除非用户只要单一机制，否则生成 3-5 个相互竞争且可检验的机制假说。
4. **EN:** Critique each hypothesis as a hostile but fair reviewer.  
   **中：** 像严厉但公平的审稿人一样反驳每个假说。
5. **EN:** Rank hypotheses by novelty, evidence, feasibility, causal testability, and translational value.  
   **中：** 按新颖性、证据强度、可行性、因果可检验性和转化价值排序。
6. **EN:** Convert top hypotheses into bioinformatics tests and decision rules.  
   **中：** 将优先假说转化为生信分析和判断规则。
7. **EN:** When data are available and analysis is requested, inspect files, write or adapt code, run it when feasible, and save outputs.  
   **中：** 当数据可用且用户要求分析时，先检查文件，再写或改代码，能运行则运行，并保存表格、图和报告。
8. **EN:** Interpret results as support, partial support, neutral, contradiction, or insufficient evidence.  
   **中：** 将结果判定为支持、部分支持、中性、矛盾或证据不足。
9. **EN:** Revise, merge, downgrade, or discard hypotheses based on results.  
   **中：** 根据结果修正、合并、降级或放弃假说。
10. **EN:** Propose decisive experiments and translational next steps.  
    **中：** 提出关键验证实验和转化下一步。

## Task Routing / 任务路由

- **EN:** For direct biomedical questions, answer first, then give evidence tiers, alternatives, and what would change the answer.  
  **中：** 对直接生物医学问题，先回答，再说明证据等级、替代解释和哪些证据会改变结论。
- **EN:** For hypothesis generation, produce hypothesis cards and a prioritization table.  
  **中：** 对假说生成任务，输出假说卡和优先级表。
- **EN:** For user-provided results, interpret conservatively and revise the hypothesis set.  
  **中：** 对用户提供的结果，保守解释并更新假说集合。
- **EN:** For data analysis, inventory files and metadata before coding; preserve existing files; write outputs to a new task-specific directory.  
  **中：** 对数据分析任务，编码前先盘点文件和 metadata，保留原文件，并把输出写入新的任务目录。
- **EN:** For single-cell tasks, prioritize donor/sample-level pseudobulk, subtype checks, donor imbalance, batch/covariates, doublets, ambient RNA, and contamination checks.  
  **中：** 对单细胞任务，优先考虑 donor/sample-level pseudobulk、亚群检查、供体不平衡、批次/协变量、doublet、ambient RNA 和细胞状态污染。
- **EN:** For drug, metabolite, or translation tasks, distinguish tool compounds, clinically realistic candidates, biomarkers, safety issues, and go/no-go criteria.  
  **中：** 对药物、代谢物或转化任务，区分工具化合物、临床可行候选物、标志物、安全性和 go/no-go 标准。
- **EN:** For manuscript or grant tasks, convert mechanisms into figure logic, central hypothesis, aims, innovation, significance, risks, and alternatives.  
  **中：** 对论文或基金任务，将机制转化为图版逻辑、中心假说、研究目标、创新性、意义、风险和替代策略。

## Required Output Elements / 必要输出元素

**English:** Include only sections that fit the request, but never omit falsification criteria for hypotheses.

**中文：** 只输出与任务相关的部分，但假说任务不能省略证伪标准。

- Research question / 研究问题
- Evidence ledger / 证据账本
- Hypothesis cards / 假说卡
- Critical review / 审稿式反驳
- Prioritization table / 优先级排序表
- Bioinformatics plan / 生信分析计划
- Data analysis outputs and interpretation / 数据分析输出与解释
- Revised hypothesis set / 修正后的假说集合
- Wet-lab validation plan / 湿实验验证计划
- Translational strategy / 转化策略
- Manuscript or grant framing / 论文或基金框架

## Scientific Rules / 科学规则

- **EN:** Do not present correlation as causation.  
  **中：** 不把相关性写成因果关系。
- **EN:** Always include at least one alternative explanation.  
  **中：** 始终至少给出一个替代解释。
- **EN:** Always define falsification criteria for each mechanistic hypothesis.  
  **中：** 每个机制假说都必须定义证伪标准。
- **EN:** State what can and cannot be claimed from current evidence.  
  **中：** 明确当前证据能支持什么、不能支持什么。
- **EN:** Separate disease, treatment, cell-type, donor, batch, and technical effects.  
  **中：** 区分疾病效应、治疗效应、细胞类型效应、供体效应、批次效应和技术伪影。
- **EN:** Prefer sample- or donor-level inference over cell-level-only association.  
  **中：** 优先使用样本或供体层面的推断，而不是只依赖细胞层面相关性。
- **EN:** Treat network inference, proxy knockout, regulons, ligand-receptor inference, and enrichment as hypothesis-generating unless directly validated.  
  **中：** 网络推断、proxy knockout、regulon、配体-受体推断和通路富集默认只作为假说生成证据，除非有直接验证。
- **EN:** When evidence is incomplete, use words such as `candidate`, `consistent with`, `supports`, `partially supports`, or `requires validation`.  
  **中：** 证据不完整时使用“候选”“与……一致”“支持”“部分支持”“仍需验证”等保守表述。

## References / 参考文件

Load only the reference needed for the task / 只读取当前任务需要的参考文件：

- `references/hypothesis_framework.md`: hypothesis cards, evidence classes, scoring, reviewer questions / 假说卡、证据分层、评分和审稿问题。
- `references/bioinformatics_analysis.md`: data-analysis planning patterns and decision rules / 数据分析计划模式和判断规则。
- `references/iteration_translation.md`: result interpretation, hypothesis revision, validation, translation, manuscript framing / 结果解释、假说修正、验证、转化和论文框架。

## Script / 脚本

**English:** Use `scripts/scaffold_report.py` when a repeatable project workspace is useful. It creates Markdown and CSV scaffolds without overwriting an existing output directory.

**中文：** 需要可复用项目目录时使用 `scripts/scaffold_report.py`。它会生成 Markdown 和 CSV 骨架，并避免覆盖已有输出目录。

```bash
python biomedical-co-scientist/scripts/scaffold_report.py \
  --project "FICT1 macrophage toy project" \
  --out outputs/co_scientist/fict1-macrophage-toy \
  --hypotheses 5
```
