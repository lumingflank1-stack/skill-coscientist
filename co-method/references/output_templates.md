# Output Templates and Reusable Prompts

Use these templates when generating a complete Methods draft or when the user asks for a prompt.

## Default Concise Chinese Output

Use this as the default unless the user asks for a full audit, full tables, or English output:

```markdown
## 材料与方法

### 数据来源与研究设计

### 数据预处理与质量控制

### 实验/分析流程

### 统计分析

### 数据与代码可用性

## 软件参考文献

[1] ...

## 高风险需作者核对

- ...
```

Keep the Methods正文 compact. Prefer 4-7 short subsections and avoid large tables in the default response. Use searched Chinese-priority reagents directly in the prose. Use unresolved notes only for details that cannot be ethically or scientifically inferred, such as ethics approvals, actual sample numbers, lot numbers, patient demographics, animal protocol numbers, or exact instrument models already used by the lab.

## Alignment Note

```markdown
研究类型：
目标期刊/格式：
使用的输入：
是否联网核对：
主要假设：
```

Keep this note short. Do not delay drafting unless a missing detail changes the study design or could make the Methods misleading.

## Result-to-Method Map

```markdown
| Result/claim | Method needed | Sample/model | Key materials | Instrument/software | Statistical support | Status |
|---|---|---|---|---|---|---|
```

Status values: `verified`, `searched implementation`, `inferred`, `not reported`, `requires author verification`.

## Methods Draft Skeleton

```markdown
## Methods

### Study design

### Ethics approval and consent

### Participants, samples, animals, or cell models

### Randomization, blinding, and sample-size rationale

### Reagents and resources

### Experimental procedures

### Sequencing, imaging, cytometry, or platform acquisition

### Bioinformatics and data processing

### Statistical analysis

### Data, code, and material availability
```

Delete irrelevant headings only after confirming the study does not need them.

## Specific Materials Index

```markdown
| Category | Item as written in Methods | Cat./ID | Company | Country | Specific details | Source | Confidence |
|---|---|---|---|---|---|---|---|
```

Categories: antibody, primer, shRNA/siRNA/sgRNA, kit, chemical, cytokine, inhibitor, plasmid, cell line, animal strain, medium, sequencing reagent, other.

## Sequence Index

```markdown
| Target | Reagent type | Species | Sequence 5'->3' | Vector/modification | Source/design method | Company | Country | Status |
|---|---|---|---|---|---|---|---|---|
```

Use for primers, shRNA, siRNA, ASO, sgRNA, probes, barcodes, or genotyping primers.

## Instrument Index

```markdown
| Instrument/use | Model | Company | Country | Key settings | Result supported |
|---|---|---|---|---|---|
```

In prose, write:

`Images were acquired using a [model] microscope ([Company], [Country]) with [objective/settings].`

## Software and Statistics Index

```markdown
| Software/package | Version | Company/developer | Country | Purpose | Parameters/tests | Citation no. | Citation source | Status |
|---|---|---|---|---|---|---|---|---|
```

In prose, write:

`Differential expression was performed using DESeq2 (vX.X.X; Bioconductor, USA) [1] with [design formula], and P values were adjusted by the Benjamini-Hochberg method.`

For R packages and other software, cite the relevant method paper, package `citation()` record, official manual, or release DOI with numbered citations. For open-source tools, use the project foundation, primary developer group, or institution as the developer when the company field is meaningful; otherwise write `not applicable` rather than guessing.

## Software References

```markdown
## Software references

[1] Author(s). Title. Journal/Publisher year; volume: pages. DOI/URL.
[2] Author(s). Title. Journal/Publisher year; volume: pages. DOI/URL.
```

Use this section whenever software or R packages appear in the Methods. The numbered references may be merged into the manuscript's main reference list if the journal requires one continuous bibliography.

## High-Risk Author-Verification Ledger

```markdown
| High-risk item | Why it matters | Best source to verify | Draft choice | Risk if unchecked |
|---|---|---|---|---|
```

Risk values: `low`, `medium`, `high`.

High-risk author-verification details include: ethics approval, exact participant criteria, animal sex/age/strain, lot numbers, the lab's actual instrument model, proprietary sequences, replicate unit, randomization/blinding, and whether a searched reagent exactly matches the reagent already purchased by the authors. Antibody clone/catalog, primer sequence, shRNA/siRNA sequence, sequencing platform, reference genome, and statistical test should be actively searched or designed first and moved here only when the information is truly not inferable.

## Concise Chinese Prompt Template

```text
Use $co-method.

Task: 根据下面的摘要和结果，用中文精简撰写论文“材料与方法”部分。

要求：
1. 默认只输出精简 Methods 正文、软件参考文献和“高风险需作者核对”。
2. 若涉及抗体、引物、shRNA/siRNA/sgRNA、试剂盒、仪器、细胞系或软件，必须联网核对关键细节并尽量补全。
3. 试剂格式：(货号；公司，国家；关键细节)。
4. 仪器格式：(型号；公司，国家)。
5. R 包或软件格式：(版本；公司/开发者，国家) [编号引用]。
6. R 包或软件必须用 [1]、[2] 形式引用方法论文、package citation、官方 manual 或 release。
7. 优先从中国官方供应商补全：抗体优先武汉三鹰/Proteintech；qPCR 引物优先上海生工生物；细胞系优先中科院上海细胞库；常规试剂/试剂盒优先正能生物、碧云天、赛维尔、天根、诺唯赞、生工等。
8. 没有现成 qPCR 引物或 siRNA/shRNA 序列时，基于公开参考序列设计候选序列，并标注为“设计候选序列”；不要空着。
9. 只有伦理编号、真实样本数、批号、真实病人信息、动物伦理编号、实验室实际仪器型号等无法推断内容，才放入“高风险需作者核对”。

摘要：
[粘贴摘要]

结果：
[粘贴结果、图注或 panel-level findings]

已知材料/流程：
[粘贴已有试剂、流程、软件版本或补充方法]
```

## Full Prompt Template

```text
Use $co-method.

Task: Write a complete Methods section from the abstract and results below.

Target journal/style:
Language:
Study type:

Requirements:
1. Build a result-to-method map before drafting.
2. Search the internet for exact reagent, antibody, primer, shRNA/siRNA/sgRNA, instrument, and software details when missing.
3. Search Chinese official supplier/manufacturer pages first, then global official sources if Chinese pages lack the required detail.
4. Put item metadata immediately after each item in parentheses:
   - Reagent: (Cat. no.; Company, Country; key details)
   - Primer: (forward 5'-...-3', reverse 5'-...-3'; amplicon; Company, Country)
   - shRNA/siRNA/sgRNA: (target/guide sequence 5'-...-3'; vector/modification; Company, Country)
   - Instrument: (model; Company, Country)
   - Software/R package: (version; Company/Developer, Country) [numbered citation]
5. For R packages and other software, use numbered citations to the relevant method papers, package citation records, manuals, or official release pages.
6. Do not fabricate unverified details. Fill gaps through Chinese-priority web search and clearly label searched/designed candidate materials when the exact purchased item was not user-provided.
7. Follow medical manuscript Methods format and Nature-style reproducibility logic.

Abstract:
[paste abstract]

Results:
[paste results, figure legends, or panel-level findings]

Known materials/protocols:
[paste any known reagents, assays, protocols, supplementary details]

Output:
- Alignment note
- Result-to-method map
- Full Methods section
- Specific materials and sequence index
- Instrument index
- Software/statistics index
- Numbered software references
- Search evidence ledger with URLs
- High-risk author-verification ledger
```
