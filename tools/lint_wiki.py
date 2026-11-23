#!/usr/bin/env python3
"""Wiki lint：檢查引用、連結、孤兒頁、frontmatter。用法：python3 tools/lint_wiki.py"""
import re, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
WIKI, RAW = ROOT / "wiki", ROOT / "raw"
SPECIAL = {"index.md", "log.md"}
cite_re = re.compile(r"\[(S\d+)\]")
link_re = re.compile(r"\]\(([^)#\s]+\.md)(?:#[^)]*)?\)")
digit_re = re.compile(r"\d")

raw_ids = {p.name.split("-")[0] for p in RAW.glob("S*.md")}
pages = sorted(WIKI.glob("*.md"))
index_text = (WIKI / "index.md").read_text(encoding="utf-8") if (WIKI / "index.md").exists() else ""
errors, warns = [], []

for p in pages:
    text = p.read_text(encoding="utf-8")
    fm = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    body = text[fm.end():] if fm else text
    # R4 連結有效
    for target in link_re.findall(text):
        if not (WIKI / target).exists():
            errors.append(f"[R4 斷連結] {p.name} → {target} 不存在")
    if p.name in SPECIAL:
        continue
    # R1 frontmatter
    if not fm or "sources:" not in fm.group(1):
        errors.append(f"[R1 frontmatter] {p.name} 缺少 sources 欄位")
        declared = set()
    else:
        declared = set(re.findall(r"S\d+", fm.group(1)))
    # R5 孤兒頁
    if f"({p.name})" not in index_text:
        errors.append(f"[R5 孤兒頁] {p.name} 沒有列在 index.md")
    in_code = False
    for n, line in enumerate(body.splitlines(), 1):
        s = line.strip()
        if s.startswith("```"):
            in_code = not in_code
            continue
        if in_code or not s or s.startswith("#") or s.startswith("|---") or s.startswith(">"):
            continue
        cites = set(cite_re.findall(s))
        # R3 來源存在、R6 有宣告
        for c in cites:
            if c not in raw_ids:
                errors.append(f"[R3 來源不存在] {p.name}:{n} 引用 {c}")
            elif c not in declared:
                errors.append(f"[R6 未宣告] {p.name}:{n} 引用 {c} 但 frontmatter 沒列")
        # R2 含數字的主張要有引用（去掉連結、引用標記後再判斷）
        plain = cite_re.sub("", re.sub(r"\[[^\]]*\]\([^)]*\)", "", s))  # v1.1：連結文字（如「V60 入門食譜」）不算主張
        plain = re.sub(r"^(\d+\.|[-*])\s*", "", plain)  # 去掉清單編號
        if digit_re.search(plain) and not cites:
            errors.append(f"[R2 數字無引用] {p.name}:{n} {s[:60]}")
    for c in declared:
        if f"[{c}]" not in body:
            warns.append(f"[W1] {p.name} 宣告了 {c} 但內文沒有引用")

print(f"Wiki lint：{len(pages)} 頁，來源 {sorted(raw_ids)}")
for e in errors: print("  ✗", e)
for w in warns: print("  !", w)
print(f"結果：{len(errors)} 個錯誤，{len(warns)} 個警告")
sys.exit(1 if errors else 0)
