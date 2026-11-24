# Building and editing a plan page

## The files

- `template.html` is the only design source. It holds the subject settings (`KLA`), the calendar (`TERMS`), the year-level events (`YEAR_EVENTS`), the drive folder names (`CM_FOLDERS`), the VCE mapping (`VCE_MAP`, `VCE_SD`) and all the page code. It holds no plan data.
- `build.py` copies `template.html` into each plan. It keeps the plan's `<title>`, its `<h1>` line, `const DEFAULTS=`, `const SAVED=` and `const PLAN=`. It stops with an error if a kept line is missing or appears twice.
- **Plan files** are named by code (`09SCI.html`). Each is the template plus its own data.
- `index.html` is the homepage. It has its own copy of the term dates (`T=[...]`), which must match `TERMS`.
- `overview.html` is the whole-subject overview. It reads each plan's data and calendar from the plan file (including `YEAR_EVENTS`), so plans must be registered in `CLASSES` and `LAP_YEARS`.

Rebuild after any template change: `python build.py 07SCI.html 08SCI.html 09SCI.html ...` (list every plan).

## Plan codes

`<YY><ADV?><LETTERS>`, e.g. `09SCI` and `09ADVSCI`. VCE plans are `<LETTERS>12` (Units 1–2, Year 11) and `<LETTERS>34` (Units 3–4, Year 12). The page reads the year level, "Advanced" and VCE from the code, so keep this pattern.

## Subject settings: `KLA` in template.html

| Key | What it is |
|---|---|
| `name` | Subject name used in the Word documents ("Science"). |
| `strandRe`, `strands` | A regex whose first group is the strand letters in a VC 2.0 code, and the names of those strands. The unit plan names the strand from the most-used codes. |
| `std` | The Levels 9 and 10 achievement standards, quoted from VC 2.0. These go in the unit plan. |
| `vceRe` | Which plan codes are VCE. |
| `subStrands` | `[regex, sub-strand, focus phrase]` rows. The first rows that match the unit's words name the unit plan's sub-strand. |
| `defaultSubStrand`, `defaultFocus` | Used when no row matches. |

## The calendar: `TERMS` and `YEAR_EVENTS`

Each term has `n`, `start`, `weeks`, `hol` (public holiday weeks: three lessons plus Ad libitum), `grey` (non-teaching weeks with a label), `noLessons`, `exam` and `notes`.

`YEAR_EVENTS` adds school-wide year-level events to every plan of that year: the Year 7 induction and camp, the Year 8 camp, Year 11 HeadStart and the Year 12 finish. It uses the same keys as `PLAN` (below). A plan's own `PLAN` settings win.

A plan changes its calendar with `const PLAN={...}` on its own line:

| Setting | Format | Effect |
|---|---|---|
| `normalWeeks` | `[[term, week], ...]` | Removes grey or exam marking, making it a teaching week. |
| `greyWeeks` | `[[term, week, "Label"], ...]` | Greys a week with no lessons. |
| `notes` | `[[term, week, "Label"], ...]` | Labels a week ("Camp 24-26 Feb"). |
| `lessonCount` | `[[term, week, n], ...]` | Limits a week to `n` lessons. |
| `noUnit` | `[[term, week], ...]` | The week has lessons but belongs to no unit (e.g. exam revision). |
| `assessWord` | `"SAC"` | Says SAC instead of CAT everywhere (VCE). |
| `devBanner` | `[[term, week, "text"], ...]` | Shows a developmental task banner above a week. |

## Data keys

Every value is stored in `const SAVED={...}`:
- `T--W` is the weekly topic: `"1--4"` is Term 1 Week 4. A topic starting `S1_`, `S2_` or `EXAM` becomes an assessment badge and ends a unit. A topic starting `Developmental task` shows as a teal badge.
- `info-T--W` holds the CAT or exam details.
- `codes-T--W` holds the week's curriculum codes, comma-separated.
- `T-W-L-title`, `T-W-L-li`, `T-W-L-sc` and `T-W-L-dn` are a lesson's title, learning intention, success criteria (separated by ` | `) and Do Now. `L` is 1 to 4.

To fill a plan quickly, write the `SAVED` JSON directly (one line, valid JSON), then run `build.py` on the file.

## Checking data did not change

Compare the kept lines before and after against the last commit. For a plan you did not mean to touch, `git diff` should show no change to its `SAVED` line. When you changed data on purpose, show the user that line's diff.
