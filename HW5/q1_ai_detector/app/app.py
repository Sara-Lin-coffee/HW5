import os
import joblib
import numpy as np
import streamlit as st


st.set_page_config(page_title="Q1 AI/Human Detector (MVP)", page_icon="🧪", layout="centered")
st.title("🧪 Q1 — AI / Human 文章偵測器（MVP）")

MODEL_PATH = os.getenv("MODEL_PATH", "model/ai_detector.joblib")

@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)

model = load_model()

text = st.text_area("請貼上一段文字（建議 20 字以上）", height=180, placeholder="在這裡貼上文字...")

col1, col2 = st.columns([1, 1])
with col1:
    run = st.button("立即偵測", use_container_width=True)
with col2:
    st.caption("📌 MVP：TF-IDF + Logistic Regression（字元 n-gram）")

def clamp01(x: float) -> float:
    return float(max(0.0, min(1.0, x)))

if run:
    if not text or len(text.strip()) < 10:
        st.warning("文字太短了～再貼長一點會比較準（至少 10 字）。")
    else:
        proba = model.predict_proba([text])[0]
        # 取出 ai / human 類別對應的 index
        classes = list(model.classes_)
        ai_idx = classes.index("ai") if "ai" in classes else int(np.argmax(proba))
        human_idx = classes.index("human") if "human" in classes else int(np.argmin(proba))

        ai_p = clamp01(proba[ai_idx])
        human_p = clamp01(proba[human_idx])

        st.subheader("判斷結果")
        st.metric("AI %", f"{ai_p*100:.1f}%")
        st.metric("Human %", f"{human_p*100:.1f}%")

        st.progress(ai_p)

        with st.expander("怎麼做的？（MVP 說明）"):
            st.write(
                "用字元 n-gram 的 TF-IDF 把文字轉成特徵，"
                "再用 Logistic Regression 做二分類。"
                "這種做法部署簡單、速度快，很適合作業 MVP。"
            )
