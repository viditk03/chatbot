from flask import Flask, render_template, request
from sentiment_analysis import get_sentiment
import langid

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def hello():
    if request.method == "GET":
        text = request.args.get("text")
    elif request.method == "POST":
        text = request.form["text"]
    else:
        return ({"error": "Unsupported request method"}), 405

    if text is None:
        return ({"error": "Text is required"}), 400

    # Detect the language of the input text
    lang, confidence = langid.classify(text)

    # Perform sentiment analysis and get the full sentiment result
    sentiment_result = get_sentiment(text, lang)

    # Render results as an HTML table using the template, passing the full sentiment result
    return render_template(
        "results.html",
        text=text,
        language=lang,
        sentiment=sentiment_result['sentiment_classification'],
        sentiment_scores=sentiment_result['sentiment_scores']
    )

if __name__ == "__main__":
    app.run()