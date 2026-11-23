# 00 先討論：範圍與目標（Discuss before Generate）

> 依「先討論、後生成」原則，生成任何 Wiki 頁面前，先確認以下決定。
> 這份紀錄是 Wiki 的「設計契約」，後續 ingest、query、lint 都以它為準。

## 討論中已確定的決定

| 問題 | 決定 | 由誰決定 |
|---|---|---|
| 主題 | 手沖咖啡（pour-over coffee） | 使用者 |
| 資料來源 | 由 AI 上網搜尋，至少 5 篇，優先官方／研究來源 | 使用者授權 AI |
| 成果交付 | GitHub repo（Wiki）＋ GitHub Pages（簡報） | 使用者 |
| 目標受眾 | 完全沒手沖過、但想在家沖一杯不酸不苦咖啡的初學者 | AI 提案 |
| 範圍內 | 萃取概念、粉水比、研磨度、水溫、悶蒸、注水、水質、風味診斷、一份入門食譜 | AI 提案 |
| 範圍外 | 咖啡產地／品種、烘焙學、義式濃縮、器材採購推薦 | AI 提案 |

## 學習目標（簡報驗收標準）

看完簡報，初學者應能：

- **LG1**：用自己的話說明「萃取」是什麼，以及為什麼咖啡會太酸或太苦。
- **LG2**：說出手沖最重要的幾個變因（粉水比、研磨度、水溫、注水／悶蒸、水質），並知道每個變因會怎麼影響結果。
- **LG3**：照著一份入門食譜沖出第一杯，並能依味道「一次調一個變因」修正。

## 來源篩選規則

- A 級：官方標準或研究（SCA、大學研究）→ 數字類主張優先採用
- B 級：知名器材商／烘豆商／業界媒體（HARIO、Blue Bottle、Perfect Daily Grind）→ 技術與經驗類主張
- C 級：個人部落格、電商文章、二手整理 → 只作線索，不 ingest
- 兩個來源數字不一致時，**不得擅自選一個**，要記錄到 `wiki/conflicts.md`

## Wiki 頁面草案（討論後才生成）

overview → extraction → brew-ratio / grind-size / water-temperature / bloom / pouring-agitation / water-quality → v60-recipe → troubleshooting → conflicts
