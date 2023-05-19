import nltk
import numpy
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from transformers import pipeline

class sentiment: #uses vader lexicon to anylis text with Nltk
    def __init__(this):
        nltk.download('all')
        this.sid = SentimentIntensityAnalyzer()
    def oldAnalysis(this,text):
        #tokenizes
        tokens = word_tokenize(text.lower())
        #removes stop words
        tokens = [token for token in tokens if token not in stopwords.words('english')]
        #lemmatizes
        lem = WordNetLemmatizer()
        lemTokens = [lem.lemmatize(token) for token in tokens]
        #creates new string
        newText = ' '.join(tokens)
        print(newText)
        #gets score
        return this.sid.polarity_scores(newText)['compound']
    def analysis(this,text): #analysis using hugging face models
        sentiment_pipeline = pipeline(model="zhayunduo/roberta-base-stocktwits-finetuned")
        analysis = sentiment_pipeline(text)
        print(analysis)
        if (analysis)[0]['label']=='Negative':
            analysis[0]['score'] = -2*(analysis[0]['score']-0.5)
        else:
            analysis[0]['score'] = 2*(analysis[0]['score']-0.5)
        return analysis[0]['score']