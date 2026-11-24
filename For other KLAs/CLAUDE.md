# Curriculum plans site: instructions for Claude

This folder is a faculty's 2027 curriculum plans site, copied from the English faculty's working site. It is plain HTML on GitHub Pages with no framework.

**Use the `curriculum-plans` skill** (in `.claude/skills/`) for any work on plans, codes, documents or the drive. It has the full workflow and the scripts.

## Fill these in on first use
- Subject: _(e.g. Science)_ (also set `KLA.name` in `template.html`)
- Plan code letters: _(e.g. SCI → 09SCI, 09ADVSCI, SCI12, SCI34)_
- GitHub repository and live site URL: _
- Drive `Year Level Folder` path: _
- VC 2.0 content descriptions document: _
- School templates (curriculum map, unit plan, Learning Area Plan): already built into the site; no files needed

## Rules (always)
1. **Never change entered data** you weren't asked to change. Snapshot each plan's `<title>`, `<h1>`, `const DEFAULTS=`, `const SAVED=` and `const PLAN=` lines before an edit, and confirm afterwards that they're unchanged. Say what you checked.
2. **Commit and push after every change.** Change nothing beyond the request.
3. **Design changes go only in `template.html`**, then run `python build.py <every plan>.html`. Never hand-edit one plan's design. All plans must look the same.
4. **The live site is read-only.** People edit their local copies and push. Don't propose live editing.
5. **No placeholders and no generic content.** Write specific learning intentions ("We will…"), three success criteria ("I can…") and a Do Now for every lesson, from the user's sources. Flag drafted content as draft.
6. **Never invent curriculum codes, texts or rubrics.** Codes come from the VC 2.0 content descriptions.
7. **Never delete files or drive folders without asking.**
8. **The site is the source of truth for every Word document.** Fix the data, then regenerate the documents.

## Where things are
- The subject settings, calendar, camps, drive folder names and VCE mapping are at the top of the `template.html` script (`KLA`, `TERMS`, `YEAR_EVENTS`, `CM_FOLDERS`, `VCE_MAP`/`VCE_SD`).
- Plans are `<CODE>.html`. Register a new plan on the `index.html` card, in `overview.html` (`CLASSES`, `LAP_YEARS`), in `CM_FOLDERS`, and in `README.md`.
- To test the pages, serve the folder (`python -m http.server`) and open `localhost:8000`. The overview and homepage need HTTP.
