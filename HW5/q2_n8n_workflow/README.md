# Q2 — n8n 自動化流程（MVP）

## 你會得到什麼
- `workflow.json`: n8n workflow（Webhook → Set Input → OpenAI Summary）
- `app.py`: Streamlit UI（把文字送到 webhook）

## n8n 設定步驟（最短版）
1. n8n 匯入 `workflow.json`
2. 在 OpenAI 節點設定你的 OpenAI credential（把 `YOUR_CREDENTIAL_ID` 換成你的 credential）
3. 啟用 workflow
4. 複製 Webhook URL（Test/Production 都可，建議 Production）

## Streamlit Cloud
- App path: `q2_n8n_workflow/app.py`
- Requirements: `q2_n8n_workflow/requirements.txt`
- Secrets / Env: `N8N_WEBHOOK_URL=<你的 webhook URL>`
