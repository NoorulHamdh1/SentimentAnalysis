# Sentiment Analysis Web App

A Flask-based web application that performs sentiment analysis using the TextBlob Natural Language Processing library. The application classifies user text as Positive, Negative, or Neutral while displaying polarity and subjectivity scores through a clean and modern interface.

## Features

- Positive, Negative and Neutral sentiment detection
- Polarity score analysis
- Subjectivity score analysis
- Analysis history
- Responsive minimal UI
- Built using Flask and TextBlob

## Technologies Used

- Python
- Flask
- TextBlob
- HTML
- CSS

## Project Structure

```
SentimentAnalysis/

├── app.py
├── history.json
├── requirements.txt
├── templates/
│ └── index.html
├── static/
│ └── style.css
└── README.md
```

## Installation

```bash
pip install flask textblob
python -m textblob.download_corpora
```

Run

```bash
python app.py
```

Open

```
http://127.0.0.1:5000
```

## Example

Input

```
I absolutely love learning Python.
```

Output

```
Sentiment: Positive

Polarity: 0.65

Subjectivity: 0.72
```

## Future Improvements

- Emotion classification
- Multiple language support
- Sentiment visualization charts
- User authentication
- Export analysis history
