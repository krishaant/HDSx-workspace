"""Reusable helpers for the Assignment 4 Python/pandas translation.

Called from translation.ipynb. Each function mirrors one piece of the R code in
polyglot-parity.qmd so the two languages can be compared step by step.
"""

from pathlib import Path

import pandas as pd


def find_repo_root(start=None):
    """Walk up from `start` (default: current folder) until _quarto.yml is found.

    Jupyter usually starts inside the submission folder, while a terminal may
    start at the repository root. Looking for _quarto.yml gives the same
    relative data path in both cases, with no machine-specific paths.
    """
    here = Path(start or Path.cwd()).resolve()
    for folder in [here, *here.parents]:
        if (folder / "_quarto.yml").exists():
            return folder
    raise FileNotFoundError("Could not find the repository root (_quarto.yml).")


def summarise_mean_sd(data, value, group1, group2, digits=2):
    """Python twin of the R function summarise_mean_sd().

    R step                                  pandas step
    filter(!is.na(value), !is.na(groups))   dropna(subset=[...])
    group_by(group1, group2)                groupby([...])
    summarise(n, mean, sd)                  agg(size, mean, std)
    arrange(group1, group2)                 sort_values([...])
    """
    summary = (
        data
        .dropna(subset=[value, group1, group2])
        .groupby([group1, group2], as_index=False)
        .agg(
            n=(value, "size"),
            mean_value=(value, "mean"),
            # pandas std() divides by n - 1 by default, the same as R's sd()
            sd_value=(value, "std"),
        )
        .sort_values([group1, group2])
        .reset_index(drop=True)
    )
    summary["mean_value"] = summary["mean_value"].round(digits)
    summary["sd_value"] = summary["sd_value"].round(digits)
    return summary
