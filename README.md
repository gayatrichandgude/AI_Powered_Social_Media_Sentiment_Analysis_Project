# 🧠 AI_Powered_Social_Media_Sentiment_Analysis_Project

An AI-powered web application that analyzes social media posts, tweets, reviews, and comments to determine their sentiment using Natural Language Processing (NLP) and Machine Learning techniques.

The system classifies text into:

* 😊 Positive
* 😞 Negative
* 😐 Neutral

Built using Flask, Scikit-Learn, NLTK, TF-IDF Vectorization, Logistic Regression, and SQLite Database.

---

# 🚀 Features

### 🔍 Sentiment Analysis

* Analyze tweets, reviews, comments, and social media posts.
* Predict sentiment in real-time.
* Supports Positive, Negative, and Neutral classifications.

### 🧠 NLP Processing

* Text Cleaning
* Lowercase Conversion
* URL Removal
* Special Character Removal
* Tokenization
* Stopword Removal

### 🤖 Machine Learning

* TF-IDF Vectorization
* Logistic Regression Classifier
* Scikit-Learn Based Model

### 📊 Analytics Dashboard

* Total Predictions Count
* Positive Sentiment Count
* Negative Sentiment Count
* Neutral Sentiment Count
* Pie Chart Visualization
* Bar Chart Visualization
* Recent Predictions Table

### 📜 Prediction History

* Stores all predictions in SQLite Database
* Displays complete prediction history
* Search functionality for records


### 🎨 Modern  Interface

* Responsive Design
* Professional Dashboard
* Interactive Charts
* Attractive Landing Page

---

# 🛠️ Technology Stack

## Frontend

* HTML5
* CSS3
* JavaScript
* Chart.js

## Backend

* Flask

## Machine Learning

* Scikit-Learn
* Logistic Regression
* TF-IDF Vectorizer

## Natural Language Processing

* NLTK

## Database

* SQLite

## Programming Language

* Python

---

## 📂 Project Structure

```text
AI_Powered_Social_Media_Sentiment_Analysis_Project
│
├── dataset
│   └── twitter_sentiment.csv
│
├── database
│   └── sentiment.db
│
├── model
│   ├── sentiment_model.pkl
│   └── tfidf.pkl
│
├── static
│   ├── style.css
│   ├── analyze.css
│   ├── dashboard.css
│   ├── history.css
│   └── result.css
│
├── templates
│   ├── index.html
│   ├── analyze.html
│   ├── dashboard.html
│   ├── history.html
│   ├── result.html
│   
│   
│
├── utils
│   └── preprocessing.py
│
├── app.py
├── create_db.py
├── train_model.py
├── requirements.txt
└── README.md
```

# 🗄️ Database Schema

## History Table

| Column     | Type                |
| ---------- | ------------------- |
| id         | INTEGER PRIMARY KEY |
| text       | TEXT                |
| sentiment  | TEXT                |
| created_at | TIMESTAMP           |

---


---

# ⚙️ Installation

## Clone Repository

git clone https://github.com/your-username/AI_Powered_Social_Media_Sentiment_Analysis_Project.git



cd AI_Powered_Social_Media_Sentiment_Analysis_Project


---

## Create Virtual Environment

### Windows


python -m venv venv
venv\Scripts\activate


### Linux / Mac


python3 -m venv venv
source venv/bin/activate


---

## Install Dependencies


pip install -r requirements.txt


---

# 🗄️ Create Database


python create_db.py


---

# 🤖 Train Machine Learning Model


python train_model.py


Generated Files:


model/
├── sentiment_model.pkl
└── tfidf.pkl


---

# ▶️ Run Application

python app.py


Open your browser:


http://127.0.0.1:5000


---

# 🧠 Machine Learning Workflow


Input Text
     │
     ▼
Text Cleaning
     │
     ▼
Tokenization
     │
     ▼
Stopword Removal
     │
     ▼
TF-IDF Vectorization
     │
     ▼
Logistic Regression Model
     │
     ▼
Sentiment Prediction


---

# 📈 Model Information

| Component   | Details                     |
| ----------- | --------------------------- |
| Algorithm   | Logistic Regression         |
| Vectorizer  | TF-IDF                      |
| NLP Library | NLTK                        |
| Classes     | Positive, Negative, Neutral |
| Backend     | Flask                       |
| Database    | SQLite                      |

---

# 📊 Dashboard Analytics

The dashboard provides:

* Total Predictions
* Positive Sentiments
* Negative Sentiments
* Neutral Sentiments
* Sentiment Distribution Chart
* Sentiment Comparison Chart
* Recent Prediction Records

---

# 🎯 Learning Outcomes

This project demonstrates:

* Natural Language Processing (NLP)
* Machine Learning Classification
* Text Vectorization
* Data Cleaning & Preprocessing
* Model Training & Evaluation
* Flask Web Development
* SQLite Database Integration
* Dashboard Development
* User Authentication System

---

# 🔮 Future Enhancements

* Password Hashing
* User-wise Prediction History
* Admin Dashboard
* Export History to CSV
* PDF Report Generation
* Deep Learning Models (LSTM)
* Real-Time Twitter Analysis
* REST API Integration
* Sentiment Trend Analytics

---

# 👩‍💻 Author

**Gayatri Chandgude**

GitHub: https://github.com/gayatri132004

---

# 📜 License

This project is developed for educational and learning purposes.

© 2026 AI_Powered_Social_Media_Sentiment_Analysis_Project. All Rights Reserved.
