---
name: curriculum-plans
description: Build and maintain a faculty's 2027 curriculum plans site (copied from the English plans) end to end. Use this whenever the user mentions a year level plan (Year 7 to 12, Mainstream or Advanced, codes like 09SCI or 09ADVSCI), adding or changing CATs, SACs, exams, weekly topics, lessons, learning intentions, success criteria, Do Nows, VC 2.0 curriculum codes, unit plans, curriculum maps, lesson plans, CAT briefs, the Learning Area Plan, the overview page, camps or interruptions, or putting any of these into the faculty's drive folders. Also use it for "make a plan for year X", "do the same for Year 10", or "set this up for our subject", even when the user does not say "skill" or name the files.
---

# Curriculum plans (2027)

This skill covers the whole chain. A plan page on the site gets its curriculum codes, then the site generates the Word documents (curriculum maps, unit plans and the Learning Area Plan). The scripts also make lesson plans and CAT briefs and lay the files out for the drive. **The site is the source of truth.** Every Word document is generated from the plan's own data, so fix the data first and regenerate.

Read the reference files only when you need them:
- `references/site-plan.md`: building or editing a plan page, the data keys, the calendar, the subject settings, and registering a new plan.
- `references/codes.md`: finding and checking VC 2.0 curriculum codes.
- `references/documents.md`: what each generated document contains, and the writing style for lessons.
- `references/drive.md`: the drive folder layout and placing files.

## Locations

- **The site folder:** the folder holding `template.html`, `build.py`, `index.html` and `overview.html`. It's usually the current working directory, and `CLAUDE.md` there names it. `template.html` is the only design source. `build.py` copies the design into each plan. `README.md` is the manual, so keep it current.
- **Scripts in this skill:**
  - `scripts/export_docs.mjs` makes the curriculum maps and unit plans by running the site's own code.
  - `scripts/drive_docs.py` makes the lesson plans and CAT briefs. It needs `pip install python-docx`.
- **The drive root and the school templates:** ask the user the first time, then note them in `CLAUDE.md`.

## Rules that override everything else

1. **Never change entered data.** Before any edit, snapshot the `const SAVED=`, `const DEFAULTS=`, `<title>` and `<h1>` lines of every plan you touch. Afterwards, confirm they are byte-identical, except where the user asked for that exact data to change. Say what you checked.
2. **Always commit and push** after a repo change. Change nothing the user did not ask for.
3. **The live site is read-only.** Visitors cannot type or save. The user edits local copies and pushes. Do not propose live editing.
4. **Never delete files or folders without an explicit go-ahead.** If a delete is blocked, stop, list what needs removing and ask the user. Do not work around the block.
5. **Never invent a curriculum code, a text or a rubric.** Codes come from the VC 2.0 content descriptions for the subject. Any drafted lesson content, achievement standard or adjustment must be flagged as a draft in your reply.
6. **The semester comes from the CAT prefix.** `S1_` is Semester 1 and `S2_` is Semester 2. A unit that spans the break is placed by its CAT.
7. **Step-Up weeks start the next semester.** They are left out of Semester 2 curriculum maps and units.
8. **Exam weeks are never part of a unit.**
9. **No "to be added".** Write specific content from the user's sources (texts, study guides, the faculty's own sites), not generic filler. Ask for sources when you need them.

## First-time setup for a new subject

If `template.html` still says `name:"Subject"` in its `KLA` block, the site has not been set up yet. Before any plan:
1. Ask for the subject name, the plan code letters (e.g. `SCI`, giving `09SCI`, `09ADVSCI`, `SCI12`, `SCI34`), and which classes exist (Mainstream, Advanced, VCE units).
2. Ask for the VC 2.0 content descriptions document for the subject, Levels 7–10. From it, fill `KLA.strandRe` and `KLA.strands` (the strand letters in the codes), `KLA.std` (Levels 9 and 10 achievement standards, quoted from the document), and `KLA.subStrands`.
3. Replace "Subject" and "SUB" in `index.html` and `overview.html` (the title, heading, cards, `CLASSES`, `LAP_YEARS`, and "Curriculum Area: Subject").
4. Check `TERMS` and `YEAR_EVENTS` in `template.html` with the user. They hold the term dates, public holidays, exams, camps and induction.
5. Run `python build.py` on every plan, commit and push.

## Workflow for a plan

Work in this order. Each step checks the one before it.

1. **Gather inputs.** You need the CAT list (title, term and week), the exam weeks, the texts or topics, and source documents for lesson content. If the user gives a previous year's assessment screenshot, map each item to the 2027 week containing the same date, and ask about anything unclear. If the user gives a week, that wins over the date.
2. **Build the plan page.** Copy `template.html` to `<CODE>.html` and set `<title>` and `<h1>` to `<CODE> Curriculum Plan 2027`. Enter the weekly topics and CATs (`S1_<CODE>_CAT1: Title`, `S2_…`, `EXAM…`) and any per-plan settings in `const PLAN={...}`. Year-level camps come from `YEAR_EVENTS` automatically. Run `python build.py <CODE>.html`.
3. **Add curriculum codes.** Every teaching week gets its VC 2.0 codes, and each CAT's details end with `Curriculum codes: …`. Follow `references/codes.md`.
4. **Write lessons.** Every teaching week has its lessons (four, or three plus Ad libitum in holiday weeks; the calendar decides). Each lesson has a learning intention, success criteria and a Do Now, in the style in `references/documents.md`. Mark it as draft in your reply.
5. **Register the plan** in all four places:
   - `index.html`: the class's "Coming soon" card becomes a link (copy an existing link card).
   - `overview.html`: add the code to `CLASSES` and `LAP_YEARS`.
   - `template.html`: add a `CM_FOLDERS` entry naming each unit's drive folder. Check for missing commas, which break the page for every plan. Rebuild all plans afterwards.
   - `README.md`: list the plan.
6. **Verify the site.** Syntax-check the page script and confirm every teaching week has lessons and no grey week carries lessons. Run `node <skill>/scripts/export_docs.mjs <CODE>.html <scratch>`: if it runs, the units and documents build. Push, then check the live page after a minute or two (hard-refresh if it looks old).
7. **Generate the documents into scratch:**
   ```
   node <skill>/scripts/export_docs.mjs <CODE>.html <scratch>
   python <skill>/scripts/drive_docs.py <CODE>.html <scratch>
   ```
   This gives the drive layout: `Semester N/Curriculum Map/`, and per unit `Unit Plan/`, `Lesson Plans/`, `Assessments & Rubrics/` and `Class Resources/`. Fix anything reported as "no CM_FOLDERS entry" before placing.
8. **Place the files on the drive.** Follow `references/drive.md`. Do a dry run first, never overwrite without saying so, and keep existing files.
9. **Report.** Say what changed and what you checked (data identical, files open, links resolve). List what is still draft, and each decision the user needs to confirm, as short questions.

## Known traps

- In file names, `:` becomes ` -`, matching the site's `fileSafe`. Folder names must match `CM_FOLDERS` exactly, because the curriculum map links point at them.
- Design changes go in `template.html` and are rebuilt with `build.py`. Never hand-edit the design of one plan.
- `build.py` needs LF line endings in `template.html`. If it reports `<title>` not found, convert the template to LF.
- `overview.html` and the homepage read the plans over HTTP. Test them with `python -m http.server`, not by opening the file.
- If a Word document won't open, the usual causes are an empty table cell (each needs a paragraph) or a broken hyperlink. Fix it in `template.html`, and the site and the scripts are both fixed.
