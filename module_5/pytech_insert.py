#Ryan Songcuan
#11/14/21
#Module 5.3 Assignment

from pymongo import MongoClient
url="mongodb+srv://admin:admin@cluster0.uwg0x.mongodb.net/myFirstDatabase?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE"
client = MongoClient(url)
db = client.pytech
# by following the students.insert_one().inserted_id I kept getting the error that "students" was not defined, so I added the fields below to make it work while matching your format
collection = db.students
students = collection


harry = {
	"student_id": 1007,
	"first_name": "Harry",
	"last_name": "Potter"
}

ron = {
	"student_id": 1008,
	"first_name": "Ronald",
	"last_name": "Weasley"
}

hermione = {
	"student_id": 1009,
	"first_name": "Hermione",
	"last_name": "Granger"
}

harry_sudent_id = students.insert_one(harry).inserted_id
ron_sudent_id = students.insert_one(ron).inserted_id
hermione_sudent_id = students.insert_one(hermione).inserted_id

print(harry_sudent_id)
print(ron_sudent_id)
print(hermione_sudent_id)