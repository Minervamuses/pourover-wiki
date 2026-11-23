# 操作紀錄（append-only）

格式：`## [日期] 操作 | 對象`，新紀錄加在最下面。

## [2026-11-23] discuss | 範圍與學習目標
- 與使用者確認：主題＝手沖咖啡；來源由 AI 搜尋；交付＝GitHub＋Pages。
- AI 提案受眾、範圍、LG1–LG3，寫入 `discussion/00-scope.md`。

## [2026-11-23] search | 候選來源篩選
- 搜尋 5 組關鍵字（金杯標準、Hoffmann V60、悶蒸、研磨調整、水質）。
- 收錄 6 篇（A 級 3、B 級 3）。
- 排除（C 級）：field-guides.vercel.app（作者不明，且悶蒸水量寫法與 HARIO 官方食譜不一致）、lamose.com 部落格（電商導購文）、open-exam-prep.com（二手整理）。改採原始出處。

## [2026-11-23] ingest | S1 SCA Heritage Standards
- 新建：extraction、water-quality；更新：overview、water-temperature。
- 發現頁面註明「部分傳承標準可能已失效」→ 加註警語。

## [2026-11-23] ingest | S2 SCA 水溫研究
- 更新：extraction、water-temperature、overview。
- 與 S1／S3 的水溫數字不同 → 建立 conflicts.md（C1）。

## [2026-11-23] ingest | S3 HARIO Hoffmann V60
- 新建：v60-recipe、bloom、pouring-agitation；更新：brew-ratio、water-temperature、grind-size。

## [2026-11-23] ingest | S4 PDG 悶蒸
- 更新：bloom、pouring-agitation、grind-size、troubleshooting。
- 搖 vs. 攪無定論 → conflicts.md（C2）。

## [2026-11-23] ingest | S5 Blue Bottle 研磨調整
- 新建：grind-size、troubleshooting；更新：extraction、water-temperature、overview。

## [2026-11-23] ingest | S6 SCA《25》水與酸度
- 更新：water-quality、brew-ratio、troubleshooting。
- 水質標準版本問題 → conflicts.md（C3）。

## [2026-11-23] lint | 第 1 次 Wiki lint → 5 錯誤
- 3 個真錯誤：brew-ratio、v60-recipe 中「推算出的份量」沒有標依據 → 補「推算自 [S#]」。
- 2 個誤判：連結文字「V60 入門食譜」含數字被當成主張 → 修正 lint 工具（v1.1）。
- 人工複查另發現 water-quality.md 一句無數字主張漏引用（lint 規則抓不到）→ 補 [S3]。

## [2026-11-23] lint | 第 2 次 Wiki lint → 0 錯誤
- Wiki 可作為簡報知識來源。

## [2026-11-23] query | 簡報規劃
- 依 LG1–LG3 從 index 挑頁，產出 `workflow/slide-plan.md`（18 張，每張對應 Wiki 頁＋來源）。

## [2026-11-23] generate+check | 簡報 v1 → 檢查 → 修正
- 簡報檢查第 1 輪：1 錯誤。第 14 張出現 Wiki 沒有的「3:30」（生成節點憑模型記憶補入）→ 刪除，記錄 conflicts C4。
- 同時發現檢查工具 bug：封面（class="slide cover"）沒被抓到，只檢查了 17 張 → 修正 regex。
- 第 2 輪：0 錯誤。截圖人工審查：修 3 個版面問題；並抓到第 12 張「結果可能又酸又苦」是 Wiki 沒有的推論（無數字，自動檢查抓不到）→ 改回 Wiki 原意。

## [2026-11-23] workflow | v1 → v2：檢查前移
- 新增 `tools/check_plan.py`：生成前就比對每張投影片要用的數字。
- 回歸測試：把 3:30 放回計畫，v2 在規劃階段即擋下。

## [2026-11-23] lint | 第 3 次 Wiki lint → 1 錯誤 → 修正
- 新增 conflicts C4 時，描述「3:30」的那一行本身沒有引用 → lint 擋下 → 改寫並引用 [S3]。（規則對維護者自己也有效）
