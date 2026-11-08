# 2027 English Curriculum Plans

South Oakleigh College English faculty curriculum plans for 2027, Years 7 to 12.

- **Live site:** https://nmo-soc.github.io/english-2027/
- **Repository:** https://github.com/NMO-SOC/english-2027

The site is plain HTML with no server, database, framework or build tools. Each plan is a single HTML file that holds its own design, code and data. GitHub Pages publishes whatever is on the `main` branch.

---

## Contents

1. [Files](#files)
2. [How the site works](#how-the-site-works)
3. [The homepage](#the-homepage-indexhtml)
4. [A curriculum plan page](#a-curriculum-plan-page)
5. [Reading a plan (live site)](#reading-a-plan-live-site)
6. [Editing a plan (on your computer)](#editing-a-plan-on-your-computer)
7. [Printing and PDFs](#printing-and-pdfs)
8. [Unit plans (Word)](#unit-plans-word)
9. [Changing the design: template.html and build.py](#changing-the-design-templatehtml-and-buildpy)
10. [Adding a new plan](#adding-a-new-plan)
11. [Term dates, holidays and special weeks](#term-dates-holidays-and-special-weeks)
12. [How the data is stored](#how-the-data-is-stored)
13. [Links to a week or term](#links-to-a-week-or-term)
14. [Accessibility, phones and browsers](#accessibility-phones-and-browsers)
15. [Troubleshooting](#troubleshooting)
16. [Quick reference](#quick-reference)

---

## Files

| File | What it is |
|---|---|
| `index.html` | The homepage. It lists every year level and links to the plans that exist. |
| `template.html` | The master design for every curriculum plan. It holds no data. **All design changes are made here.** |
| `09ADVEN1.html` | The Year 9 Advanced English plan: the template design plus Year 9 data. |
| `10ADVEN1.html` | The Year 10 Advanced English plan: the template design plus Year 10 data. |
| `09EN.html` | The Year 9 Mainstream English plan (draft): the template design plus Year 9 data. |
| `10EN.html` | The Year 10 Mainstream English plan (draft): the template design plus Year 10 data. The film for the film study is still to be decided. |
| `build.py` | A small script that copies the template's design into the plans and keeps each plan's own title, heading and data. |
| `logo.png` | The faculty values logo (Consistency, Culture and Collaboration). It is the browser tab icon and sits in the homepage footer. |
| `README.md` | This file. |

---

## How the site works

- **One file per plan.** Each plan's file contains the page layout, the styling, the code, and the plan's entries (topics, CATs, learning intentions and so on) as data near the bottom.
- **Same file, two modes:**
  - **Live site (GitHub Pages):** read-only. Visitors can open, search and print plans, but can't type in them.
  - **Local copy (opened from your computer):** editable. You type into the boxes and press **Save** to write the changes back into the file.
- **Updating the site:** edit the file locally, save it, then commit and push it to GitHub. GitHub Pages updates within a minute or two.

The page detects the live site by its web address: any address ending in `github.io` is read-only.

---

## The homepage (`index.html`)

From top to bottom:

1. **Banner:** "South Oakleigh College", the title "2027 English Curriculum Plans", "Years 7 to 12", and a **current-week line** that updates itself (see below).
2. **Term colour strip:** four bands in the term colours (blue, green, orange, purple).
3. **Mainstream** column: Years 7, 8, 9 and 10.
4. **Advanced** column: Years 7, 8, 9 and 10.
5. **VCE** panel across the full width: Years 11 and 12.
6. **Footer:** the faculty values logo.

### Plan cards

- A **finished plan** is a coloured card in its year's colour (Year 7 blue, Year 8 green, Year 9 orange, Year 10 purple, VCE navy). It shows the year, the class code (e.g. `09ADVEN1`) and "Open plan".
- A **plan not made yet** is a dashed card marked "Coming soon".

To turn a "Coming soon" card into a link, replace its line in `index.html`. For example, for Year 8 Advanced, change:

```html
<div class="soon y8"><span>Year 8</span><small>Coming soon</small></div>
```

to:

```html
<a class="plan y8" href="08ADVEN1.html"><span>Year 8<span class="code">08ADVEN1</span></span><small>Open plan</small></a>
```

Use `y7`, `y8`, `y9`, `y10`, `y11` or `y12` for the colour.

### Current-week line

The banner line works out where the school year is from today's date:

| When | It shows |
|---|---|
| Before Term 1 | "Term 1 starts Wed 27 Jan 2027" |
| During a term | "Today: Term 2, Week 5". The plan cards then say "Open at Week 5" and open the plan scrolled to that week. |
| School holidays | "School holidays. Term 3 starts Mon 12 Jul" |
| After Term 4 | "The 2027 school year has finished" |

To preview a date, add `?today=YYYY-MM-DD` to the address, e.g. `index.html?today=2027-05-12`.

> **The homepage keeps its own copy of the term dates** (the `T=[...]` list in the script at the bottom of `index.html`). If term dates change, update them there **and** in `template.html` (see [Term dates](#term-dates-holidays-and-special-weeks)).

---

## A curriculum plan page

### Header

- **All plans** (left, house icon): back to the homepage.
- **Plan title** (centre): e.g. "10ADVEN1 Curriculum Plan 2027".
- **Tools** (right):
  - **Expand all / Collapse all:** opens or closes every lesson, assessment and curriculum-code panel.
  - **Save:** local editing only. Hidden on the live site.
  - **Print full plan:** see [Printing](#printing-and-pdfs).
  - **Print CATs and topics:** see [Printing](#printing-and-pdfs).
  - **Unit plans (Word):** download a unit of work as a Word curriculum map. See [Unit plans](#unit-plans-word).
  - **Clear all:** local editing only, and asks for confirmation. Hidden on the live site.
- **Hint line:** short instructions. These differ between the live site and a local copy.

### Sticky bar

This bar stays at the top of the screen as you scroll:

- **Term 1 to Term 4** buttons jump to each term.
- **This week** (navy) appears only during term and jumps to the current week.
- **Search box** (right): see [Search](#search).

### Assessments at a glance

A collapsible panel listing every CAT and exam in the plan. It is collapsed by default. Click the title, or Tab to it and press Enter, to open it.

- The badge beside the title shows how many assessments there are, with "Show" or "Hide" next to it.
- **Columns:**
  - **When:** term and week (a link) plus the date.
  - **Assessment:** the code (e.g. `S1_10ADVEN1_CAT1`) and its name.
  - **Curriculum codes:** that week's codes.
- Clicking a **When** link scrolls to that week and opens its assessment details.
- **It always prints**, even if collapsed on screen.

The panel is built from the plan's weekly entries. Any weekly topic starting with `S1_`, `S2_` or `EXAM` counts as an assessment (see [CATs](#cats-and-exams)).

### Term tables

There is one table per term, with one column per week.

**Week header** (coloured strip):
- Week number and the Monday's date.
- Notes such as public holidays ("Labour Day Mon", "King's Bday Mon", "Cup Day Tue"), "Starts Wed", "Ends Thu (Good Fri)".
- Labels for special weeks ("Exams", "Step-Up", "Activities Week" and so on).
- The current week has a navy outline and a "This week" tag.

**Each week's cell, top to bottom:**
1. **Weekly topic**, e.g. "Reading Macbeth: Acts 1–2". If it's a CAT or exam it shows as a navy badge instead (see below).
2. **Assessment details** (hidden until opened): only used for CAT and exam weeks.
3. **Curriculum codes:** a small bar. Click it to show that week's Victorian Curriculum codes. On the live site the bar is hidden when the week has no codes.
4. **Lessons:**
   - Normal weeks have four lessons: Lesson I, II, III and IV.
   - Weeks with a public holiday or a short week have Lesson I, II and III plus **Ad libitum** (a flexible lesson).
   - A lesson bar shows the lesson's title if it has one (e.g. "Act 1 Scene 3"), otherwise "Lesson I" and so on.
   - Click a lesson bar to open it. Each lesson has three fields:
     - **Learning Intention:** what students will learn.
     - **Success Criteria:** how students show it. Separate the criteria with ` | `; the live site shows them as a bulleted list.
     - **Do Now:** the starter task.

**Grey weeks** (Exams, Step-Up, Set-Up, Activities, Clean-Up) are shaded grey:
- Exam weeks keep a topic box (for the exam CAT) but have no lessons.
- Other grey weeks have no boxes at all.

### CATs and exams

A weekly topic is treated as an assessment when it **starts with** `S1_`, `S2_` or `EXAM`. For example:

```
S1_10ADVEN1_CAT1: Personal Text Response Essay (Rear Window)
EXAM: Creating Texts and English Conventions
```

- It shows as a navy badge.
- On the live site the text before the first `:` is shown small (the code) and the text after it larger (the title).
- Clicking the badge opens its **assessment details**.
- It appears in **Assessments at a glance**.

### Search

Type in the search box (at least 2 letters). The search covers weekly topics, assessment details, curriculum codes, lesson titles and all lesson fields.

- **Matching words are highlighted** in yellow, and the lessons and panels containing them open automatically.
- **Weeks with no match fade out** so the matches stand out.
- **Result line:** e.g. "44 matches in 13 weeks", or "No matches. Check the spelling or try a shorter word."
- **Enter** or **Next match** steps through the matches one by one ("Match 3 of 44"), scrolling each into view.
- **Esc** clears the search and closes everything it opened.

Search only changes what's on screen. It never changes or saves anything. Ctrl+F (the browser's own find) also works and opens collapsed panels to show matches.

---

## Reading a plan (live site)

On the live site:

- Nothing can be typed into or changed. The Save and Clear all buttons are hidden.
- Empty placeholders ("Assessment details", "What students will learn…") are hidden, so only real content shows.
- Lesson bars are white with a coloured edge. The solid "filled" colour used while editing (see below) isn't needed when reading.
- CAT badges split into code and title; success criteria show as bullet points.

---

## Editing a plan (on your computer)

### Setting up

1. Get a copy of the repository on your computer: clone it with Git or GitHub Desktop, or download it.
2. Open the plan file (e.g. `10ADVEN1.html`) by double-clicking it. **Use Chrome or Edge.** They can save straight back into the file; other browsers download a copy instead.

### Typing

- **Weekly topic:** click the top box in a week and type. Start with `S1_`, `S2_` or `EXAM` to make it a CAT (see [CATs](#cats-and-exams)).
- **Assessment details:** click a CAT badge to open its details box, then type.
- **Curriculum codes:** click the "Curriculum codes" bar to open it, then type.
- **Lessons:** click a lesson bar to open it, then type in Learning Intention, Success Criteria or Do Now.
- **Success Criteria:** separate the criteria with ` | ` (space, bar, space), e.g. `Uses evidence | Explains effect | Links to the question`.
- **Plan title:** the heading at the top can be clicked and edited.

Empty boxes show a grey italic hint about what goes in them.

**Spotting blanks:** a lesson bar turns **solid colour** once any of its three fields has text. Pale bars are lessons with nothing entered yet. This only shows on a local copy.

**Lesson titles** (e.g. "Act 1 Scene 3" in place of "Lesson III") have no typing box. They are stored as entries named like `1-4-3-title` (Term 1, Week 4, Lesson 3) in the plan's data line (see [How the data is stored](#how-the-data-is-stored)).

### Saving

Press **Save** or **Ctrl+S**.

- **Chrome / Edge:** the first time, a save window opens; pick the same plan file to overwrite it. Later saves in the same session go straight to that file, and the status shows "Saved at 10:42".
- **Other browsers:** a copy downloads, and the status says "Downloaded – replace the file in your folder with it". Move the downloaded file over the original in your repository folder.

While there are unsaved changes the status shows "Unsaved changes", and the browser warns you if you try to close the tab.

The saved file is the whole page with your entries written into its `SAVED` data line. The search, open panels and "This week" highlight are never saved.

**Clear all** empties every entry, after a confirmation. Nothing is lost until you press Save. If you clear by mistake, close the tab without saving.

### Publishing your changes

After saving, commit and push the changed file:

```bash
git add 10ADVEN1.html
git commit -m "Update Term 2 lessons"
git push
```

Or use GitHub Desktop: write a summary, then **Commit to main** and **Push origin**. The live site updates within a minute or two; refresh the page (Ctrl+F5 if it looks stale).

---

## Printing and PDFs

Plans are laid out for **A3 landscape**: each term starts on a new page, and colours print as on screen. There are two print buttons:

| Button | What prints | Year 10 length |
|---|---|---|
| **Print full plan** | Everything: Assessments at a glance, weekly topics, CATs with their details, curriculum codes, and every lesson with its Learning Intention, Success Criteria and Do Now. | about 9 pages |
| **Print CATs and topics** | A short overview: Assessments at a glance, weekly topics, and CATs with their details. Lessons and weekly curriculum codes are left out. | about 4 pages |

- **To make a PDF**, press either button and choose **Save as PDF** as the printer.
- In the print window, check the paper is **A3** and the layout is **Landscape**. Turn off "Headers and footers" for a cleaner page.
- **Ctrl+P** prints the full plan.
- When printing, every lesson prints open (you don't need to press Expand all first). The buttons, hint, sticky bar and search are left off the page.

---

## Unit plans (Word)

**Unit plans (Word)** downloads one unit of work as a `.docx` curriculum map in the school's format (landscape A4, one table). It works on the live site and on a local copy, and it never changes the plan.

**What counts as a unit:** it starts in the first teaching week after the previous assessment and ends with its CAT (a weekly topic starting `S1_` or `S2_`). Exams don't get unit plans: an exam and its revision weeks belong to no unit. Units can cross terms. Grey weeks without lessons (Set-Up, Step-Up and so on) are skipped. Weeks after the last assessment of the year belong to no unit. To move a unit's start, move the CAT before it.

The window lists every unit with its weeks. Click **Download .docx** beside one.

**The document:**

| Row or column | Contents |
|---|---|
| Row 1 | `CURRICULUM MAP – Year 9 English` (from the plan code; `ADV` gives "Advanced") |
| Row 2 | Semester and term(s), then "Unit of work:" with the CAT's title and the week range |
| Week | Week of the unit (Week 1, 2…), the term and week (e.g. Term 1, Week 5) and the Monday's date |
| TOPIC / Links to VIC Curriculum | The weekly topic, then each curriculum code on its own line |
| Weekly Learning Intention and Success Criteria | A summary of the week: up to 3 Learning Intentions and 3 Success Criteria, picked from the start, middle and end of the week |
| Link to lesson plans | Each lesson in full (title, Learning Intention, Success Criteria, Do Now), then an `[embed lesson plan]` placeholder. To fill one in Word: click the placeholder, then **Insert > Object > Create from File > Browse**, tick **Display as icon**, then **OK** |
| Assessment | Only in the CAT's week: the CAT and its assessment details |

The download includes unsaved edits currently on screen.

---

## Changing the design: `template.html` and `build.py`

**Rule:** every plan must look and work the same. Make design changes (layout, colours, buttons, features, term dates) **only in `template.html`**, then rebuild the plans with `build.py`. Don't edit the design inside the plan files (`09ADVEN1.html`, `10ADVEN1.html`, `09EN.html`, `10EN.html`) directly. The next rebuild would overwrite it.

### What build.py does

For each plan file named, it:

1. Copies the whole of `template.html`.
2. Puts back the plan's own four lines, unchanged:
   - `<title>…</title>`: the browser tab title
   - `<h1 contenteditable="true">…</h1>`: the heading on the page
   - `const DEFAULTS={…};`: data line
   - `const SAVED={…};`: data line
3. Writes the result over the plan file.

Each plan's entries are carried across character for character; the script never edits them. If it can't find exactly one of each of those four lines in both the template and the plan, it stops with an error and writes nothing to that file.

### Running it

From the repository folder (needs Python 3):

```bash
python build.py 09ADVEN1.html 10ADVEN1.html 09EN.html 10EN.html
```

List every plan file each time, including new ones.

### Checking nothing in the data changed

Before committing a design change, check that only the design changed:

```bash
git diff --stat
git diff 10ADVEN1.html | grep "^[-+]const \(SAVED\|DEFAULTS\)"
```

The second command should print nothing. Any output means a data line changed.

### Fonts and colours

| Thing | Value |
|---|---|
| Body font | Atkinson Hyperlegible (Google Fonts), designed for readability |
| Headings font | Source Serif 4 (Google Fonts) |
| Navy (headers, CATs, buttons) | `#1d2b4f` |
| Term 1 | `#2a5f9e` / light `#dce8f6` |
| Term 2 | `#2e7d32` / light `#dcefdb` |
| Term 3 | `#a8532a` / light `#f6e1d5` |
| Term 4 | `#7e3f84` / light `#efdff0` |

These are set as CSS variables at the top of the `<style>` block in `template.html` and `index.html`.

---

## Adding a new plan

Example: Year 8 Advanced, class code `08ADVEN1`.

1. **Copy the template:** duplicate `template.html` and name it `08ADVEN1.html`.
2. **Set the tab title:** in the new file, change `<title>Curriculum Plan 2027</title>` to `<title>08ADVEN1 Curriculum Plan 2027</title>`.
3. **Set the heading:** change `  <h1 contenteditable="true">Curriculum Plan 2027</h1>` to `  <h1 contenteditable="true">08ADVEN1 Curriculum Plan 2027</h1>`. Keep the two leading spaces exactly as they are, because `build.py` looks for them.
4. **Fill it in:** open the file in Chrome or Edge, type the plan in and **Save** over the same file.
5. **Link it from the homepage:** change its "Coming soon" card in `index.html` (see [Plan cards](#plan-cards)).
6. **Add it to future rebuilds:** from now on, run `python build.py 08ADVEN1.html 09ADVEN1.html 10ADVEN1.html 09EN.html 10EN.html`.
7. **Commit and push** the new file and `index.html`.

---

## Term dates, holidays and special weeks

The 2027 calendar is the `TERMS` list near the top of the `<script>` in `template.html`:

```js
const TERMS=[
 {n:1,start:"2027-01-25",weeks:9,label:"Wed 27 Jan – Thu 25 Mar (students start Thu 28 Jan)",
  notes:{1:"Starts Wed",7:"Labour Day Mon",9:"Ends Thu (Good Fri)"},grey:{},hol:[7,9]},
 {n:2,start:"2027-04-12",weeks:11,label:"Mon 12 Apr – Fri 25 Jun",
  notes:{10:"King's Bday Mon"},grey:{9:"Exams",11:"Set-Up"},hol:[10],noLessons:[9],exam:[9]},
 {n:3,start:"2027-07-12",weeks:10,label:"Mon 12 Jul – Fri 17 Sep",notes:{},grey:{},hol:[]},
 {n:4,start:"2027-10-04",weeks:11,label:"Mon 4 Oct – Fri 17 Dec",
  notes:{5:"Cup Day Tue"},grey:{6:"Exams",8:"Step-Up",9:"Step-Up",10:"Activities Week",11:"Clean-Up Week"},hol:[5],noLessons:[6,8,9,10,11],exam:[6]}
];
```

| Setting | Meaning |
|---|---|
| `n` | Term number. |
| `start` | The **Monday** of Week 1 (`YYYY-MM-DD`), even if term starts mid-week. Every week's date is counted from it. |
| `weeks` | Number of weeks (columns). |
| `label` | The date range shown under the term heading. |
| `notes` | Small notes under a week's date, e.g. `{7:"Labour Day Mon"}`. |
| `grey` | Weeks shaded grey with a label, e.g. `{9:"Exams"}`. |
| `hol` | Short weeks. These get three lessons plus **Ad libitum** instead of four lessons. |
| `noLessons` | Weeks with no lessons. |
| `exam` | Of the `noLessons` weeks, those that keep a topic box for an exam CAT. |

Victorian public holidays that fall in 2027 term time are already included:
- Labour Day: Mon 8 Mar, Term 1 Week 7
- Good Friday: 26 Mar, so Term 1 ends Thu 25 Mar
- King's Birthday: Mon 14 Jun, Term 2 Week 10
- Melbourne Cup: Tue 2 Nov, Term 4 Week 5

Easter Monday (29 Mar) and the AFL Grand Final Friday fall in the holidays. ANZAC Day falls on Sunday 25 Apr, with no weekday holiday in place of it.

**After changing `TERMS`:**
1. Run `build.py` on every plan.
2. Update the matching dates in `index.html` (the `T=[...]` list: each term's Monday, its first-day label and its last day).
3. Check that lessons still line up. Entries are stored by term, week and lesson number. For example, if you remove a lesson from a week, that lesson's text is still saved but no longer shown.

---

## How the data is stored

Each plan keeps its entries in two lines in its `<script>`:

```js
const DEFAULTS={...};
const SAVED={...};
```

- **`SAVED`** holds everything entered and saved. Pressing Save rewrites only this line.
- **`DEFAULTS`** holds starting entries (Year 9 Advanced has a copy here; the other plans' are empty). On load, `SAVED` entries win over `DEFAULTS`.

Both are lists of `"name":"text"` pairs. The names follow a pattern:

| Name | Example | What it is |
|---|---|---|
| `T--W` | `2--5` | Weekly topic (or CAT), Term 2 Week 5 |
| `info-T--W` | `info-2--6` | Assessment details, Term 2 Week 6 |
| `codes-T--W` | `codes-3--2` | Curriculum codes, Term 3 Week 2 |
| `T-W-L-title` | `1-4-3-title` | Title on the bar of Term 1, Week 4, Lesson 3 |
| `T-W-L-li` | `1-4-3-li` | That lesson's Learning Intention |
| `T-W-L-sc` | `1-4-3-sc` | That lesson's Success Criteria |
| `T-W-L-dn` | `1-4-3-dn` | That lesson's Do Now |

Lesson numbers run 1 to 4, and Ad libitum is lesson 4.

You can hand-edit these lines in a text editor, but the line must stay valid. Safer to type in the page and Save. The heading (`<h1>`) and tab title (`<title>`) are stored as normal HTML, not in these lines.

---

## Links to a week or term

Every week and term has its own address. Add it to the end of the plan's URL:

| Link | Goes to |
|---|---|
| `10ADVEN1.html#term3` | Term 3 |
| `10ADVEN1.html#w2-5` | Term 2, Week 5 |
| `10ADVEN1.html#overview` | Assessments at a glance |

`?today=YYYY-MM-DD` previews the "This week" highlight for any date, e.g. `10ADVEN1.html?today=2027-08-04`. This works on the homepage too.

---

## Accessibility, phones and browsers

- **Keyboard:**
  - Everything can be reached with Tab.
  - Enter or Space opens lesson bars, curriculum-code bars, CAT badges and the Assessments panel.
  - "Skip to the plan" appears on the first Tab press.
- **Screen readers:**
  - Collapsible bars announce whether they are open or closed.
  - Tables have hidden captions and column headers.
  - Search results and save status are announced.
- **Readable type:** Atkinson Hyperlegible font, and colours meet WCAG AA contrast.
- **Reduced motion:** animations are switched off if the device asks for it.
- **Phones (narrow screens):**
  - Weeks stack top to bottom instead of scrolling sideways.
  - The search box goes full width.
  - Buttons are larger on touch screens.
- **Ctrl+F** finds text inside collapsed panels and opens them, in Chrome and Edge.
- **Browsers:** current Chrome, Edge, Firefox and Safari can all read and print. Chrome or Edge is best for editing (direct Save). Search highlighting uses a newer browser feature; in older browsers the matches are still outlined and opened, just without the yellow highlight.

---

## Troubleshooting

| Problem | Fix |
|---|---|
| Live site hasn't changed after pushing | Wait a minute or two, then hard refresh (Ctrl+F5). Check the push reached GitHub, and check the repo's **Actions** tab for the Pages deploy. |
| Can't type in a plan | You're on the live site, which is read-only. Open your local copy of the file instead. |
| Save downloads a file instead of saving | You're not in Chrome/Edge, or you cancelled the save window. Move the downloaded file over the original, or reopen in Chrome/Edge. |
| "Not saved: this file's data line is missing" | The `const SAVED=…;` line was damaged or removed. Your work is still on screen, so don't close the tab. Restore the file from Git (`git checkout 10ADVEN1.html`) in a separate copy, or ask for help. |
| `build.py` stops with an `AssertionError` | One of the four kept lines (title, h1, DEFAULTS, SAVED) is missing or appears twice in the named file or the template. Check the spacing of the `<h1>` line. Nothing was written to that file. |
| A CAT shows as a normal topic | It must **start** with `S1_`, `S2_` or `EXAM`, with no space before it. |
| Success criteria show as one line on the live site | Separate them with ` \| ` (space, bar, space). |
| "This week" is missing | It only appears during term weeks. Preview with `?today=2027-05-12`. |
| Plan looks blank | A JavaScript error, usually from a hand-edited data line. Open the browser console (F12) to see it, or restore the file from Git. |
| Print has the wrong size or splits oddly | Choose A3 and Landscape in the print window, and set margins to Default. |

---

## Quick reference

| Task | How |
|---|---|
| Edit a plan | Open the local file in Chrome/Edge, type, press Ctrl+S, then commit and push |
| Change the design for all plans | Edit `template.html`, run `python build.py 09ADVEN1.html 10ADVEN1.html 09EN.html 10EN.html`, check data lines unchanged, then commit and push |
| Add a plan | Copy `template.html`, set the title and h1, fill in, link from `index.html`, add to the build command |
| Make a CAT | Start the weekly topic with `S1_`, `S2_` or `EXAM`, e.g. `S1_09ADVEN1_CAT1: Essay` |
| List success criteria | Separate with ` \| ` |
| Print everything | **Print full plan** |
| Print an overview | **Print CATs and topics** |
| Make a PDF | Either print button, then choose Save as PDF |
| Make a unit plan | **Unit plans (Word)**, then **Download .docx** beside the unit |
| Change term dates | `TERMS` in `template.html` and `T` in `index.html`, then rebuild |
| Link to a week | `10ADVEN1.html#w2-5` |
| Preview a date | Add `?today=2027-05-12` to the address |
