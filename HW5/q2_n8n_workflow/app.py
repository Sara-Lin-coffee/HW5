import os
import requests
import streamlit as st

st.set_page_config(page_title="Q2 n8n Workflow Demo (MVP)", page_icon="⚙️", layout="centered")
st.title("⚙️ Q2 — n8n 自動化流程（MVP）")
st.caption("Streamlit → 呼叫 n8n Webhook → n8n 用 OpenAI 做摘要 → 回傳結果")

WEBHOOK_URL = os.getenv("N8N_WEBHOOK_URL", "")

if not WEBHOOK_URL:
    st.warning("請先在 Streamlit Cloud 設定環境變數 `N8N_WEBHOOK_URL`（你的 n8n Webhook URL）。")

text = st.text_area("輸入要摘要的內容", height=200, placeholder="貼上一段文章或筆記...")

if st.button("送出摘要", use_container_width=True):
    if not WEBHOOK_URL:
        st.error("缺少 N8N_WEBHOOK_URL。")
    elif not text.strip():
        st.warning("內容空的喔～貼點文字再試試。")
    else:
        try:
            r = requests.post(WEBHOOK_URL, json={"text": text}, timeout=60)
            r.raise_for_status()
            st.subheader("摘要結果")
            # n8n OpenAI node 的回傳格式可能因版本不同而異，這裡做容錯處理
            data = r.json() if "application/json" in r.headers.get("content-type", "") else {"raw": r.text}
            st.json(data)
        except Exception as e:
            st.error(f"呼叫失敗：{e}")
            st.info("檢查：n8n workflow 是否已啟用、Webhook 是否可公開連線、以及 OpenAI credential 是否設定完成。")
