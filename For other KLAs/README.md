# Curriculum Plans: handover kit for other KLAs

This folder is a copy of the 2027 English Curriculum Plans site with the English content taken out. It looks and works the same: weekly topics, lessons, CATs, search, printing, copy buttons, the overview page, and the three Word exports (**curriculum maps**, **unit plans** and the **Learning Area Plan**). It is ready for any subject.

Everything is plain HTML. There is no server, no database and nothing to install except Python, which is only needed for `build.py`.

## What's in the folder

| File | What it is |
|---|---|
| `index.html` | The homepage. It has a card for every class, and "Coming soon" cards for plans not made yet. |
| `template.html` | The master design for every plan. **The subject settings are at the top of its script** (see step 2). |
| `09SUB.html` | An empty example plan (Year 9 Mainstream). Rename it and fill it in. |
| `overview.html` | The whole-subject overview with search, print and the **Learning Area Plan (Word)** download. |
| `build.py` | Copies the template's design into your plans and keeps each plan's own data. |

## Setting it up for your subject

### 1. Get your own copy
The easiest way is to create a new GitHub repository (e.g. `science-2027`) and copy these five files into it. Then turn on **Settings → Pages → Deploy from branch → main**. Your site appears at `https://<your-account>.github.io/science-2027/`.

(You can also use the folder where it is: `.../english-2027/For%20other%20KLAs/`.)

### 2. Edit the subject settings (once)
Open `template.html` in a text editor and find `SUBJECT SETTINGS` near the top of the script:

```js
const KLA={
  name:"Subject",                 // "Science", "Humanities"...
  strandRe:/^VC2[A-Z]+\d+([A-Z]+)/, // how a VC 2.0 code shows its strand
  strands:{},                     // e.g. {U:"Science understanding", I:"Science inquiry"}
  std:{9:"...",10:"..."},         // Level 9 and 10 achievement standards, pasted from VC 2.0
  vceRe:/^[A-Z]+(12|34)$/,        // which plan codes are VCE (Units 1-2, 3-4)
  subStrands:[ ... ],             // keywords that name a unit's sub-strand in the unit plan
  defaultSubStrand:"to be added",
  defaultFocus:"the key ideas of the unit"
};
```

These settings feed the unit plan and curriculum map exports, so set them before you download anything.

Also in `template.html`, filled in when ready:
- `CM_FOLDERS`: the drive folder name for each unit, so the Word documents link to the lesson plans. Plans without an entry just have no links.
- `VCE_MAP` and `VCE_SD`: for Years 11 and 12 only. These map units to your study design's outcomes, key knowledge and key skills.
- `TERMS`: the term dates, public holidays, exam weeks and Step-Up weeks. These are already set for 2027.
- The unit plan's adjustments wording (EAL, Integration, Extension) is generated in `unitDocxV2`. Change it if it doesn't suit your subject.

### 3. Rename the words "Subject" and "SUB"
- `index.html`: in the title, the heading, the overview button and the plan codes on the cards.
- `overview.html`: in the title, the heading, the `CLASSES` and `LAP_YEARS` lists (your plan codes) and "Curriculum Area: Subject" (Learning Area Plan header).

The code naming is `09SUB` (Year 9), `09ADVSUB` (Year 9 Advanced) and `SUB12`/`SUB34` (VCE). It's best to keep this pattern with your own letters, e.g. `09SCI`, `09ADVSCI`, `BIO12`. The year level and "Advanced" are read from the code.

### 4. Make a plan
1. Copy `template.html` to `09SCI.html`, or rename `09SUB.html`.
2. In the file, change `<title>` and `<h1>` to start with the code: `09SCI Curriculum Plan 2027`.
3. Open the file **from your computer** in Chrome or Edge. It is editable locally and read-only on the live site.
4. Type the weekly topics, lessons, learning intentions, success criteria, Do Nows and VC 2.0 codes, then press **Save**.
5. On the homepage, turn that class's "Coming soon" card into a link (copy the Year 9 card).
6. Commit and push. The site updates within a minute or two.

### Writing assessments
A week becomes a CAT or exam when its topic starts with `S1_` / `S2_` / `EXAM`, e.g. `S1_09SCI_CAT1: Practical report`. A **unit of work** runs from the first lesson after the previous CAT to this CAT. Unit plans and curriculum maps are built from units, so each CAT ends one unit.

Week topics starting `Developmental task` show as teal badges. Per-plan calendar changes (normal weeks, greyed weeks, lesson counts, "SAC" instead of "CAT") are set in that plan's `const PLAN={...}` line. See the comments next to `PLAN` in `template.html`.

## The Word exports
| Where | Button | What you get |
|---|---|---|
| Each plan | **Curriculum map (Word)** | One document per semester in the school's curriculum map layout, with Do Nows as retrieval practice and links to lesson plans. |
| Each plan | **Unit plans (Word)** | The school's unit plan template for each unit (first lesson to CAT): adjustments, VC 2.0 mapping, big idea, essential understandings, capabilities and assessment. |
| `overview.html` | **Learning Area Plan (Word)** | Every class by semester and week, with the topic and VC 2.0 codes, coloured by unit of work. |

Everything comes from the plan data, so change the plan and download again.

## Changing the design
Edit only `template.html`, then copy the design into every plan without touching its data:

```
python build.py 09SCI.html 10SCI.html 09ADVSCI.html
```

## Good to know
- `overview.html` and the homepage's "next assessment" read the plans over the web. Open them from the live site or a local web server (`python -m http.server`), not by double-clicking.
- A plan listed in `overview.html` that doesn't exist yet shows as "coming soon".
- Analytics are optional. Paste your own GoatCounter script line where `index.html`, `overview.html` and `template.html` say so.
- To add a faculty logo, put `logo.png` in the folder and see the comment at the bottom of `index.html`.
