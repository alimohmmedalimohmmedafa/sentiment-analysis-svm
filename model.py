import json
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC

# تنظيف النص
def clean_text(text):
    return re.sub(r"[^\w\s]", "", text)

# تحميل البيانات
with open("sentiment_dataset.json", "r", encoding="utf-8") as f:
    data = json.load(f)

texts = [clean_text(item["text"]) for item in data]
labels = [item["label"] for item in data]

# تحويل النصوص إلى أرقام
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)

# تدريب نموذج SVM
model = LinearSVC()
model.fit(X, labels)

# دالة التنبؤ
def predict_sentiment(text):
    text = clean_text(text)
    vector = vectorizer.transform([text])
    return model.predict(vector)[0]
