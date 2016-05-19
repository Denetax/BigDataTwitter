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
    Count = query().count()
    for element in query().find({},{"name":1,"date":1, "_id":0}):
        if element != {}:
            Tweet.append(element)
    return render_template("Home.html",Tweet=Tweet,Count=Count)

if __name__== '__main__':
    app.run(debug=True)