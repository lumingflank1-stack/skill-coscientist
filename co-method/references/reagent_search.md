# Reagent and Identifier Search Guide

Use this guide whenever a Methods draft needs exact materials, sequences, catalog numbers, manufacturers, countries, or searchable identifiers.

## Non-Negotiable Rule

Do not invent details. However, do not stop at placeholder language when a credible, citable, commercially available reagent, primer, siRNA/shRNA design, cell line, kit, or software record can be found. If the user has not supplied the exact purchased item, select a searched reagent or designed sequence and draft the method as a reproducible implementation. Use `高风险需作者核对` notes only for details that cannot be ethically or scientifically inferred, such as ethics approval numbers, actual sample sizes, lot numbers, patient demographics, or proprietary sequences.

## Search Priority

1. Search user-provided files first: manuscript draft, abstract, results, figure legends, tables, supplementary methods, protocols, inventory exports, sequencing manifests, ELN notes, grant text.
2. Search Chinese sources first for purchasable equivalents or official pages:
   - Use Chinese and English terms: `基因/靶点 + 抗体 + 货号`, `primer sequence 引物序列 货号`, `shRNA 靶向序列 公司`, `试剂盒 货号 公司`, `仪器 型号 公司 国家`.
   - Prefer official manufacturer or official China distributor pages over marketplaces.
   - Default supplier preferences when no user supplier is provided:
     - Antibodies: 武汉三鹰/Proteintech first, then CST, Abcam, Thermo Fisher, Abclonal, Affinity, or other official pages.
     - qPCR primers and oligonucleotides: 上海生工生物 first; design primers from NCBI/PrimerBank/Primer-BLAST when no validated pair is found.
     - siRNA/shRNA: use official supplier design services/pages when available; otherwise design 2-3 candidate sequences using conservative design rules and label them as searched/designed candidate sequences.
     - Cell lines: 中国科学院分子细胞科学卓越创新中心细胞库/中科院上海细胞库 first, then ATCC or other official cell banks.
     - Co-IP/WB/qPCR kits and routine reagents: Chinese official suppliers such as 正能生物, 碧云天, 赛维尔, 天根, 诺唯赞, 生工, or official China distributors first.
   - If a Chinese source lacks sequence/catalog detail, keep the source as availability evidence only and verify the detail from the original manufacturer.
3. Search global official sources:
   - Manufacturer product pages, datasheets, IFU, SDS, certificates of analysis.
   - Addgene or repository pages for plasmids.
   - RRID/Antibody Registry for antibodies.
   - NCBI, PrimerBank, or supplier design pages for primer or sequence checks.
   - GEO/SRA/ArrayExpress/Zenodo/GitHub only when they are linked to the study or provide exact pipeline/software metadata.
4. Use peer-reviewed papers as secondary context. They may justify a protocol parameter or cite a previously validated sequence, but they do not prove this user's study used that sequence unless the user says so.

## Source Acceptance

Accept as final evidence:

- Official manufacturer/supplier page or datasheet.
- Official distributor page that includes manufacturer identity and catalog number.
- Repository record with stable identifier.
- Article supplementary material containing exact sequence or catalog data.
- User-provided protocol, inventory, or purchase record.

Use cautiously:

- Retail pages, shopping aggregators, and generic reseller entries.
- Protocol-sharing pages without product identifiers.
- Review articles.

Reject as final evidence:

- AI-generated summaries.
- Blogs or forum posts.
- Product lists missing manufacturer or catalog number.
- Any sequence that cannot be traced to a source or design record.

## Item-Specific Requirements

### Antibodies

Capture: target antigen, host species, clonality, clone, conjugate, application, dilution/concentration, catalog number, RRID, company, country, validation note, and source URL.

Format in prose:

`anti-CD68 antibody (Cat. no. XXXX; Company, Country; clone Y; RRID:AB_ZZZ; dilution 1:500)`

If multiple antibodies target the same antigen, choose a reasonable application-matched product rather than leaving the method blank. Prefer products validated for the needed species and application, such as IP for the pull-down antibody and WB for the detection antibody. If an antibody is searched rather than user-provided, phrase the method as a recommended reproducible implementation and keep the source in the evidence ledger.

### Primers

Capture: gene/transcript, organism, assay, forward sequence, reverse sequence, amplicon length, genome/transcript reference, company, country, and source/design method.

Format:

`GAPDH primers (forward 5'-...-3', reverse 5'-...-3'; amplicon 142 bp; Company, Country; source/design method)`

Rules:

- Keep sequences in 5' to 3' orientation.
- Preserve capitalization only if it encodes modified bases; otherwise uppercase is acceptable.
- Do not substitute mouse and human primer sets.
- If the result requires splice isoform specificity, include transcript ID or exon junction if known.
- If no validated primer pair is found, design primers and write them as `designed candidate primers` with the gene, species, transcript reference, amplicon length, and synthesis supplier. Do not leave qPCR primer sequences blank.

### shRNA, siRNA, ASO, sgRNA, and CRISPR Reagents

Capture: target gene, species, exact target or guide sequence, vector/backbone, promoter, selection marker, modification, supplier, catalog or clone ID, company, country, and validation/readout.

Format:

`TP53 shRNA (target sequence 5'-...-3'; vector pLKO.1; Cat. no./clone ID X; Company, Country)`

Rules:

- Distinguish shRNA target sequence from oligonucleotide insert sequence and from mature siRNA guide/passenger strands.
- Distinguish sgRNA spacer sequence from PAM; do not include PAM in the guide unless the source does.
- Include non-targeting control sequence when available.
- If only knockdown is reported and sequence is absent, search supplier or literature sequences first. If none is found, provide 2-3 designed candidate siRNA/shRNA target sequences with species/transcript reference and label them as `designed candidate sequences`. Do not leave the sequence blank unless the sequence is proprietary and cannot be designed from public reference sequence.

### Chemicals, Inhibitors, Cytokines, Kits, and Media

Capture: product name, purity/grade, catalog number, lot if provided, company, country, working concentration, solvent, storage condition, incubation time, and critical deviations from kit instructions.

Format:

`recombinant human IL-6 (Cat. no. X; Company, Country; 20 ng/ml)`

### Cell Lines, Primary Cells, Animals, Microbes, and Plasmids

Capture:

- Cell lines: source, catalog/accession, authentication method, mycoplasma status, passage range, culture medium.
- Primary cells/tissues: donor/source, consent/ethics, processing time, isolation kit/markers.
- Animals: strain, sex, age, weight, source, catalog/stock number, housing, ethics.
- Plasmids: Addgene ID or source, backbone, insert, promoter, tag, resistance, sequence verification.
- Microbes: strain, source, culture conditions, identifier.

## Country Naming

Use the manufacturer's or developer's headquarters country unless the official product page clearly states a different legal manufacturer. For distributor-only pages, cite the distributor country only if no original manufacturer is identifiable, and mark it as distributor evidence.

## Search Ledger Columns

Use this table whenever internet search was performed:

| Item | Required detail | Search query/source | Verified value | Evidence URL/source | Confidence | Remaining issue |
|---|---|---|---|---|---|---|

Confidence:

- High: exact value from official source or user material.
- Medium: exact value from supplementary paper/repository, or official distributor with manufacturer identity.
- Low: plausible but not directly linked to the study; requires author confirmation.
