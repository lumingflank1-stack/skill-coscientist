# Bioinformatics Analysis Patterns

Use this reference when the user wants data analysis, an executable bioinformatics plan, single-cell or bulk omics interpretation, or analysis-driven hypothesis revision.

## Before Coding

Inventory the workspace:

- File paths, formats, and object types
- Sample, donor, group, disease, treatment, batch, time point, sex, age, and tissue metadata
- Unit of replication: cell, sample, donor, animal, patient, organoid, batch
- Expected comparisons and covariates
- Existing scripts and output conventions

Do not overwrite user files. Write outputs to a new descriptive directory and keep intermediate objects when analyses are expensive.

## Analysis Plan Template

```markdown
### Analysis Objective

### Input Data

### Required Metadata

### Preprocessing and QC

### Main Model or Comparison

### Covariates and Confounders

### Decision Rules

### Expected Tables

### Expected Figures

### Failure Modes
```

## Single-Cell RNA-Seq

Default checks:

- Confirm cell type and subtype annotation.
- Check sample and donor contribution per cluster or state.
- Check doublets, ambient RNA, mitochondrial fraction, ribosomal fraction, and library size.
- Prefer donor-level pseudobulk for differential expression where replication exists.
- For module scores, compare at donor/sample level as well as cell level.
- For co-expression, report donor-level or pseudobulk association when possible.
- Use partial correlation or regression to control broad activation modules such as IFN, stress, cell cycle, and inflammation.
- Treat ligand-receptor, GRN, regulon, and trajectory outputs as hypotheses unless externally supported.

Useful R packages: Seurat, SingleCellExperiment, scater, scran, muscat, edgeR, DESeq2, limma, presto, fgsea, clusterProfiler, ComplexHeatmap, ggplot2, patchwork.

Useful Python packages: scanpy, anndata, pandas, numpy, scipy, statsmodels, decoupler, gseapy, seaborn, matplotlib, pertpy when available.

## Bulk RNA-Seq or Pseudobulk

Use a sample-level model:

- DESeq2, edgeR, or limma-voom for counts.
- Include covariates when metadata support them.
- Avoid using cell count as biological replication.
- Report effect size, confidence interval or standard error, adjusted p value, and sample counts.
- Use pathway enrichment as a secondary interpretation layer, not as primary proof.

## Mechanism-Specific Tests

Map each hypothesis to at least one decisive analysis:

- Upstream trigger: receptor/pathway module, ligand availability, microbial/metabolite proxy, stimulation signature.
- Candidate mediator: expression, protein proxy when available, regulon or target module, perturbation signature.
- Downstream program: pathway module, target genes, cytokines, antigen presentation, metabolism, migration, survival, or fibrosis.
- Specificity: compare across cell types, disease states, treatment states, and activation modules.
- External validation: public datasets, independent cohorts, perturbation datasets, or known gene signatures.

## Decision Rules

Before running analysis, define how each result will be interpreted.

Examples:

- Strong support: donor-level association persists after controlling confounders and aligns with external perturbation data.
- Moderate support: same direction in multiple analyses but no perturbation evidence.
- Weak support: cell-level-only association or pathway enrichment without replication.
- Neutral: effect direction inconsistent or underpowered.
- Contradictory: decisive readout moves opposite to prediction.

When results are contradictory, revise the hypothesis instead of forcing a positive narrative.
