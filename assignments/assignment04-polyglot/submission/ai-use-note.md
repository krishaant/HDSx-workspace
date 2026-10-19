# AI-Use Note

## Audit trail
# AI prompt: R dplyr summary of BMI by IncomeGroup and Gender, refactored into summarise_mean_sd()
# Verified: all.equal() shows the function reproduces the Part A pipeline; column names checked in names(nhanes)
# AI prompt: translate the R summary to pandas one step at a time, with a reusable helper in helpers.py
# Verified: raw rows (105626), columns (18), filtered rows (87647), 6 group labels, and every n/mean/SD match R after rounding
# AI prompt: build a parity table comparing R and Python outputs
# Verified: group_check joins on both labels with full_join, so a missing or renamed group would show as NA

## What AI helped with
Claude (Anthropic) drafted the R pipeline and function, the pandas translation in
translation.ipynb, the helpers.py functions, and the code that builds parity-table.csv.
It also explained the R-to-pandas equivalents for each step.

## What I changed
I had already written my own first version of the R summary (read_csv, filter on
the three variables, group_by(IncomeGroup, Gender), summarise with n and
mean_bmi) and I kept that structure. The drafted version added the missingness
counts, the function refactor, the Waist and Race reuse checks, and the parity
code on top of it rather than replacing my approach.

## How I verified the result
I ran the notebook from the submission
folder and rendered the Quarto file, then confirmed every row of the parity table
says TRUE. I checked that pandas `std()` and R `sd()` both use n - 1, that both
languages drop rows missing BMI, IncomeGroup, or Gender, and that the notebook
cell comparing the helper with the step-by-step pipeline prints True. I kept the
interpretation descriptive and unweighted.
