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

    Tweet = [] # Table des tweets
    tabData = {}
    tabDataPays = {}
    Count = {} # liste des différents count (nbr tweet + nbr abonnée + ....)
#    test = 0;

#    Count["nbrAbonner"] = query().find().count()

#    DataDate = query().find({},{"date":1, "_id":0})
#    for element in DataDate :
#        tabData.append(str(element["date"]).split(" ")[0])
#        tabData = list(set(tabData))
#  ElementMoyenne = [query().find({"date" : {"$regex": element}}).count() for element in tabData]
# for element in ElementMoyenne :
# test = test+element
#    print(test / len(ElementMoyenne))
#    print(str(maintenant).split(" ")[0])

    #DataDate = list(set(DataDate))
    followersCount = query().find({},{"followers_count" : 1})
    Count["nbrPeopleToucher"] = 0
    for element in followersCount :
        Count["nbrPeopleToucher"]= int(Count["nbrPeopleToucher"]) + int(element["followers_count"])

    DataDate = query().find({}, {"tweetos": 1, "_id": 0})
    for element in DataDate :
        if(element["tweetos"] in  tabData):
            tabData[element["tweetos"]] = tabData[element["tweetos"]]+1
        else :
            tabData[element["tweetos"]] = 1

    DataPays = query().find({}, {"location": 1, "_id": 0})
    for element in DataPays:
        if (element["location"] in tabDataPays):
            tabDataPays[element["location"]] = tabDataPays[element["location"]] + 1
        else:
            tabDataPays[element["location"]] = 1
    print(tabDataPays)
    yo = query().find({},{"retweet":1,"tweet":1,"tweetos":1,"date":1, "_id":0})
    for element in yo:
        Tweet.append(element)

    Count["nbrPaysTweet"] = len(tabDataPays)
    Count["nbrPeopleTweet"] = len(tabData)
    Count["nbrTweet"] = len(Tweet)
    return render_template("Home.html",Tweet=Tweet,Count=Count,tabData=tabData,tabDataPays=tabDataPays)

if __name__== '__main__':
    app.run(debug=True)

