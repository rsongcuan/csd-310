#Ryan Songcuan
#11/21/21
#Module 6.2 Assignment

from pymongo import MongoClient
url="mongodb+srv://admin:admin@cluster0.uwg0x.mongodb.net/myFirstDatabase?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE"
client = MongoClient(url)
db = client.pytech
collection = db.students

for x in collection.find():
    print(x)

filter = { "student_id": 1007}
newvalues = { "$set": { "last_name": "Potter, Jr."} }

collection.update_one(filter, newvalues)

y = collection.find_one()
print(y)