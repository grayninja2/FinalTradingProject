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
        for submissions in Agent.reddit.subreddit(this.subR).hot(limit=None): #gets submissions and saves them if they have keywords as a article with their popularity calculated
            for a in this.keywords:
                if submissions.title.lower().find(a.lower())!=-1:
                    pop = math.pow(10,(2-((submissions.upvote_ratio*100)/-50)))*submissions.score
                    this.articles.append(Ar.Article(submissions.title,submissions.created_utc,submissions.selftext,pop,submissions.url))