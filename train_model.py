import os
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

from utils.preprocessing import clean_text

# Load Dataset
df = pd.read_csv("dataset/twitter_sentiment.csv")

print("Dataset Loaded Successfully")
print(df.head())

# Check columns
print("Columns:", df.columns.tolist())

# Clean text
df["text"] = df["text"].astype(str)
df["text"] = df["text"].apply(clean_text)

# Features & Labels
X = df["text"]
y = df["sentiment"]

print("\nLabel Counts:")
print(y.value_counts())

# TF-IDF
tfidf = TfidfVectorizer(max_features=5000)
X = tfidf.fit_transform(X)

# Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Model
model = LogisticRegression(max_iter=1000)

model.fit(X_train, y_train)

# Prediction
pred = model.predict(X_test)

accuracy = accuracy_score(y_test, pred)

print(f"\nAccuracy: {accuracy:.4f}")

# Create model folder
os.makedirs("model", exist_ok=True)

# Save model
joblib.dump(model, "model/sentiment_model.pkl")
joblib.dump(tfidf, "model/tfidf.pkl")

print("\nModel Saved Successfully!")