# Rebuild plans from template.html, keeping each plan's title, heading and data.
# Usage: python build.py 09ADVEN1.html 10ADVEN1.html   (edit design in template.html only)
import re,sys
tpl=open("template.html",encoding="utf-8",newline="").read()
pats=[r"<title>.*</title>",r'  <h1 contenteditable="true">.*</h1>',r"const DEFAULTS=.*;",r"const SAVED=\{.*;",r"const PLAN=.*;"]
for f in sys.argv[1:]:
    old=open(f,encoding="utf-8",newline="").read().replace("\r\n","\n")
    out=tpl
    for p in pats:
        o=re.findall("^"+p+"$",old,re.M); t=re.findall("^"+p+"$",out,re.M)
        if p.startswith("const PLAN") and not o: continue  # older plans have no PLAN line: keep the template's default
        assert len(o)==1 and len(t)==1,(f,p,len(o),len(t))
        out=out.replace(t[0],o[0],1)
    open(f,"w",encoding="utf-8",newline="").write(out)
    print("built",f)
