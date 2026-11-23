#!/usr/bin/env python3
"""簡報檢查：每張投影片的內容必須能追溯到 Wiki。用法：python3 tools/check_slides.py"""
import re, sys, pathlib, html as H

ROOT = pathlib.Path(__file__).resolve().parent.parent
WIKI, RAW = ROOT / "wiki", ROOT / "raw"
doc = (ROOT / "docs" / "index.html").read_text(encoding="utf-8")
doc = re.sub(r"<(script|style)\b.*?</\1>", "", doc, flags=re.S)
raw_ids = {p.name.split("-")[0] for p in RAW.glob("S*.md")}
slides = re.findall(r'<section class="slide[^"]*"([^>]*)>(.*?)</section>', doc, re.S)
time_re = re.compile(r"\d{1,2}:\d{2}")
num_re = re.compile(r"(?<![A-Za-z\d.])\d+(?:\.\d+)?")
errors, lg_seen = [], set()

def attr(a, name):
    m = re.search(rf'{name}="([^"]*)"', a); return [x.strip() for x in m.group(1).split(",") if x.strip()] if m else []

for i, (a, body) in enumerate(slides, 1):
    pages, srcs, lgs = attr(a, "data-wiki"), attr(a, "data-src"), attr(a, "data-lg")
    lg_seen.update(lgs)
    if not pages:
        errors.append(f"[C1 無對應] 第 {i} 張沒有 data-wiki"); continue
    wtext = ""
    for pg in pages:
        f = WIKI / f"{pg}.md"
        if not f.exists(): errors.append(f"[C1 頁不存在] 第 {i} 張 → wiki/{pg}.md"); continue
        wtext += f.read_text(encoding="utf-8")
    for s in srcs:
        if s not in raw_ids: errors.append(f"[C2 來源不存在] 第 {i} 張 {s}")
        elif f"[{s}]" not in wtext: errors.append(f"[C2 來源不在對應頁] 第 {i} 張 {s} 沒出現在 {pages}")
    body = re.sub(r'<[^>]*data-nocheck[^>]*>.*?</[^>]+>', "", body, flags=re.S)
    text = H.unescape(re.sub(r"<[^>]+>", " ", body))
    toks = time_re.findall(text)
    text2 = time_re.sub(" ", text)
    toks += [t for t in num_re.findall(text2) if len(t) >= 2 or "." in t]
    for t in sorted(set(toks)):
        if not re.search(rf"(?<![\d.]){re.escape(t)}(?![\d])", wtext):
            errors.append(f"[C3 數字無依據] 第 {i} 張出現「{t}」，但對應 Wiki 頁 {pages} 找不到")
for lg in ["LG1", "LG2", "LG3"]:
    if lg not in lg_seen: errors.append(f"[C4 學習目標未覆蓋] {lg}")

print(f"簡報檢查：{len(slides)} 張投影片")
for e in errors: print("  ✗", e)
print(f"結果：{len(errors)} 個錯誤")
sys.exit(1 if errors else 0)
