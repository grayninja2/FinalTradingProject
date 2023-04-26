class Article:
    def __init__(self, title, date, text, pop, popPercent, source):
        self.title = title #saves title of article
        self.date = date #saves date of article in hours after 2000
        self.text = text #saves text in a string
        self.pop = pop #saves a number for the popularity
        self.source = source #saves url of source