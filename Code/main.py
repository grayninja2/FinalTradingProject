import pandas as pd
import praw
import RedditScraper as RS
import keyword as k

#saves subreddits to be scraped
subR = ["stocks"]

#saves key words for Tesla
keyTesla = {"Tesla ":1,"TSLA ":1, " Tech ":0.2, "Electric Car":0.5, "Elon Musk":0.8, "Musk ":0.8, "Battery ":0.1, "Self Driving ":0.5, "Car ":0.1, "SpaceX ":0.8}

#master dictionary of keywords
keys = {"Tesla":keyTesla}

#saves articles with keywords
relArticles = list()

#scrapes all subreddits
for sub in subR:
    scraperR = RS.RedditScraper(list(keys["Tesla"].keys()),sub)
    scraperR.scrape()
    
    for x in scraperR.articles:
        relArticles.append(x) #adds all articles

for x in relArticles:
    print(x.title)

