from flask import *
from pymongo import MongoClient
import requests

app = Flask(__name__)

def query():
    client = MongoClient('localhost', 27017)
    #db = client['BigDataTwitter']
    db = client.BigDataTwitter
    collection = db.data
    return collection

@app.route('/')
def index():
    # = query().find_one()
    Tweet = []
    Count = {}
    Count["nbrAbonner"] = query().find().count()
    yo = query().find({},{"name":1,"date":1, "_id":0})
    for element in yo:
        print(element)
        if "date" in element :
            Tweet.append(element)
        Count["nbrTweet"] = len(Tweet)
    return render_template("Home.html",Tweet=Tweet,Count=Count)

if __name__== '__main__':
    app.run(debug=True)

