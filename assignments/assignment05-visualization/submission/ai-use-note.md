# AI-Use Note

## What AI helped with

Claude (Anthropic) drafted `visualization-audit.qmd` end to end: the audit of
`flawed-plot-code.R`, the initial draft plot, the revised/corrected plot
code, and the wording in `visual-audit-note.md`, `caption.md`, and
`m1-link-note.md`.

## What I changed / checked

- Checked every column used (`BMI`, `IncomeGroup`, `Age`, `Cycle`) against
  `names(nhanes)` and the actual values in
  `examples/nhanes-equity/data/nhanes_equity_v6.csv` rather than trusting
  the names Claude used.
- Ran `summary(nhanes$Age)` and confirmed the flawed starter's "Adults age
  20-80" subtitle does not match its code (no `Age` filter exists), which is
  why that mismatch is listed as a correctness issue rather than assumed.
- Recomputed the dropped-row count (6,286) and the analyzed sample size
  (50,851) directly from the data rather than accepting the numbers as
  written, since they appear in the caption as a stated exclusion.
- Rendered `visualization-audit.qmd` with `quarto render` from the
  repository root and inspected the resulting `corrected-plot.png`: fixed a
  `kg/m²` encoding glitch in the y-axis label and a caption that ran off the
  right edge of the plot by switching to a plain-ASCII axis label and
  wrapping the caption text, then re-rendered to confirm both were fixed.
- Removed/rewrote any causal or population-level language ("drives",
  "Americans have higher BMI") before accepting the final title, subtitle,
  and caption, keeping the interpretation descriptive and unweighted.
