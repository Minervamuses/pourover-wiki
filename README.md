# ☕ 手沖咖啡 LLM Wiki → 教學 HTML 簡報

用「先討論、後生成」建立一個手沖咖啡的 LLM Wiki，再以 Wiki 作為**唯一知識來源**，產生給初學者的教學型 HTML 簡報。

- **教學簡報**：`docs/index.html`（透過 GitHub Pages 瀏覽）
- **Wiki 入口**：[wiki/index.md](wiki/index.md)
- **流程設計**：[workflow/graph.md](workflow/graph.md)
- **執行紀錄**：[workflow/run-log.md](workflow/run-log.md)
- **反思**：[workflow/reflection.md](workflow/reflection.md)

## 結構
```
discussion/00-scope.md   先討論：範圍、受眾、學習目標（生成前的契約）
CLAUDE.md                Wiki schema：LLM 維護 Wiki 的規則（ingest / query / lint）
raw/                     6 張來源卡（S1–S6，改寫重點＋原文連結）
wiki/                    13 頁 Wiki（概念頁＋index＋log＋conflicts）
workflow/                graph、slide-plan、run-log、reflection、原始檢查輸出
tools/                   lint_wiki.py、check_plan.py、check_slides.py
docs/index.html          教學簡報（18 張）
```

## 重跑全部檢查
```bash
python3 tools/lint_wiki.py && python3 tools/check_plan.py && python3 tools/check_slides.py
```

## 來源
| ID | 來源 | 等級 |
|---|---|---|
| S1 | [SCA Heritage Coffee Standards](https://www.sca.coffee/heritage-coffee-standards) | A |
| S2 | [SCA News：UC Davis 水溫研究](https://sca.coffee/sca-news/read/just-published-brewing-temperature-and-the-sensory-profile-of-brewed-coffee) | A |
| S3 | [HARIO Europe：James Hoffmann V60 食譜](https://www.hario-europe.com/blogs/hario-community/v60-ambassadors-james-hoffmann) | B |
| S4 | [Perfect Daily Grind：悶蒸搖或攪](https://perfectdailygrind.com/2025/09/swirl-or-stir-coffee-bloom-best-practices/) | B |
| S5 | [Blue Bottle：如何調整研磨度](https://blog.bluebottlecoffee.com/posts/dialing-in-the-grind) | B |
| S6 | [SCA《25》：水與咖啡酸度](https://sca.coffee/sca-news/25/issue-9/english/water-and-coffee-acidity-how-to-adapt-your-water-for-different-extraction-methods-25-magazine-issue-9) | A |
