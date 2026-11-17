# Table 1 Audit Note

Audit of `planted-error-starter.qmd`. The corrected version is `eda-note.qmd`.

## Cohort

- We want people aged 20 to 80, including people who are exactly 20 or exactly 80
- The starter code uses Age > 20 and Age < 80, which leaves out anyone who is exactly 20 or exactly 80.
- The fix is to `filter(Age >= 20, Age <= 80)`
- My report checks that minimum age is 20 and the maximum is 80.

## Missingness

Before making any tables, I checked how much data was missing for people aged 20 to 80. I checked `BMI`, `Age`, `IncomeGroup`, `PIR`, `Gender`, `Race`, and `Cycle`. Income (`IncomeGroup` and `PIR`) is missing for 5,395 people (9.4%), and BMI is missing for 1,009 people (1.8%). Age, gender, race, and cycle have no missing values. The starter file never checked for missing data.

## Planted Issues

| # | Issue | Category | Why it matters | Corrected approach |
|---|---|---|---|---|
| 1 | Age filter uses `Age > 20, Age < 80`, but the text says 20-80 inclusive | Correctness | Code and documented cohort disagree; people aged exactly 20 and 80 are silently excluded, so N and the means describe a different cohort than the one reported | `filter(Age >= 20, Age <= 80)`, then check `min(Age)` and `max(Age)` in the output |
| 2 | Table 1 reports `var()` labelled as "(SD)" for BMI and age | Correctness | Variance is SD squared (BMI SD ~7 shows up as ~49), so every spread value in the table is wrong and in the wrong units | Use `sd(x, na.rm = TRUE)` inside a `mean_sd()` helper |
| 3 | `na.omit()` on the whole data frame drops any row missing any of 18 columns (including unused ones like `Marital`, `Waist`) | Correctness | Removes about a quarter of the cohort (57,137 to 43,502 rows) for reasons unrelated to the table, and the exclusion is never documented or counted | Only exclude on variables the table uses (`IncomeGroup`), handle BMI with `na.rm = TRUE`, and show counts at each step in a cohort-flow table |
| 4 | Missingness is never checked or reported before summarizing | Reproducibility | A reader cannot see how many records were lost or whether missing income is concentrated in certain groups, so the analysis cannot be audited or repeated with the same decisions | Add a missingness table (n and %) for key variables on the cohort denominator, placed before Table 1 |
| 5 | `candidate_paths` includes an absolute path `C:/Users/analyst/Documents/nhanes_equity_v6.csv` | Reproducibility | Only works on one person's Windows machine, leaks a local username, and if that file existed it would be picked first and silently use a different copy of the data | Keep only repository-relative paths |
| 6 | "Statistically significant ... shows that income determines BMI" | Interpretation | No test was run, the data are unweighted and unadjusted, and a cross-sectional descriptive table cannot support a causal claim | Describe differences as descriptive only and state that no causal or population inference is made |
| 7 | "Complete and publication-ready" because missing rows were removed | Interpretation | Dropping missing rows does not make results complete; it can bias them if missingness is related to income or BMI. Unweighted NHANES summaries are not population estimates | State the missingness handling and its limitation; say results describe the classroom dataset only |
| 8 | Comment says "Data downloaded fresh from the NHANES website last week" | Stewardship | False provenance: the file is a prepared, cached classroom snapshot (`nhanes_equity_v6.csv`) derived from CDC public-use files, not a fresh download. Wrong provenance breaks traceability and misleads reuse | Name the actual source: prepared classroom snapshot in `examples/nhanes-equity/data/`, derived from CDC NHANES public-use files, for classroom use |

Categories covered: correctness (1, 2, 3), reproducibility (4, 5), interpretation (6, 7), stewardship (8).

## AI-Use Check

AI helped organize this table and suggest wording for "why it matters". I found and confirmed each issue by reading the starter code and checking against the data: I re-ran the age filter both ways to get the row counts above, compared `var(BMI)` with `sd(BMI)` to confirm the units error, and counted rows before and after `na.omit()`. See `ai-use-note.md`.
