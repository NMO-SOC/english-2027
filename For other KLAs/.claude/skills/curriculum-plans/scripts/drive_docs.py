"""Lesson plans and CAT briefs for one plan, into the folder tree export_docs.mjs made.
Usage: python drive_docs.py <path-to-plan.html> <outdir>      (run export_docs.mjs on the same outdir first)
Needs: pip install python-docx
Writes, for each unit:
  Semester N/<unit folder>/Lesson Plans/<CODE> - <unit> - Lesson Plans.docx
  Semester N/<unit folder>/Assessments & Rubrics/<CODE> - <unit> - CAT Assessment.docx
and an empty Class Resources folder. Copy the finished tree into the class's drive folder.
"""
import json, os, re, sys, zipfile, datetime as dt
from docx import Document
from docx.shared import Pt

MON = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
fmt = lambda iso: (lambda d: f"{d.day} {MON[d.month-1]}")(dt.date.fromisoformat(iso))
safe = lambda s: re.sub(r'[\\/*?"<>|]', "", s.replace(":", " -")).replace("  ", " ").strip()  # same as the site's fileSafe


def doc():
    d = Document(); st = d.styles["Normal"]; st.font.name = "Aptos"; st.font.size = Pt(10); return d


def lesson_plans(code, u, store, path):
    d = doc()
    a, b = u["weeks"][0], u["weeks"][-1]
    d.add_heading(f"{code}: {u['name']}", level=1)
    d.add_paragraph(f"Lesson plans. Term {a['t']} Week {a['w']} to Term {b['t']} Week {b['w']} ({len(u['weeks'])} weeks).")
    for n, wk in enumerate(u["weeks"], 1):
        d.add_heading(f"Week {n}: {wk['topic']}", level=2)
        d.add_paragraph(f"Term {wk['t']}, Week {wk['w']} (Monday {fmt(wk['monday'])})")
        for i, lname in enumerate(wk["lessons"], 1):
            kk = f"{wk['t']}-{wk['w']}-{i}"
            title, li, dn = (store.get(kk + x, "").strip() for x in ("-title", "-li", "-dn"))
            sc = [s.strip() for s in store.get(kk + "-sc", "").split("|") if s.strip()]
            p = d.add_paragraph(); p.add_run(f"{lname} - {title}" if title else lname).bold = True
            if not (li or sc or dn):
                p.add_run("  (not yet entered)").italic = True; continue
            if li: p = d.add_paragraph(); p.add_run("Learning Intention: ").bold = True; p.add_run(li)
            if sc:
                d.add_paragraph().add_run("Success Criteria:").bold = True
                for s in sc: d.add_paragraph(s, style="List Bullet")
            if dn: p = d.add_paragraph(); p.add_run("Do Now: ").bold = True; p.add_run(dn)
    d.save(path)


def cat_brief(code, u, store, path):
    wk = u["weeks"][-1]; d = doc()
    d.add_heading(f"{code}: {u['cat']}", level=1)
    d.add_paragraph(f"Unit of work: {u['name']}")
    d.add_paragraph(f"Due: Term {wk['t']}, Week {wk['w']} (Monday {fmt(wk['monday'])})")
    d.add_heading("Curriculum codes", level=2); d.add_paragraph(store.get("codes-" + wk["k"], "").strip() or "Not yet entered.")
    d.add_heading("Assessment details", level=2)
    info = [l.strip() for l in store.get("info-" + wk["k"], "").split("\n") if l.strip()]
    for l in info or ["Assessment details not yet entered in the plan."]: d.add_paragraph(l)
    d.add_heading("Rubric", level=2); d.add_paragraph("To be added.")
    d.save(path)


if __name__ == "__main__":
    plan, out = sys.argv[1], sys.argv[2]
    src = open(plan, encoding="utf-8").read()
    store = {**json.loads(re.search(r"^const DEFAULTS=(\{.*\});$", src, re.M).group(1)),
             **json.loads(re.search(r"^const SAVED=(\{.*\});$", src, re.M).group(1))}
    data = json.load(open(os.path.join(out, "units.json"), encoding="utf-8")); code = data["code"]
    made = []
    for u in data["units"]:
        base = os.path.join(out, f"Semester {u['sem']}", u["folder"] or f"(no CM_FOLDERS entry) {safe(u['name'])}")
        for sub in ("Lesson Plans", "Assessments & Rubrics", "Class Resources", "Unit Plan"): os.makedirs(os.path.join(base, sub), exist_ok=True)
        lp = os.path.join(base, "Lesson Plans", f"{code} - {safe(u['name'])} - Lesson Plans.docx")
        cb = os.path.join(base, "Assessments & Rubrics", f"{code} - {safe(u['name'])} - CAT Assessment.docx")
        lesson_plans(code, u, store, lp); cat_brief(code, u, store, cb); made += [lp, cb]
    bad = [f for f in made if zipfile.ZipFile(f).testzip() is not None]
    print(f"{code}: {len(made)} documents" + (f", BROKEN: {bad}" if bad else ", all open as valid .docx"))
