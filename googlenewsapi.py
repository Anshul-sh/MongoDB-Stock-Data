from GoogleNews import GoogleNews
import datetime
today = datetime.date.today();

# Creates a googlenews object
class GoogleNewsMethods():
    def __init__(self):    
        self.googlenews = GoogleNews(lang="en")

    def newscollection(self, stock, date):
        self.googlenews.search(stock)
        self.newsList = googlenews.result()
        print (self.newsList)

if __name__ == "__main__":
    news = GoogleNewsMethods()
    news.newscollection("APPL", today)