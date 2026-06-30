# Output Contract

## Default Folder Layout

For a full co-result task, create a folder named from the project or figure topic:

```text
<project>_results/
  <project>_results_section.md
  result_source_ledger.md
  figure_generation_prompts.md
  raw_data_requirements_summary.md
  <project>_virtual_raw_data.xlsx  # only when explicitly requested
  figures/
    Figure_1_<topic>.png
    Figure_2_<topic>.png
  specs/
    workbook_spec.json
```

Use ASCII-safe filenames where possible. Chinese prose can live inside Markdown and Excel.

## Markdown Structure

The main Markdown file should contain:

1. Title.
2. Result source note: input, assumed, simulated, or requirements-only.
3. `## Results`.
4. Subheaded Results paragraphs with in-text figure panel indexing.
5. Embedded figure image links.
6. `## Figure legends`.
7. Figure generation notes and a single result source note when applicable.

## Figure Legend Structure

Use this pattern:

```text
**Figure 1 | <one-sentence title>.**
**A,** <panel A description and what it supports.>
**B,** <panel B description.>
**C,** <quantification and statistics boundary.>
**D,** <orthogonal assay or model.>
```

For planning figures, explicitly state that exact values, sample sizes, and statistics should be replaced after real experiments.

## Raw-Data Summary Structure

Include a table:

| Position | Current result or figure content | Needs raw data? | Real data to add |
|---|---|---:|---|

## Final Response

Report:

- Markdown file path.
- Figure image paths.
- Excel file path, if generated.
- Prompt/spec paths, if generated.
- The Markdown report path that contains the result source note and source ledger.
