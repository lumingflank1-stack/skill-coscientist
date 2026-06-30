# Raw Data and Virtual Excel Guide

## Raw-Data Requirement Identification

For every panel and claim, classify whether raw data are required:

| Panel or claim type | Needs raw numeric/image data? | Required real source |
|---|---:|---|
| Mechanistic schematic | No numeric raw data | Literature, domain annotation, structural rationale |
| Representative Western blot, gel, IF, IHC, microscopy | Yes | Uncropped image, lane/ROI map, exposure, acquisition metadata |
| Quantified signal | Yes | Replicate-level values, normalization, background correction |
| Binding kinetics | Yes | Sensorgrams, concentration series, reference subtraction, fit output |
| qPCR/ELISA/flow | Yes | Ct/standard curve/MFI/count data, gating, normalization |
| Sequencing/omics | Yes | Count matrix, metadata, QC, model outputs |
| Animal behavior/clinical score | Yes | Subject-level measurements, inclusion/exclusion, randomization/blinding |

## Required Workbook Sheets

A full simulated workbook is allowed only when the user explicitly requests simulated, mock, virtual, or positive expected results. It should include:

1. `README`: purpose, linked manuscript/figure paths, and a pointer to the Markdown report source ledger.
2. `RawData_Needs`: panel-level raw data requirements.
3. Assay-specific raw data sheets, such as `CoIP_Densitometry`, `SPR_Sensorgrams`, or `qPCR_Ct`.
4. Assay-specific summary sheets for plotting.
5. `Figure_Data_Map`: figure panel to workbook sheet/columns.
6. `Stat_Plan`: unit of analysis, recommended test/model, required real data.
7. Optional `Quick_Plots`: simple Excel charts when useful.

## Simulated Data Rules

Use simulated data only when explicitly requested, and only for:

- manuscript logic rehearsal;
- figure layout prototyping;
- table schema design;
- future real-data entry templates.

Every simulated workbook must:

- avoid repeated simulated-status labels inside data tables, figure maps, or figure legends;
- rely on the accompanying Markdown report and `result_source_ledger.md` for source-mode disclosure;
- link to `virtual_result_rationale.md` or `assumed_result_explanation.md`, which explains the literature/public-data basis for choosing the most plausible positive result axis;
- use four decimal places for numeric outputs unless the user asks otherwise;
- preserve reasonable within-group variance;
- avoid impossible values, such as negative concentrations or negative normalized intensities;
- avoid exact duplicate replicate values.

Do not create simulated values just because expected directions are described. If the prompt is ambiguous, produce `RawData_Needs` and a requirements-only workbook or Markdown summary instead. If simulated values are generated, document that status in the Markdown report rather than repeating it in every table.

## Variance Guidance

Choose variance based on assay type:

| Assay | Typical simulated variance |
|---|---|
| Western blot densitometry | CV 8-20% for positive groups, low but nonzero background for controls |
| ELISA/qPCR relative abundance | CV 5-15% for technical summaries, 10-30% for biological variation |
| SPR sensorgram noise | low RU noise plus concentration-dependent variation |
| Cell counts/proportions | binomial-like variance, bounded 0-1 for fractions |
| Omics summaries | donor-level or sample-level variance, avoid cell-level pseudoreplication |

## Excel Generation Script

Use `scripts/write_virtual_workbook.py` to write `.xlsx` from a JSON workbook spec.

Minimal JSON shape:

```json
{
  "workbook_title": "Example simulated result workbook",
  "decimal_places": 4,
  "sheets": [
    {
      "name": "RawData_Needs",
      "columns": ["Figure_panel", "Claim", "Needs_raw_data", "Required_real_data"],
      "rows": [
        ["Figure 1A", "Mechanistic model", "No", "Literature and domain rationale"]
      ]
    }
  ],
  "variance_checks": [
    {
      "sheet": "CoIP_Densitometry",
      "group_by": ["species", "condition", "IP_condition"],
      "value_column": "normalized_signal",
      "min_sd": 0.0200
    }
  ]
}
```

Run:

```bash
python co-result/scripts/write_virtual_workbook.py --input workbook_spec.json --output result_virtual_raw_data.xlsx --decimals 4
```

The script rounds numeric values to four decimals and, for groups with insufficient variance, adds deterministic centered jitter to simulated values before writing.
