# AI Use Note (Assignment 6)

**Tool used:** 

I used Claude, it helped me rewrite code and md and qmd files to make it look prettier and helped do some data cleaning. I did not paste and row-level data into the AI (so I didn't put NHANES csv in it).

## What AI helped with, and how I verified it (I asked Claude to help me make this table based on the prompts I gave it)

- **Loading the data (`eda-note.qmd`, chunk `load-data`)**
- Prompt: a relative-path loader that works from the repo root or the `submission/` folder.
- Verified: there are no absolute paths in the list; I rendered from `submission/` and the `../../../` path resolved; `stop()` triggers if no path exists.

- **Cohort filter (`eda-note.qmd`, chunk `define-cohort`)**
- Prompt: a dplyr filter for age 20-80 inclusive plus a cohort-flow table.
- Verified: it uses `>=` and `<=`; the rendered output shows min age 20 and max age 80; the flow-table counts subtract correctly (105,626 to 57,137 to 51,742).

- **Missingness table (`eda-note.qmd`, chunk `missingness-table`)**
- Prompt: NA count and percent for key variables.
- Verified: the denominator is the cohort, not the full CSV; I hand-checked BMI (1,009 missing) and IncomeGroup (5,395 missing).

- **Table 1 (`eda-note.qmd`, chunk `table1`)**
- Prompt: Table 1 with N, BMI mean (SD), and age mean (SD) by `IncomeGroup`, written to CSV.
- Verified: it uses `sd()` not `var()`; `stopifnot()` confirms the group Ns sum to the Table 1 set; I cross-checked the means and SDs with a separate pandas calculation; `table1.csv` matches the rendered table.

- **Methods note (`eda-note.qmd`)**
- Prompt: wording for a descriptive, unweighted, non-causal methods paragraph.
- Verified: it names the cohort, the exclusions, and the missingness handling, says "unweighted", and makes no causal or population claim.

- **Audit note (`audit-note.md`)**
- Prompt: organizing the planted issues into the template.
- Verified: I confirmed each issue against the starter code and re-ran the starter's filter and `na.omit()` to get the row counts quoted.



## What I changed or rejected

- AI's first draft of the income-group order used the label "Middle Income (1.3-3.5)", which does not exist in the data (the actual label is "Middle Income"); I corrected it after checking the unique values.
- I kept BMI as available-case (`na.rm = TRUE`) instead of complete-case and added a "BMI non-missing, n" column so the handling is visible.
