# Visual Audit Note

## Plot Question

How does mean BMI differ by household income group across NHANES cycles
(1999-2000 through 2021-2023), among adults aged 20-80?

## Issues Checked

| Issue | Category | Why it matters | Correction |
|---|---|---|---|
| Title "Low income drives rising obesity in American adults" | Interpretation | Claims causation from a cross-sectional, unweighted, descriptive comparison; income was not manipulated and no causal design is used | Rewrote the title descriptively: "Mean BMI by household income group, NHANES 1999-2023", and the caption states the pattern is descriptive and unweighted |
| Subtitle says "Adults age 20-80" but the code never filters `Age` | Correctness | The flawed summary silently includes every age in the file (0-85), so a plot labeled "adults" actually mixes in pediatric BMI, which has a different distribution than adult BMI | Added an explicit `filter(Age >= 20, Age <= 80)` before summarizing, and reported the resulting `n` in the subtitle |
| y-axis limited to `c(24, 28)` (flawed plot) / `c(25, 31)` (my own draft) | Design | Starting the axis well above zero visually exaggerates the gap between income groups and the size of any change over time | Set the y-axis to start at 0 (`scale_y_continuous(limits = c(0, 32))`) in the corrected plot |
| Only the first and last of 11 NHANES cycles are shown, joined by a line, and captioned "climbed steadily across every... cycle" | Aggregation | Two points cannot show a steady trend; the 9 intermediate cycles could rise, fall, or plateau and the plot would look identical | Plotted all 11 cycles so the real year-to-year pattern is visible instead of implied |
| Rows missing `IncomeGroup`/`BMI` are dropped with no count reported (flawed plot and my own first draft) | Correctness | Readers cannot tell how much of the sample was excluded or whether missingness differs by group | Reported the dropped-row count (6,286 adult records) directly in the plot caption |
| My own draft title, "Low income Americans have higher BMI" | Interpretation | Generalizes an unweighted convenience/classroom sample to the whole country; NHANES sample weights (not used here) are what would support a population-level claim | Caption states the figures are "not survey-weighted or population-representative" |

## Final Caption

See [caption.md](caption.md).

## AI-Use Check

See [ai-use-note.md](ai-use-note.md).
