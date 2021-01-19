from argparse import ArgumentParser
import requests
import pymongo 
from pymongo.errors import ConnectionFailure
from bson import json_util, ObjectId
import couchdb
import json

client = couchdb.Server('http://eadmin:eagila926@localhost:5984/')

try:
    print('Couch connection: Success')
except ConnectionFailure as e:
    print('Couch connection: Failed', e)
    
HEADERS = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

clientatlas = pymongo.MongoClient("mongodb://ejercicio7:ejer7@cluster0-shard-00-00.mae3c.mongodb.net:27017,cluster0-shard-00-01.mae3c.mongodb.net:27017,cluster0-shard-00-02.mae3c.mongodb.net:27017/<dbname>?ssl=true&replicaSet=atlas-3q4yws-shard-0&authSource=admin&retryWrites=true&w=majority")
Database_m = clientatlas.get_database('ubisoft')
Database_ma =Database_m.sports

try:
    clientatlas.admin.command('ismaster')
    print('MongoDB Atlas connection: Success')
except ConnectionFailure as e:
    print('MongoDB Atlas connection: failed', e)
    
NewDB=client['ubisoft']

for db in DBc:
    try:
        Database_ma.insert_one(DBc[db])
        print('Data saved mongoDB Atlas')
    except TypeError as et:
        print('current document raised error: {}'.format(et))
        SKIPPED.append(db)  # creating list of skipped documents for later analysis
        continue    # continue to next document
    except Exception as e:
        raise e