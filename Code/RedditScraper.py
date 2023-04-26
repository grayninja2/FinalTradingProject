import Article
import praw
import math
import RedditAgent

class RedditScraper:
    def __init__(this,keywords):
        this.keywords = keywords
        this.articles = []
    def scrape(this):
        for submissions in RedditAgent.reddit.subreddit('stocks').hot(limit=None):
            pop = math.pow(10,(2-((submissions.upvote_ratio*100)/-50)))*submissions.score
            this.articles.add(Article(submissions.title,submissions.created_utc,submissions.selftext,pop,submissions.url))