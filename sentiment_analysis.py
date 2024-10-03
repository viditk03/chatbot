# sentiment_analysis.py

from langdetect import detect
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from indic_transliteration import sanscript
import nltk

try:
    nltk.data.find('vader_lexicon')
except LookupError:
    nltk.download('vader_lexicon')
    
# Load the sentiment analysis model
sia = SentimentIntensityAnalyzer()

def get_sentiment(text, lang):
    # Perform language-specific sentiment analysis
    if lang == 'hi':  # Hindi
        # Transliterate Hinglish text to Devanagari script
        text = sanscript.transliterate(text, sanscript.HK, sanscript.DEVANAGARI)

    # Perform sentiment analysis
    sentiment_scores = sia.polarity_scores(text)

    # Determine sentiment classification
    if sentiment_scores['compound'] >= 0.05:
        sentiment_classification = 'positive'
    elif sentiment_scores['compound'] <= -0.05:
        sentiment_classification = 'negative'
    else:
        sentiment_classification = 'neutral'

    # Return both sentiment scores and classification
    return {
        'sentiment_scores': sentiment_scores,
        'sentiment_classification': sentiment_classification
    }   