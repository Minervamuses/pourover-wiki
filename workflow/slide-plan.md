# 簡報規劃（Query 節點產出）

> 由 LLM 讀 `wiki/index.md` → 依學習目標挑頁面 → 產生每張投影片的「內容契約」。
> HTML 中每張投影片都用 `data-wiki`、`data-src`、`data-lg` 標註這份對應，`tools/check_slides.py` 會自動驗證。

| # | 投影片 | 教學目的 | 對應 Wiki 頁 | 來源 | LG |
|---|---|---|---|---|---|
| 1 | 封面：為什麼我沖的咖啡又酸又苦？ | 引起動機 | overview | – | – |
| 2 | 今天學會三件事 | 揭示學習目標 | overview | – | LG1–3 |
| 3 | 手沖在做什麼 | 建立心智模型 | overview, extraction | S2 | LG1 |
| 4 | 萃取的兩個數字 | 認識 TDS／萃取率／金杯 | extraction | S1 | LG1 |
| 5 | 萃取不足 vs. 過度萃取 | 把數字連到味道 | extraction | S5 | LG1 |
| 6 | 研究：終點比路線重要 | 為什麼要看結果不看單一變因 | extraction, water-temperature | S2 | LG1 |
| 7 | 五個旋鈕 | 變因總覽 | overview | – | LG2 |
| 8 | 粉水比＋計算器 | 互動換算 | brew-ratio, bloom | S3, S6, S4 | LG2 |
| 9 | 研磨度 | 最重要的旋鈕、dial in | grind-size | S5 | LG2 |
| 10 | 水溫 | 各家建議＋研究結論 | water-temperature, conflicts | S1, S2, S3, S5 | LG2 |
| 11 | 悶蒸 | 為什麼要悶蒸 | bloom | S3, S4 | LG2 |
| 12 | 注水與擾動 | 通道效應、細粉堵塞 | pouring-agitation | S4 | LG2 |
| 13 | 水質 | 鹼度比 pH 重要 | water-quality | S1, S6 | LG2 |
| 14 | 動手：V60 食譜時間軸 | 可照做的流程 | v60-recipe | S3 | LG3 |
| 15 | 喝了之後：診斷器 | 互動診斷 | troubleshooting | S4, S5, S6 | LG3 |
| 16 | 一次只改一個變因 | 調整迴圈 | troubleshooting, grind-size | S5 | LG3 |
| 17 | 小測驗 | 形成性評量 | extraction, troubleshooting, brew-ratio | S1, S5, S6 | LG1–3 |
| 18 | 總結＋這份簡報怎麼做的 | 收束、指向 Wiki | index | – | – |

## 覆蓋檢查（人工）
- LG1：#3–6、#17 ✔　LG2：#7–13、#17 ✔　LG3：#14–17 ✔
- 每個 Wiki 概念頁都至少被一張投影片使用 ✔（conflicts 由 #10 使用）

## 關鍵數字清單（v2 新增：生成前先驗證）
> 規則：規劃時就列出每張投影片打算用的數字，`tools/check_plan.py` 先比對 Wiki；
> 找不到的數字 → 回到 Ingest 找來源，或從計畫中刪除，**通過後才進入生成**。

- #4 extraction: 1.15%, 1.35%, 18%, 22%
- #6 water-temperature: 87°C, 90°C, 93°C
- #8 brew-ratio: 60 g/L, 16.7, 0.06, 30 g, 500 mL
- #9 grind-size: 1–2 格
- #10 water-temperature: 97°C, 195–205°F, 90.5–96°C, 92°C
- #11 bloom: 2 倍, 3–4 倍, 60 mL, 45 秒
- #13 water-quality: 40 ppm
- #14 v60-recipe: 30 g, 500 mL, 97°C, 60 mL, 45 秒, 0:45, 1:15, 1:45, 300 mL, 15 g, 250 mL
- #17 brew-ratio: 300 mL, 18 g, 0.06
