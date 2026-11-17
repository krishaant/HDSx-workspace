# Provenance and Stewardship Note

**Data source.** I used `nhanes_equity_v6.csv`, a classroom version of the National Health and Nutrition Examination Survey (NHANES) covering survey years 1999-2000 to 2021-2023.

**Where it originally came from.** The data comes from public NHANES files released by the U.S. Centers for Disease Control and Prevention (CDC), and the course team cleaned it and added some new columns (like `IncomeGroup`, `EducationClean`, and `WHtR`).

**How I got it.** I loaded the file from the course repository (`examples/nhanes-equity/data/nhanes_equity_v6.csv`) using a relative path; I did not download it from the CDC website.

**What it can be used for.** This data is only for learning in SPPH 381H; my results are unweighted and ignore the survey design, so they do not describe the whole U.S. population and do not show cause and effect.

**Privacy caution.** Even though the data has no names, I did not upload the raw rows to any AI tool, and I will not report very small groups (for example, a rare mix of year, race, age, and income) because that would make it easier to identify someone.