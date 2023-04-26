import pandas as pd
import praw
import RedditScraper as RS

scraperR = RS.RedditScraper("Tesla")

titles = list()

for a in scraperR.articles:
    if a.title.find("Tesla")!=-1:
        titles.add(a.title)

print(titles)

