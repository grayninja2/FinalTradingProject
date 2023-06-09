import Article as Ar
import praw
import math
import Agent

class RedditScraper:
    def __init__(this,keywords,subR):
        this.subR = subR
        this.keywords = keywords #Saves keywords for grabbing relevent articles
        this.articles = [] #saves all articles
    def scrape(this):
        for submissions in Agent.reddit.subreddit(this.subR).new(limit=100): #gets submissions and saves them if they have keywords as a article with their popularity calculated
            max = 0
            for a in this.keywords.keys():
                if submissions.title.lower().find(a.lower())!=-1: #finds keyword in article title
                    keys = list()
                    vals = list()
                    for a in this.keywords.keys(): #makes it so articles dont repeatedly get added
                        if submissions.title.lower().find(a.lower())!=-1:
                            if(not(a in keys)):
                                keys.append(a)
                                vals.append(this.keywords[a])
                    for x in vals:
                        max += x
                    pop = (math.pow(10,(2-((100-(submissions.upvote_ratio*100))/50)))/100)*submissions.score*max #uses a function to make sure higher ratio of upvotes matter more
                    this.articles.append(Ar.Article(submissions.title,submissions.created_utc,submissions.selftext,pop,submissions.url,None)) #appends a new article with all the criteria to list
                    break