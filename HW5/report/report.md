# HW5 報告（MVP）

> 你可以直接把這份 Markdown 匯出成 PDF（例如用 VSCode/Typora/Obsidian 或 Pandoc）。

## 共同要求
- GitHub Repo：包含程式碼、workflow、PPT 檔案
- Streamlit Demo：Q1/Q2/Q3 各一個可運作連結
- ChatGPT / AI Agent 對話紀錄：可附在附錄（本次對話即可）

---

## Q1 — AI / Human 文章偵測器（AI Detector）
### 目標
輸入一段文字 → 輸出 AI% / Human%

### 方法（MVP）
- TF-IDF（字元 n-gram）+ Logistic Regression
- 優點：速度快、部署簡單、作業展示穩定

### 執行步驟
1. `python train.py` 產生模型 `model/ai_detector.joblib`
2. `streamlit run app/app.py` 啟動 UI

### 結果截圖（自行貼）
- （貼 Streamlit 畫面）

---

## Q2 — n8n 自動化流程（仿小林 AI）
### 目標
Streamlit 送出文字 → n8n workflow 用 OpenAI 做摘要 → 回傳結果

### Workflow（MVP）
- Webhook Trigger → Set Input → OpenAI Summary → Response

### 執行步驟
1. n8n 匯入 `workflow.json`
2. 設定 OpenAI credential
3. 啟用 workflow 並取得 Webhook URL
4. Streamlit 設定環境變數 `N8N_WEBHOOK_URL`

### 結果截圖（自行貼）
- （貼 n8n workflow 畫面）
- （貼 Streamlit 回傳結果）

---

## Q3 — PPT 換版型（AI 重新設計）
### 目標
輸出至少兩種不同風格的新 PPT

### 作法（MVP）
- 使用 python-pptx 直接生成兩種風格的簡報成品（Style A / Style B）
- Streamlit 提供下載

### 成品
- `assets/HW5_Q3_StyleA_MinimalTech.pptx`
- `assets/HW5_Q3_StyleB_AcademicClean.pptx`

---

## 附錄 A：ChatGPT 對話紀錄
- 直接附上本次對話截圖或匯出 PDF/Markdown 即可。
