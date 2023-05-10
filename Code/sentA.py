import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

class sentiment: #uses vader lexicon to anylis text with Nltk
    def __init__(this):
        nltk.download('vader_lexicon')
        this.sid = SentimentIntensityAnalyzer()
    def analysis(this,text):
        return this.sid.polarity_scores(text)['compound']