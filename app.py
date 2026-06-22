from flask import Flask
from flask import render_template
from flask import request
import sqlite3
import joblib

from utils.preprocessing import clean_text

app = Flask(__name__)

model = joblib.load(
    "model/sentiment_model.pkl"
)

tfidf = joblib.load(
    "model/tfidf.pkl"
)

history = []

@app.route("/")
def home():

    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    text = request.form["text"]

    cleaned_text = clean_text(text)

    vector = tfidf.transform([cleaned_text])

    prediction = model.predict(vector)[0]

    probability = model.predict_proba(vector)

    confidence = round(
        max(probability[0]) * 100,
        2
    )

    # Save Prediction in Database

    conn = sqlite3.connect("database/sentiment.db")

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO history(text, sentiment)
        VALUES(?, ?)
        """,
        (text, prediction)
    )

    conn.commit()
    conn.close()

    return render_template(
        "result.html",
        text=text,
        prediction=prediction,
        confidence=confidence
    )
    
@app.route("/dashboard")
def dashboard():

    conn = sqlite3.connect("database/sentiment.db")
    cursor = conn.cursor()

    # Counts

    cursor.execute("SELECT COUNT(*) FROM history")
    total = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM history WHERE sentiment='positive'"
    )
    positive = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM history WHERE sentiment='negative'"
    )
    negative = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM history WHERE sentiment='neutral'"
    )
    neutral = cursor.fetchone()[0]

    # Recent Predictions

    cursor.execute("""
        SELECT id, text, sentiment, created_at
        FROM history
        ORDER BY id DESC
        LIMIT 10
    """)

    recent_predictions = cursor.fetchall()

    conn.close()

    return render_template(
        "dashboard.html",
        total=total,
        positive=positive,
        negative=negative,
        neutral=neutral,
        recent_predictions=recent_predictions
    )
@app.route("/analyze")
def analyze():
    return render_template("analyze.html")

@app.route("/history")
def history():

    conn = sqlite3.connect("database/sentiment.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM history
        ORDER BY id DESC
    """)

    records = cursor.fetchall()

    conn.close()

    return render_template(
        "history.html",
        history=records
    )
    
@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        conn = sqlite3.connect("database/sentiment.db")
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO users(username,email,password)
            VALUES(?,?,?)
            """,
            (username,email,password)
        )

        conn.commit()
        conn.close()

        return redirect("/login")

    return render_template("register.html")

@app.route("/login", methods=["GET","POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        conn = sqlite3.connect("database/sentiment.db")
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM users
            WHERE email=? AND password=?
            """,
            (email,password)
        )

        user = cursor.fetchone()

        conn.close()

        if user:

            session["user_id"] = user[0]
            session["username"] = user[1]

            return redirect("/")

    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)