from flask import *
from pymongo import MongoClient
import requests

app = Flask(__name__)

def query():
    client = MongoClient('localhost', 27017)
    db = client['BigDataTwitter']
    return db['data']

@app.route('/')
def index():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
