from pymongo import MongoClient

url = "mongodb://35.195.35.203:27017"
db = MongoClient(url).tweetstock
news = db['news']

# get 2 news and print them
nw= news.find().limit(2)
for n in nw:
    print "==============="
    print n['text']
