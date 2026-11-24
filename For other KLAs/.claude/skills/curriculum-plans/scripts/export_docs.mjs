// Make every Word document for one plan, without a browser, laid out as the drive folders.
// Usage: node export_docs.mjs <path-to-plan.html> <outdir>
// It runs the plan's own code (from template.html), so the documents are exactly what the site's buttons make.
// Writes into <outdir>:
//   units.json                                  every unit (first lesson to CAT) with its weeks and lessons
//   Semester N/Curriculum Map/<CODE> Semester N Curriculum Map.docx
//   Semester N/<unit folder>/Unit Plan/<CODE> Unit Plan - <unit>.docx
// Then run drive_docs.py on the same outdir for the lesson plans and CAT briefs.
import fs from "fs";
import vm from "vm";
import path from "path";

const [, , plan, outdir] = process.argv;
if (!plan || !outdir) { console.error("usage: node export_docs.mjs <plan.html> <outdir>"); process.exit(1); }

const src = fs.readFileSync(plan, "utf8");
const store = Object.assign({}, JSON.parse(src.match(/^const DEFAULTS=(\{.*\});$/m)[1]), JSON.parse(src.match(/^const SAVED=(\{.*\});$/m)[1]));
const title = src.match(/<title>(.*)<\/title>/)[1], code = title.split(" ")[0];
const _st = src.indexOf("<script>") + 8;
const script = src.slice(_st, src.indexOf("</script>", _st));
const cut = (a, b) => {
  const i = script.indexOf(a), j = script.indexOf(b, i + 1);
  if (i < 0 || j < 0) throw new Error(`anchor not found: ${a} / ${b} (has template.html changed?)`);
  return script.slice(i, j);
};
const parts = [
  cut("// ===== SUBJECT SETTINGS", "let dirty"),
  cut("const MONTHS", "function setStatus"),
  cut("function units()", "// Curriculum map (Word)"),
  cut("// Curriculum map (Word)", 'document.getElementById("cmbtn")'),
  cut("// Unit plans (Word): one document", 'document.getElementById("upv2btn")'),
].join("\n"); // the plan's own DEFAULTS and SAVED lines are inside the first part

const stubEl = () => ({ style: { setProperty() {} }, classList: { add() {}, remove() {}, toggle() {} }, addEventListener() {},
  querySelector() { return stubEl(); }, querySelectorAll() { return []; }, appendChild() {}, insertAdjacentHTML() {},
  setAttribute() {}, getAttribute() { return null; }, dataset: {} });
const sandbox = {
  addEventListener() {}, setTimeout,
  document: { title, getElementById: () => stubEl(), addEventListener() {}, querySelector: () => stubEl(), querySelectorAll: () => [],
    createElement: () => stubEl(), body: stubEl(), documentElement: stubEl(), head: stubEl() },
  location: { search: "", hostname: "localhost", hash: "" },
  URLSearchParams, Date, Set, Map, TextEncoder, Blob, console, Math, JSON, Object, Array, String, Number, RegExp, Promise,
};
vm.createContext(sandbox);
vm.runInContext(parts + "\n;Object.assign(this,{units,unitName,cmDocx,unitDocxV2,fileSafe,CM_FOLDERS,TERMS});", sandbox);

const S = sandbox, folders = S.CM_FOLDERS[code] || {};
const write = async (rel, blob) => {
  const f = path.join(outdir, ...rel);
  fs.mkdirSync(path.dirname(f), { recursive: true });
  fs.writeFileSync(f, Buffer.from(await blob.arrayBuffer()));
};
const monday = (t, w) => { const d = new Date(S.TERMS.find((x) => x.n === t).start + "T00:00"); d.setDate(d.getDate() + 7 * (w - 1)); return d.toISOString().slice(0, 10); };

// 1. Units, with the semester from the CAT prefix and the drive folder from CM_FOLDERS
const list = S.units().map((u) => {
  const name = S.unitName(u), cat = (store[u[u.length - 1].k] || "").trim();
  return { name, cat, sem: cat.startsWith("S2_") ? 2 : 1, folder: folders[name] || null,
    weeks: u.map((x) => ({ t: x.t, w: x.w, k: x.k, monday: monday(x.t, x.w), topic: (store[x.k] || "").trim(), lessons: x.lessons })) };
});
fs.mkdirSync(outdir, { recursive: true });
fs.writeFileSync(path.join(outdir, "units.json"), JSON.stringify({ code, units: list }, null, 1), "utf8");

// 2. Curriculum maps, one per semester
for (const sem of [1, 2]) await write([`Semester ${sem}`, "Curriculum Map", `${code} Semester ${sem} Curriculum Map.docx`], S.cmDocx(sem));

// 3. Unit plans, one per unit, in the unit's folder
const us = S.units();
for (let i = 0; i < us.length; i++) {
  const u = list[i], dir = u.folder || `(no CM_FOLDERS entry) ${S.fileSafe(u.name)}`;
  await write([`Semester ${u.sem}`, dir, "Unit Plan", `${code} Unit Plan - ${S.fileSafe(u.name)}.docx`], S.unitDocxV2(us[i]));
}
const missing = list.filter((u) => !u.folder).map((u) => u.name);
console.log(`${code}: ${list.length} units, 2 curriculum maps, ${list.length} unit plans -> ${outdir}`);
if (missing.length) console.log("No CM_FOLDERS entry (add to template.html, then rebuild):", missing.join("; "));
