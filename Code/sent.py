import pandas as pd
import praw
import RedditScraper as RS
import keyword as k
import sentA

def main(keyDic):
    #return list of sentiments
    returnStrings = [] 

    #makes sentiment analysis class
    analys = sentA.sentiment()

    #saves subreddits to be scraped
    subR = ["wallstreetbets","stocks","StocksAndTrading","Superstonk","hot_stocks","investing","StockMarket"]
    subScore = []

    #saves key words for Tesla
    keys = keyDic

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
            if(x.subR==sub):
                totalScore += float(int(x.pop)) #this gets the total score of all the posts for a subreddit

        for x in relArticles:
            if(x.subR==sub):
                if(totalScore!=0):
                    totalSentiment += ((float(int(x.pop))/totalScore)*x.sentiment) #finds the total sentimetn by taking the averages

        subScore.append(totalSentiment)
        returnStrings.append(str(totalSentiment) + " sub:" + sub) #saves our return strings in the list
    return returnStrings

if __name__ == '__main__':
    main()
