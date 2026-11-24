# Curriculum codes (VC 2.0)

## Where codes come from

Use only codes from the VCAA Victorian Curriculum 2.0 content descriptions for the subject (Levels 7–10). The user supplies them as a document, or they come from the VCAA site. Search by code before using one. **Never write a code from memory.**

## Format

`VC2E9LA07` (English) reads as:
- `VC2`: the Victorian Curriculum 2.0 prefix
- `E`: the subject letter(s); each subject has its own, so check the document
- `9`: the level (Year 9)
- `LA`: the strand letters; `KLA.strandRe` in `template.html` must capture these
- `07`: the item number

The plan's own CAT code (`S1_09SCI_CAT1`) is not a curriculum code. Keep the two apart.

## How to choose codes for a week

- Match the week's topic to the content description it teaches.
- Two or three codes per week is the usual pattern. Don't put every code in one week.
- Each CAT's details end with `Curriculum codes: …`, listing what the CAT assesses.
- Check every code in the plan appears in the content descriptions. A typo shows the school a wrong code.

## Coverage

If the user asks for a coverage check, list each code used with its weeks, then the codes for the level that are never used, and ask which are wanted. Don't add codes just to fill the list.

## Achievement standards

`KLA.std` holds the Levels 9 and 10 achievement standards for the unit plan. Quote them from VC 2.0. If you have to draft them, say so in every reply and ask the user to check them against the official text.

## VCE (Years 11 and 12)

VCE plans map to the study design, not VC 2.0. Fill `VCE_MAP` (unit name pattern to outcome) and `VCE_SD` (each outcome's unit, area of study, outcome statement, key knowledge and key skills) in `template.html`, quoting the study design.
