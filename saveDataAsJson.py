from googlenewsapi import GoogleNewsMethods
import pandas as pd
import datetime 
import json
today = datetime.date.today();

class JsonOperations():
    def __init__(self,dataInput):
        self.dataInput = pd.DataFrame(dataInput)
        #self.dataInput = dataInput
    
    def saveAsJson(self):
        jsonData = self.dataInput.to_json(orient="table")
        parsed = json.loads(jsonData)
        with open('data.txt', 'w') as outfile:
            json.dump(parsed,outfile,indent=4)

if __name__ == "__main__":
    news = GoogleNewsMethods()
    
    op = JsonOperations(news.newscollection("APPL",today))

    op.saveAsJson()