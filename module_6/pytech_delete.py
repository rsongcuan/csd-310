#Ryan Songcuan
#11/21/21
#Module 6.3 Assignment

from pymongo import MongoClient
url="mongodb+srv://admin:admin@cluster0.uwg0x.mongodb.net/myFirstDatabase?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE"
client = MongoClient(url)
db = client.pytech
collection = db.students

for x in collection.find():
    print(x)

neville = {
	"student_id": 1010,
	"first_name": "Neville",
	"last_name": "Longbottom"
}

neville_student_id = collection.insert_one(neville).inserted_id

y = collection.find_one( { "student_id": 1010 })
print(y)
collection.delete_one({"student_id": 1010 })

for x in collection.find():
    print(x)