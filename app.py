from flask import Flask, render_template, request
from textblob import TextBlob
import re
import validators

app = Flask(__name__)

# Suspicious keyword dictionary with weights
FLAGGED_TERMS = {
    "shocking": 5,
    "secret cure": 10,
    "fake news": 8,
    "they don’t want you to know": 7,
    "unverified": 5,
    "miracle": 6,
    "you won’t believe": 4
}

# Trusted domains
TRUSTED_DOMAINS = [".gov", ".edu", "bbc.com", "nytimes.com", "reuters.com"]

def analyze_text(text):
    score = 0
    flagged_words = []
    text_lower = text.lower()

    # Highlighting: wrap suspicious words
    highlighted = text
    for phrase, weight in FLAGGED_TERMS.items():
        if phrase in text_lower:
            score += weight
            flagged_words.append(phrase)
            highlighted = re.sub(
                fr"(?i)({re.escape(phrase)})",
                r'<span class="highlight-danger">\1</span>',
                highlighted
            )

    # Sentiment Analysis
    blob = TextBlob(text)
    subjectivity = blob.sentiment.subjectivity
    polarity = abs(blob.sentiment.polarity)
    score += int(subjectivity * 5 + polarity * 5)

    # Source Check (URLs)
    urls = re.findall(r'(https?://\S+)', text)
    source_status = "No URLs found"
    if urls:
        for url in urls:
            if validators.url(url):
                if any(dom in url for dom in TRUSTED_DOMAINS):
                    source_status = f"Trusted: {url}"
                    score = max(score - 5, 0)
                else:
                    source_status = f"Unverified/Unknown: {url}"
                    score += 10
            else:
                source_status = f"Invalid URL: {url}"
                score += 5

    return {
        "score": min(score, 100),
        "flagged_words": flagged_words,
        "source_status": source_status,
        "highlighted_text": highlighted
    }

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        user_text = request.form.get("user_text", "")
        if user_text.strip():
            result = analyze_text(user_text)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)