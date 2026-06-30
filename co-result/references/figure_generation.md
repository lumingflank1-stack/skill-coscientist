# Figure Generation Guide

## When to Use

Use this guide when the user asks to call ChatGPT image generation, produce `Figure 1`-style complete figure montages, or write prompts for figure images.

## Execution

Use the `imagegen` skill and the built-in ChatGPT image generation path by default. Generate one complete bitmap per independent figure:

- `figures/Figure_1_<short_topic>.png`
- `figures/Figure_2_<short_topic>.png`

Do not leave project-referenced images only in the default generated-images directory. Copy final selected images into the project workspace.

## Prompt Structure

Use a structured prompt:

```text
Use case: scientific-educational
Asset type: biomedical manuscript Figure <N> complete multi-panel figure montage
Primary request: <one sentence summary>
Panel A: <schematic/result>
Panel B: <representative image/blot/flow/cell image>
Panel C: <quantification/plot>
Panel D: <orthogonal assay/integrative model>
Composition/framing: landscape figure, panel labels A-D, aligned grid, white background
Style/medium: clean biomedical vector-like illustration rendered as bitmap
Color palette: restrained, colorblind-aware, white background
Text constraints: short exact labels only
Avoid: clutter, invented logos, excessive text, exact unsupported statistics, dark background
```

## Panel Design

Use panel types that match evidence:

- Mechanism or workflow: schematic.
- Western blot or gel: representative schematic blot with lane labels.
- Quantification: bar, dot, box, violin, line, forest, or dose-response plot.
- Binding assay: sensorgram and equilibrium fit.
- Single-cell or omics: UMAP, heatmap, dot plot, volcano, pathway map, cell-cell axis.
- Animal/clinical endpoint: timeline, representative image, quantitative plot, survival or score plot.

## Text Accuracy

Keep in-image labels short. Generated image models may misspell long text. Put detailed explanation in the legend, not inside the figure.

Do not include exact p values, sample sizes, Kd, fold changes, or clinical numbers unless the user provided them or the prompt explicitly requested virtual numeric values. Use visual placeholders when planning:

- `Kd in nanomolar range`
- `normalized signal`
- `relative expression`
- `response (RU)`

## Inspection

After generation, inspect the image:

1. The image is nonblank.
2. All panels are present.
3. Panel labels match the manuscript.
4. Key labels are legible and not badly misspelled.
5. The visual claim does not exceed the text claim.

If text is inaccurate but structure is useful, keep the raw image as a planning figure and note that final production figures should be redrawn with real data.
