# Documentation Change

File changed: `README.md` (repository root)
Section: "Getting started", new subsection added after step 5

## Before

The Getting started section ended at step 5:

> 5. Make the Assignment 1 edits, render again, then commit both
>    `practice_report.qmd` and `practice_report.html` and sync your work.

There was no statement about working outside a Codespace, even though the
milestone guidance allows "GitHub Codespaces or a documented local setup".

## After

A new subsection was added after step 5:

> ### Running locally instead of in a Codespace
>
> The Codespace is the course dependency baseline, but this workspace also
> renders locally if you have R, Quarto, and Python installed. Use the same
> render step as in the Codespace:
>
> ```
> quarto render practice_report.qmd
> ```
>
> Run everything from the repository root so relative paths such as
> `examples/nhanes-equity/data/nhanes_equity_v6.csv` and
> `assignments/assignment04-polyglot/submission/output/python-summary.csv`
> keep resolving correctly. Before a deadline, it is still worth opening a
> fresh Codespace once to confirm the project renders there too.

See the diff on branch `docs/git-audit-note`, commit `765c952`.

## Why

I work locally on macOS rather than in a Codespace. The README only described
the Codespace path, so the local route and its one real requirement (render
from the repository root so relative paths resolve) were undocumented for
anyone reading this repository.
