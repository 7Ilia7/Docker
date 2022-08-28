from pymongo import MongoClient
from pprint import pprint

MONGO_URL = "mongodb://mongo:27017"
clent = MongoClient(MONGO_URL)
db = client.admin
dbs_list = db.comman("listDatabases")
pprint(dbs_list)pprint

print("End")