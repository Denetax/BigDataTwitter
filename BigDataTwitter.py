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
    print(query().find_one())
    print("poifhjef")
    return render_template("Home.html")

if __name__== '__main__':
    app.run(debug=True)