# Software and R Package Citation Guide

Use this guide whenever a Methods section mentions R packages, Python packages, command-line tools, databases, web servers, pipelines, or commercial software.

## Core Rule

Every software or R package used for analysis must include:

1. Name.
2. Version.
3. Developer, project, company, or maintainer group.
4. Country when meaningful.
5. Purpose in the analysis.
6. Numbered citation to the relevant method paper, package citation record, manual, or official release page.

In Methods prose, write software as:

`Data were processed using Seurat (vX.X.X; Satija Lab, USA) [1].`

For multiple tools in one sentence:

`Differential expression was performed using edgeR (vX.X.X; Bioconductor, USA) [2] and visualized with ggplot2 (vX.X.X; Posit, USA) [3].`

## Citation Source Priority

Use sources in this order:

1. R `citation("package")` output or `citation()` for base R.
2. Bioconductor package citation page.
3. CRAN package citation page or package `CITATION` file.
4. Official method paper, software paper, or database paper.
5. Official software manual, release notes, or documentation page.
6. Official repository release or DOI record, such as Zenodo.

Do not cite random tutorials, blogs, package mirrors, or user forum posts as software references.

## Numbered Citation Format

Use numbered citations in the Methods text:

- Preferred: `Seurat (vX.X.X; Satija Lab, USA) [1]`
- Also acceptable when required by journal style: `Seurat vX.X.X [1]`

Then provide a numbered reference list under `Software references` or merge the entries into the manuscript's main numbered reference list:

```markdown
## Software references

[1] Author(s). Title. Journal/Publisher year; volume: pages. DOI/URL.
[2] Author(s). Title. Journal/Publisher year; volume: pages. DOI/URL.
```

Do not reuse one number for unrelated tools. Reuse the same number only when the same software citation appears multiple times.

## R-Specific Procedure

When local R is available, retrieve package citations with:

```r
citation()
citation("Seurat")
citation("DESeq2")
citation("edgeR")
packageVersion("Seurat")
sessionInfo()
```

If local R or the package is unavailable, search official CRAN/Bioconductor pages and select a current reproducible version when reasonable. Use `requires author verification` only when the actual analysis environment must be matched exactly.

## Open-Source Developer and Country Rules

For open-source software, use the project, foundation, lab, or maintainer organization as the developer:

- R: `R Foundation for Statistical Computing, Austria`
- Bioconductor packages: `Bioconductor project, USA` unless the package citation clearly identifies a specific institutional developer.
- Seurat: `Satija Lab, USA`
- Scanpy/anndata: use the package citation or maintainer organization from the official documentation.
- ggplot2 and tidyverse packages: `Posit/PBC or package authors, USA` only when supported by the official citation; otherwise use the package citation authors and mark company/country as `not applicable`.

If country is not meaningful for a distributed open-source project, write `not applicable` rather than guessing.

## No-Citation Cases

If no peer-reviewed citation exists:

1. Cite the official manual, documentation, release notes, or repository DOI as a numbered reference.
2. Mark citation type as `manual/documentation` in the software index.
3. Add the item to the high-risk author-verification ledger only if the journal requires peer-reviewed software citations.

## Software Index Columns

Use this table:

| Software/package | Version | Company/developer | Country | Purpose | Parameters/tests | Citation no. | Citation source | Status |
|---|---|---|---|---|---|---|---|---|

Status values:

- `verified`: version and citation are confirmed from user files or official sources.
- `version requires author verification`: citation is known but the exact user-run version must be matched.
- `citation requires author verification`: version is known but the citation has not been verified from an official source.
- `manual citation`: no method paper found; official manual/release is cited.
