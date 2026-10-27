# Git Audit Note

## Diff summary

Branch: `docs/git-audit-note`, commit `765c952`, two files changed
(`git diff --stat main docs/git-audit-note`: `.gitignore | 3 +++`,
`README.md | 16 ++++++++++++++++`, 2 files changed, 19 insertions(+)).

- `README.md`: added the subsection "Running locally instead of in a Codespace"
  after step 5 of Getting started. Prose and one fenced code line only.
- `.gitignore`: added the pattern `__pycache__/` under a new `# Python` comment.

I read the full diff with `git diff README.md .gitignore` before committing and
confirmed with `git status --short` that no other tracked file was staged. No
`.qmd`, `.R`, `.csv`, or rendered output file appears in the diff, so nothing
that affects an analysis result changed.

## .gitignore check

I ran:

```
git ls-files | grep -E "__pycache__|\.knit\.md|\.DS_Store|_files/"
```

No tracked generated or temporary files were found, so nothing needed to be
removed from version control. I added `__pycache__/` as a preventive pattern,
because importing the Assignment 4 `helpers.py` creates that folder next to the
submission files. I did not add any pattern that would hide source files:
`*.html` and `*.pdf` stay tracked, since the course requires rendered
submission artifacts to be committed.

## AI-use note

I used Claude (Anthropic) to draft the README subsection wording, the pull
request description, and the structure of these evidence files. I ran
`git diff` and `git diff --stat` myself and confirmed the change is limited to
documentation and the one `.gitignore` pattern, and I ran the `git ls-files`
check above before writing its result.

## M0 readiness note

- Group: Canvas "Group Project 2" (SPPH 381, Daniel Chen).
- Members: Krishaant Pathmanathan, Alyssa Jessa, Vuong Hoang Minh Nguyen,
  Paul Ona.
- GitHub usernames: krishaant (Krishaant); remaining usernames to be recorded
  in the M0 `group-formation.md` file in the group repository.
- Repository access: the group repository exists at
  https://github.com/Paulona-lab/SPPH-group-2-project- and is private, created
  from the course project template by Paul Ona. Collaborator invitations and
  the teaching team's access are being confirmed this week.
- Communication plan: the group coordinates through the Canvas group space and
  a group chat, with a weekly check-in after the Tuesday class.
- Codespaces access: I work locally on macOS (R 4.4.3, Quarto, Python via
  Anaconda) and my personal workspace renders locally. A teammate will run the
  Codespace check on the group repository and record the result in the M0
  `codespace-check.md`.
- Project direction: a descriptive NHANES analysis of obesity prevalence by
  income group among adults, with gender as the secondary comparison.
