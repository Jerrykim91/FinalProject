# import pymongo
# conn = pymongo.MongoClient('localhost',27017)
# db = conn.get_database("db1") #없으면 db1생성
# table = db.get_collection("exam4") #collection 생성

import pymongo
from pymongo import MongoClient
conn = pymongo.MongoClient('127.0.0.1',27017)
db=conn.get_database('team')
collection = db.get_collection('review')


 
post = { 
"author" : "Mike", 
"text" : "My first blog post!", 
"tags" : ["mongodb", "python", "pymongo"]
}
print(post)
#coll = db.collection
collection.insert_one(post)
# post_id = coll.insert(post)