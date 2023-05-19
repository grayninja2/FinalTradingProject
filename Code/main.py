import pandas as pd
import praw
import RedditScraper as RS
import keyword as k
import sentA

def main():
    #makes sentiment analysis class
    analys = sentA.sentiment()

    #saves subreddits to be scraped
    subR = ["wallstreetbets","stocks","StocksAndTrading","Superstonk","hot_stocks","investing","StockMarket"]

    #saves key words for Tesla
    keyTesla = {"Tesla ":1, "TSLA ":1, "Electric Car":0.2, "Elon Musk":0.5, "Musk ":0.5, "Self Driving ":0.3}

    #master dictionary of keywords
    keys = {"Tesla":keyTesla}

    #saves articles with keywords
    relArticles = list()

    #scrapes all subreddits
    for sub in subR:
        scraperR = RS.RedditScraper(keys["Tesla"],sub)
        scraperR.scrape()
        
        for x in scraperR.articles:
            relArticles.append(x) #adds all articles

    for art in relArticles:
        art.sentiment = analys.analysis(art.title)

    totalScore = 0
    totalSentiment = 0

    for x in relArticles:
        totalScore += float(int(x.pop))

    for x in relArticles:
        print(x.title + " (" + str(int(x.pop))+") { "+ str(x.sentiment) + " }")
        totalSentiment += ((float(int(x.pop))/totalScore)*x.sentiment)

    print(totalSentiment)

if __name__ == '__main__':
    main()
