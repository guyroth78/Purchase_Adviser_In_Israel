"""Fill the page template without retyping it.

Usage: python scripts/fill_template.py --data data.js --title "Short name" --out page.html
data.js holds the complete DATA block: `const DATA = { ... };`
The script copies assets/template.html, puts data.js between the DATA START / DATA END marker lines,
sets <title>, and writes the result. Nothing else in the template changes.
"""
import argparse, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent.parent
ap = argparse.ArgumentParser()
ap.add_argument("--data", required=True)
ap.add_argument("--title", required=True)
ap.add_argument("--out", required=True)
a = ap.parse_args()

page = (HERE / "assets" / "template.html").read_text(encoding="utf-8")
data = pathlib.Path(a.data).read_text(encoding="utf-8").strip()
if "const DATA" not in data:
    sys.exit("data.js must contain `const DATA = { ... };`")
start = page.index("\n", page.index("// === DATA START ===")) + 1
end = page.index("// === DATA END ===")
page = page[:start] + data + "\n" + page[end:]
title = a.title.replace("&", "&amp;").replace("<", "&lt;")
page = re.sub(r"<title>.*?</title>", f"<title>{title}</title>", page, count=1, flags=re.S)
pathlib.Path(a.out).write_text(page, encoding="utf-8")
print("wrote", a.out)
