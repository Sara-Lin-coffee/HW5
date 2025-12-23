import os
import streamlit as st

st.set_page_config(page_title="Q3 PPT Redesign (MVP)", page_icon="🖼️", layout="centered")
st.title("🖼️ Q3 — PPT 換版型（MVP）")
st.caption("作業最低需求：輸出至少兩種不同風格的新 PPT。此 MVP 直接提供兩份成品下載。")

ASSET_A = os.path.join("q3_ppt_redesign", "assets", "HW5_Q3_StyleA_MinimalTech.pptx")
ASSET_B = os.path.join("q3_ppt_redesign", "assets", "HW5_Q3_StyleB_AcademicClean.pptx")

st.subheader("下載兩種風格 PPT")
col1, col2 = st.columns(2)

with col1:
    with open(ASSET_A, "rb") as f:
        st.download_button(
            "⬇️ 下載 Style A（Minimal Tech）",
            data=f,
            file_name="HW5_Q3_StyleA_MinimalTech.pptx",
            mime="application/vnd.openxmlformats-officedocument.presentationml.presentation",
            use_container_width=True
        )

with col2:
    with open(ASSET_B, "rb") as f:
        st.download_button(
            "⬇️ 下載 Style B（Academic Clean）",
            data=f,
            file_name="HW5_Q3_StyleB_AcademicClean.pptx",
            mime="application/vnd.openxmlformats-officedocument.presentationml.presentation",
            use_container_width=True
        )

with st.expander("我之後想升級成『上傳 PPT → 自動換版』怎麼做？"):
    st.write(
        "MVP 先交兩份風格成品最穩。要自動換版可用 python-pptx 讀入既有 PPT，"
        "逐頁重建 layout（標題、內文、圖片位置），再套用兩套樣式參數輸出。"
    )
