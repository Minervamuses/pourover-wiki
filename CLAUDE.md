# Wiki Schema（給 LLM 的維護規則）

這個 repo 是一個「LLM Wiki」：由 LLM 維護、人類審核的知識庫，主題是手沖咖啡。
LLM 每次操作 Wiki 都必須遵守以下規則。

## 三層結構
- `raw/`：來源卡（不可修改的原始依據）。每張卡有 id（S1, S2…）、網址、可信度等級。
- `wiki/`：由 LLM 撰寫的概念頁。人類閱讀、LLM 維護。
- `CLAUDE.md`（本檔）：規則。

## 三種操作
### 1. Ingest（加入一篇新資料）
1. 先和使用者討論這篇資料重點是否在 `discussion/00-scope.md` 的範圍內。
2. 在 `raw/` 建立來源卡（改寫重點，不貼全文）。
3. 更新所有相關的 `wiki/` 頁面（通常 3–6 頁），**不是只新增一頁**。
4. 與既有內容矛盾 → 寫入 `wiki/conflicts.md`，不得默默覆蓋。
5. 更新 `wiki/index.md` 與 `wiki/log.md`。
6. 執行 `python3 tools/lint_wiki.py`，全部通過才算 ingest 完成。

### 2. Query（用 Wiki 回答問題／產生簡報）
- 只能使用 `wiki/` 內容回答；Wiki 沒有的知識要回到 Ingest，不可憑空補。
- 產出物要標註用到哪些 Wiki 頁面與來源 id。

### 3. Lint（健康檢查）
- 每個含數字的主張都要有 `[S#]` 引用。
- 引用的來源必須存在於 `raw/`，且列在頁面 frontmatter 的 `sources`。
- 頁面之間的連結必須有效；每頁都要列在 `index.md`。
- 來源衝突要集中在 `conflicts.md`。

## 頁面格式
```
---
title: 頁面標題
sources: [S1, S3]
updated: YYYY-MM-DD
---
```
引用寫法：句尾加 `[S1]`；頁面互連用相對連結 `[萃取](extraction.md)`。
