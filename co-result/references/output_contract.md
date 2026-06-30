# Output Contract

## Default Folder Layout

For a full co-result task, create a folder named from the project or figure topic:

```text
<project>_results/
  <project>_results_section.md
  result_source_ledger.md
  virtual_result_rationale.md           # virtual or assumed-positive rationale when applicable
  figure_generation_prompts.md
  figure_generation_blockers.md         # only when image generation is unavailable or blocked
  raw_data_requirements_summary.md
  <project>_virtual_raw_data.xlsx  # only when explicitly requested
  figures/
    Figure_1_<topic>.png
    Figure_2_<topic>.png
  specs/
    workbook_spec.json
```

Use ASCII-safe filenames where possible. Chinese prose can live inside Markdown and Excel.

Markdown reports are Chinese-only by default unless the user requests another language or bilingual output.
除非用户要求其他语言或中英双语，Markdown 报告默认只写中文。

## Markdown Structure

The main Markdown file should contain:

1. Title.
2. Result source note: input, assumed, simulated, or requirements-only.
3. Virtual or assumed-result rationale note, when applicable.
4. `## Results`.
5. Subheaded Results paragraphs with in-text figure panel indexing.
6. Embedded figure image links.
7. `## Figure legends`.
8. Figure generation notes and a single result source note when applicable.

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
- Rationale file path for virtual or assumed-positive results, if applicable.
- Prompt/spec paths, if generated.
- Blocker path if bitmap figures could not be generated.
- The Markdown report path that contains the result source note and source ledger.
