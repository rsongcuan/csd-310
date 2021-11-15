# Ryan Songcuan
# 11/14/21
# Module 5.2 Assignment

from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.uwg0x.mongodb.net/myFirstDatabase?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE"
client = MongoClient(url)
db = client.pytech
print(db.list_collection_names())