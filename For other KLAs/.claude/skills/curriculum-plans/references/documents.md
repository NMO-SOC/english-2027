# The generated documents

## Terms used everywhere

- **Unit of work**: runs from the first teaching lesson after the previous CAT through to its CAT. The CAT ends the unit. Exams are never part of a unit. A unit can span a term break or the semester break.
- **Learning intention (LI)**: the "We will…" sentence for a lesson.
- **Success criteria (SC)**: "I can…" statements, separated by ` | ` in the plan data.
- **Do Now**: the short starter task at the start of a lesson (retrieval practice).

## Lesson style (match the English plans)

- The LI starts "We will…".
- Three SC, each starting "I can…".
- The Do Now is a short starter task of one or two lines, usually retrieving last lesson's learning.
- Four lessons per week. Holiday weeks have three lessons plus Ad libitum. Camp and induction weeks have what the calendar allows.
- CAT weeks run prep lessons, then the CAT lessons, then a reflection.
- Lesson titles name the focus (a topic, an experiment, a skill). The page shows them as "Lesson I - title".
- Be specific to the actual texts, topics and sources. Never write generic filler.

Every lesson drafted this way is a draft. Say so.

## Curriculum map (one per semester)

Made by the plan's **Curriculum map (Word)** button, or `export_docs.mjs`. There is one row per week:
- **Week:** the week number, the term week and Monday's date.
- **Topic / Links to VIC Curriculum:** the topic, then its codes.
- **Learning Intentions and Success Criteria:** up to three of each.
- **Key Knowledge:** the lesson title, or else the LI reworded.
- **Link to Lesson plans:** a relative link into the unit's `Lesson Plans` folder.
- **Do Now:** each lesson's Do Now.
- **Assessment:** CAT weeks only, linked to the CAT brief.

Semester 1 is Terms 1–2 and Semester 2 is Terms 3–4. Step-Up weeks are left out of Semester 2. The map must sit in its semester's `Curriculum Map` folder for the links to work.

## Unit plan (one per unit)

Made by the **Unit plans (Word)** button, or `export_docs.mjs`. It has these sections:
1. **Adjustments:** EAL, Integration and Extension, drawn from the unit's topic. These are drafts.
2. **Curriculum mapping:** the VC 2.0 codes and the Levels 9/10 achievement standards (`KLA.std`). For VCE, it shows the study design outcome, key knowledge and key skills.
3. **Topic strip:** the strand (from the codes and `KLA.strands`), the sub-strand (from `KLA.subStrands`) and the teaching time in weeks.
4. **Big idea and essential understandings:** ONE learning intention and ONE success criterion summarising the unit.
5. **Cross-curriculum priorities, capabilities and 21CLD:** keyword-based ticks for the user to check.
6. **Common assessments:** pre-assessment (the first Do Now), formative, and summative (the CAT).

## Lesson plans and CAT briefs

These are made by `drive_docs.py`:
- **Lesson plans:** one document per unit, listing every week and lesson with its LI, SC and Do Now. Lessons with nothing entered say "(not yet entered)".
- **CAT brief:** one per CAT, with the title, unit, due week, codes and details. The rubric says "To be added" until the user supplies one.

## Learning Area Plan (one for the subject)

Made by **Learning area plan (Word)** on `overview.html`. Each class has a block per semester, with a topic row and a codes row for every week. Each unit is coloured as a whole, and there is an Exam Revision column.

## Checking any document

- It opens as a zip (`zipfile.ZipFile(f).testzip()` returns None). `drive_docs.py` checks its own documents.
- Read a sample of the text against the plan.
- You can't check the layout in Word from the command line. Say so, and ask the user to open one.
