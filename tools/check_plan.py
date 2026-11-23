#!/usr/bin/env python3
"""v2 新增：生成前的規劃檢查。用法：python3 tools/check_plan.py [slide-plan.md]"""
import re, sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
plan = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "workflow" / "slide-plan.md"
text = plan.read_text(encoding="utf-8")
errors = []
# P1：表格中每張投影片對應的 Wiki 頁都要存在
for row in re.findall(r"^\|\s*(\d+)\s*\|[^|]*\|[^|]*\|([^|]*)\|", text, re.M):
    for pg in [p.strip() for p in row[1].split(",") if p.strip()]:
        if not (ROOT / "wiki" / f"{pg}.md").exists():
            errors.append(f"[P1 頁不存在] #{row[0]} → {pg}.md")
# P2：學習目標覆蓋
for lg in ["LG1", "LG2", "LG3"]:
    if lg not in text and not (lg == "LG2" and "LG1–3" in text):
        errors.append(f"[P2 未覆蓋] {lg}")
# P3：關鍵數字必須在對應 Wiki 頁找得到
for n, pg, nums in re.findall(r"^- #(\d+) ([\w-]+): (.+)$", text, re.M):
    w = (ROOT / "wiki" / f"{pg}.md").read_text(encoding="utf-8")
    for tok in [t.strip() for t in nums.split(",")]:
        core = re.match(r"[\d.:–]+", tok).group(0)
        if not re.search(rf"(?<![\d.]){re.escape(core)}(?![\d])", w):
            errors.append(f"[P3 數字無依據] #{n} 計畫使用「{tok}」，{pg}.md 找不到 → 先回 Ingest 或刪除")
print(f"規劃檢查：{plan.name}")
for e in errors: print("  ✗", e)
print(f"結果：{len(errors)} 個錯誤")
sys.exit(1 if errors else 0)
