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
    subScore = []

    #saves key words for Tesla
    keys = {"Tesla ":1, "TSLA ":1, "Electric Car":0.2, "Elon Musk":0.5, "Musk ":0.5, "Self Driving ":0.3}

    #saves articles with keywords
    relArticles = list()

    #scrapes all subreddits
    for sub in subR:
        scraperR = RS.RedditScraper(keys,sub)
        scraperR.scrape()
        
        for x in scraperR.articles:
            x.subR = sub
            relArticles.append(x) #adds all articles
        print(sub + " done")

    for art in relArticles:
        art.sentiment = analys.analysis(art.title) #uses sentiment analysis

    for x in relArticles:
        print(x.title + " (" + str(int(x.pop))+") { "+ str(x.sentiment) + " }") #prints articles

    for sub in subR: #finds a sentiment score for a given sub reddit by taking the average sentiment weighted for score
        totalScore = 0
        totalSentiment = 0
        for x in relArticles:
            totalScore += float(int(x.pop))

        for x in relArticles:
            totalSentiment += ((float(int(x.pop))/totalScore)*x.sentiment)

        subScore.append(totalSentiment)
        print(str(totalSentiment) + " sub:" + sub)

if __name__ == '__main__':
    main()
