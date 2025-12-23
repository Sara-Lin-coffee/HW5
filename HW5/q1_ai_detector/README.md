# Q1 — AI / Human 文章偵測器（MVP）

## 內容
- `train.py`: 訓練 TF-IDF (char n-gram) + Logistic Regression
- `app/app.py`: Streamlit UI
- `data/ai_human_zh_synth.csv`: 合成資料集（作業用 MVP）
- `model/ai_detector.joblib`: 訓練完成後產生

## 本機執行
```bash
cd q1_ai_detector
pip install -r requirements.txt
python train.py
streamlit run app/app.py
```

## Streamlit Cloud
- App path: `q1_ai_detector/app/app.py`
- Python requirements: `q1_ai_detector/requirements.txt`
