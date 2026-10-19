# Dependency Note

## R (used in polyglot-parity.qmd)

- tidyverse: readr (`read_csv`, `write_csv`), dplyr (`filter`, `group_by`, `summarise`, `arrange`, `full_join`, `mutate`, `select`), tibble
- knitr: `kable()` for the parity tables

## Python (used in translation.ipynb and helpers.py)

- pandas: reading the CSV, `dropna`, `groupby`, `agg`, `sort_values`
- jupyter: to run the notebook
- pathlib: Python standard library, used to find the repository root (no install needed)

## Environment

- No packages were added beyond the course environment (`.devcontainer/setup.sh` and `.devcontainer/requirements.txt`), so `requirements.txt` was not changed and no second manifest was created.
- `renv` was not used.
- Run order: run `translation.ipynb` first (it writes `output/python-summary.csv` and `output/python-counts.csv`), then render `polyglot-parity.qmd`.
- Rendered locally on macOS with R 4.4.3, Quarto, and Python/pandas from Anaconda, rather than in a Codespace.
