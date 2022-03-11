import pymongo
from datetime import datetime
client=pymongo.MongoClient('mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false')
db=client['dunderstore']
users=db['customers']
items=db['items']
stores=db['stores']
sessions=db['sessions']
results=items.aggregate([{ "$unwind": "$rating" },{ "$group" : { "_id": "$_id", "avgRating" : {  "$avg" : "$rating.rating" } } }])
a=[]
for result in results:
    a.append(result)
print(a)        