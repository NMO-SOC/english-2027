# The drive folders

Ask the user for the faculty's `Year Level Folder` path the first time, and record it in `CLAUDE.md`. The school's layout (as Maths and English use):

```
Year 9/
  <Subject> (or "Advanced <Subject>")/
    Semester 1/
      Curriculum Map/          ONE semester curriculum map (.docx)
      Exam/                    exams, if any
      1. Unit name/
        Assessments & Rubrics/  CAT brief, rubric
        Class Resources/        texts, links (.url shortcuts), handouts
        Lesson Plans/           lesson plan document
        Unit Plan/              unit plan document
      2. Unit name/
    Semester 2/
      ...
```

- Units are numbered in teaching order within each semester: `1. Cells`, `2. Forces`.
- Unit folder names are the unit names, never "Unit of Work N". They must match `CM_FOLDERS` in `template.html` exactly, because the curriculum map links point at them.
- A unit goes in the semester of its CAT (`S1_` or `S2_`). If its lessons start in the other semester, put a copy of the folder there too, named the same.
- Check the year folder's real name before writing (some are lettered, e.g. `a. Year 7`).

## Placing files

`export_docs.mjs` then `drive_docs.py` build the whole tree in a scratch folder: `Semester N/Curriculum Map/…` and `Semester N/<unit folder>/<subfolders>/…`. To place it:
1. List what is already in the class's drive folder.
2. Do a dry run that prints every copy, every rename and every folder it would create. Show it to the user.
3. Copy the scratch tree in. Never overwrite an existing file without saying so, and never delete without approval.
4. Check every file opens and that a curriculum map link resolves from where the map sits.

## Never

- Touch other faculties' folders.
- Delete the school's own files, or folders, without asking.
- Leave old-named copies next to new ones. Remove stale copies only with approval, after checking the replacements are there.
