# Medical and Nature-Style Methods Format

Use this guide to convert an abstract and results into a complete biomedical Methods section.

## Reverse Engineering From Abstract and Results

Create this map before drafting:

| Result/claim | Evidence type | Required method subsection | Samples/model | Critical reagents | Instrument/software | Statistics |
|---|---|---|---|---|---|---|

For each result, ask:

1. What biological material was measured?
2. What intervention, exposure, comparison, or perturbation generated the contrast?
3. What assay produced the readout?
4. What instrument or platform captured the data?
5. What preprocessing and quality control happened before analysis?
6. What statistical test supports the claim?
7. What exact material details must be known for another lab to repeat it?

## Recommended Section Order

Adapt the order to the study type, but do not omit required details.

1. Study design and reporting guidelines
2. Ethics approval, consent, and biosafety
3. Participants, samples, animals, cell lines, or disease models
4. Inclusion/exclusion criteria, randomization, blinding, and sample-size rationale
5. Interventions, treatments, exposures, or perturbations
6. Tissue processing, cell culture, sample preparation, and storage
7. Assays and experimental procedures
8. Imaging, flow cytometry, sequencing, omics, or other platform-specific acquisition
9. Bioinformatics and data processing
10. Statistical analysis
11. Data, code, and material availability

For purely mechanistic wet-lab papers, put cell/animal models and assays before omics analysis. For clinical observational studies, put cohort design, endpoint definitions, missing-data handling, and confounder adjustment before assay details.

## Nature-Style Methods Logic

Methods should be reproducible and modular. For each subsection, include:

- Motivation: why this method/module was needed for the result.
- Procedure: exact chronological steps, materials, concentrations, timing, temperature, equipment, and QC.
- Evidence role: which result, endpoint, or panel this method supports.

Use a compact overview at the start only when many modules are involved:

`To test [question], we combined [model/cohort], [assay], and [analysis]. The experimental workflow comprised [module 1], [module 2], and [module 3].`

Avoid making the Methods sound like a second Introduction. The Methods explains how trust and reuse are possible.

## Medical Reporting Requirements

Include study-type details when applicable:

- Human study: recruitment setting, dates, eligibility criteria, consent, ethics committee, diagnosis criteria, treatment status, endpoint definitions, covariates, missing data, and privacy/de-identification.
- Randomized/controlled experiment: allocation sequence, concealment, randomization unit, blinding, replicate definition, exclusion rules, and sample-size basis.
- Animal study: species, strain, sex, age/weight, source, housing, light/dark cycle, diet, acclimatization, humane endpoints, anesthesia/euthanasia, randomization, and blinding.
- Cell study: source, authentication, mycoplasma testing, passage number/range, culture medium, serum, antibiotics, seeding density, transfection/transduction method, multiplicity of infection, selection, and validation.
- Omics study: library kit, platform, read length, depth, reference genome/build, aligner, quantification tool, QC thresholds, normalization, batch correction, differential analysis, multiple-testing correction, deposited accession, and numbered citations for each analysis package or software tool.
- Imaging/flow cytometry: instrument model, acquisition settings, gating/segmentation strategy, negative/positive controls, compensation, exposure, objective, magnification, image-processing software, and blinding.
- Statistical analysis: analysis population, replicate unit, test choice, normality/variance handling, paired/unpaired design, multiple-comparison correction, effect sizes, confidence intervals, p-value threshold, software versions, and numbered citations for R, R packages, Python packages, command-line tools, and commercial software.

## Reporting Guidelines

Name the appropriate reporting guideline when the study type is clear:

- CONSORT for randomized clinical trials.
- STROBE for observational studies.
- ARRIVE for animal experiments.
- PRISMA for systematic reviews/meta-analyses.
- MIAME/MINSEQE or field-specific omics guidance when relevant.

If the user has not provided a completed checklist, say that the Methods was drafted to align with the guideline but the checklist still requires author verification.

## Phrase Replacement Table

| Vague phrase | Replace with |
|---|---|
| according to standard protocols | named protocol, kit, catalog number, critical settings, deviations |
| cells were treated | cell type, density, reagent, dose, solvent, duration, temperature, replicate unit |
| RNA-seq was performed | RNA extraction kit, library kit, platform, read length, depth, aligner, reference, QC |
| images were analyzed | microscope/camera, objective, acquisition settings, segmentation method, software version |
| data were normalized | normalization method, implementation, version, parameters, software citation number |
| statistical significance was assessed | exact test, sidedness, correction, alpha threshold, replicate unit, software version and numbered citation |

## Software Citation Requirement

When a Methods paragraph names R, R packages, Python packages, command-line tools, web tools, databases, or commercial software, cite the relevant method paper or official citation record with numbered references. Use the format `PackageName (vX.X.X; Developer, Country) [n]`.

Prefer package-native citation sources such as R `citation("package")`, CRAN/Bioconductor citation pages, official method papers, official manuals, release notes, or repository DOI records. If a tool has no peer-reviewed citation, cite the official manual or release page as a numbered reference and mark this in the software index.

## Claim Safety

Do not let Methods imply a stronger design than the data support:

- Do not write `randomized` or `blinded` unless the user or protocol says so.
- Do not write `biological replicates` when the input only supports technical replicates.
- Do not write `validated antibody` unless validation source, RRID, or experiment is known.
- Do not write `clinical samples were collected prospectively` unless collection timing is known.
- Do not write `power analysis` unless parameters are known.
