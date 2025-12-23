import os
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score

DATA_PATH = os.getenv("DATA_PATH", "data/ai_human_zh_synth.csv")
OUT_DIR = os.getenv("OUT_DIR", "model")
os.makedirs(OUT_DIR, exist_ok=True)

def main():
    df = pd.read_csv(DATA_PATH)
    df = df.dropna(subset=["text", "label"])
    X = df["text"].astype(str).tolist()
    y = df["label"].astype(str).tolist()

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    clf = Pipeline([
        ("tfidf", TfidfVectorizer(
            analyzer="char",
            ngram_range=(2, 5),
            min_df=2,
            max_features=50000
        )),
        ("lr", LogisticRegression(
            max_iter=2000,
            class_weight="balanced",
            n_jobs=None
        ))
    ])

    clf.fit(X_train, y_train)
    pred = clf.predict(X_test)

    acc = accuracy_score(y_test, pred)
    print(f"Accuracy: {acc:.4f}")
    print(classification_report(y_test, pred))

    joblib.dump(clf, os.path.join(OUT_DIR, "ai_detector.joblib"))
    print("Saved:", os.path.join(OUT_DIR, "ai_detector.joblib"))

if __name__ == "__main__":
    main()
