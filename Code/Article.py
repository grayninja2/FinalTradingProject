class Article:
    def __init__(self, date, text, pop, source):
        self.date = date #saves date of article in hours after 2000
        self.text = text #saves text in a string
        self.pop = pop #saves a number for the popularity
        self.source = source #saves url of source