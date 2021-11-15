#Ryan Songcuan
#11/14/21
#Module 5.3 Assignment

from pymongo import MongoClient
url="mongodb+srv://admin:admin@cluster0.uwg0x.mongodb.net/myFirstDatabase?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE"
client = MongoClient(url)
db = client.pytech

docs = db.students.find({})
for doc in docs:
	print(doc)

doc = db.students.find_one({'student_id': 1007})
print(doc)