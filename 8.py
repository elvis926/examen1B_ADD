import json
from argparse import ArgumentParser
import requests
import pprint
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from bson import json_util, ObjectId
import couchdb
from pymongo.errors import ConnectionFailure
from bson import json_util,ObjectId
import couchdb

try:
    client=MongoClient('localhost:27017')
    print(client.list_database_names())
    dato=client.datos
    clientatl=MongoClient('mongodb://Examen1:<eagila926@cluster0-shard-00-00.mae3c.mongodb.net:27017,cluster0-shard-00-01.mae3c.mongodb.net:27017,cluster0-shard-00-02.mae3c.mongodb.net:27017/test?replicaSet=atlas-3q4yws-shard-0&ssl=true&authSource=admin')
except requests.ConnectionError as e:
    raise e

db=client['ejercicio8']
col=db['datos']
dbatl=clientatl['ejercicio8']
colatl=dbatl['datos']

for doc in col.find({}):
    print(doc)

record={
        'name':'Elvis',
        'lastname':'Agila',
        'birthday':'1996-02-19',
        'age':24
        }
colatl.insert_one(record)
col.insert_one(record)
