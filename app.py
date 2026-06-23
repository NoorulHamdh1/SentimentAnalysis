from flask import Flask, render_template, request
from textblob import TextBlob
import json
import os

app = Flask(__name__)

HISTORY_FILE = "history.json"


def load_history():

    if os.path.exists(HISTORY_FILE):

        with open(HISTORY_FILE, "r") as file:
            return json.load(file)

    return []


def save_history(data):

    history = load_history()

    history.insert(0, data)

    history = history[:5]

    with open(HISTORY_FILE, "w") as file:
        json.dump(history, file, indent=4)


@app.route("/", methods=["GET", "POST"])
def home():

    sentiment = None
    polarity = None
    subjectivity = None
    text_input = ""

    if request.method == "POST":

        text_input = request.form["text"]

        analysis = TextBlob(text_input)

        polarity = round(
            analysis.sentiment.polarity,
            3
        )

        subjectivity = round(
            analysis.sentiment.subjectivity,
            3
        )

        if polarity > 0:
            sentiment = "Positive 😊"

        elif polarity < 0:
            sentiment = "Negative 😡"

        else:
            sentiment = "Neutral 😐"

        save_history({
            "text": text_input,
            "sentiment": sentiment,
            "polarity": polarity,
            "subjectivity": subjectivity
        })

    history = load_history()

    return render_template(
        "index.html",
        sentiment=sentiment,
        polarity=polarity,
        subjectivity=subjectivity,
        text_input=text_input,
        history=history
    )


if __name__ == "__main__":
    app.run(debug=True)