from flask import *
from pymongo import MongoClient
from datetime import datetime

import requests

app = Flask(__name__)

def query():
    client = MongoClient('localhost', 27017)
    #db = client['BigDataTwitter']
    db = client.BigDataTwitter
    collection = db.dataTwitter
    return collection

@app.route('/')
def index():

    Tweet = []
    tabData = []
    Count = {}
    retweet = {}
    test = 0;
    maintenant = datetime.now()
    print(maintenant)
    print(maintenant)

    Count["nbrAbonner"] = query().find().count()
    DataDate = query().find({},{"date":1, "_id":0})
    for element in DataDate :
        tabData.append(str(element["date"]).split(" ")[0])
        tabData = list(set(tabData))
    ElementMoyenne = [query().find({"date" : {"$regex": element}}).count() for element in tabData]
    for element in ElementMoyenne :
        test = test+element
    print(test / len(ElementMoyenne))
    print(str(maintenant).split(" ")[0])
    yo = query().find({},{"retweet":1,"tweet":1,"date":1, "_id":0})
    for element in yo:
        Tweet.append(element)
        Count["nbrTweet"] = len(Tweet)
    #print(maintenant)
    return render_template("Home.html",Tweet=Tweet,Count=Count)

if __name__== '__main__':
    app.run(debug=True)

