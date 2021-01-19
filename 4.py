import couchdb
from pymongo import MongoClient
import json 
import requests
URL = 'http://eadmin:eagila926@localhost:5984'
print(URL)
try:
    response = requests.get(URL)
    if response.status_code == 200:
        print('CouchDB conection failed: Success')
    if response.status_code ==401:
        print('Couch connection: failed',response.json())
except requests.ConnectionError as e:
    raise e
    
server=couchdb.Server(URL)
HEADERS = {
    'Accept':'application/json',
    'Content-Type':'application/json'
}

CLIENT = MongoClient('mongodb://localhost:27017')

try:
    CLIENT.admin.command('ismaster')
    print('MongoDB connection: Success')
except ConnectionFailure as cf:
    print('MongoDB connection: failed',cf)

db = server['prueba_p1']

for docid in db.view('_all_docs'):
    try:
        id=docid['id']
        data=db[id]
        print (data)
        CLIENT.prueba_p1.col_couch_mongo.insert(data)
    except Exception as e:
        raise e