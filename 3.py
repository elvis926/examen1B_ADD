from facebook_scraper import get_posts
from pymongo import MongoClient
import json
import time

if __name__ == '__main__':

 	client = MongoClient('mongodb://localhost:27017')
 	Ejercicio3 = client.Ejercicio3
 	datos = Ejercicio3.posts

 	extracted = []

 	i=1
 	for post in get_posts('xbox',pages = 50, extra_info =True):
 		i=i+1
 		time.sleep(5)
 		id=post['post_id']
 		doc={}
 		doc['id']=id
 		mydate=post['time']
 		try:
 			doc['texto'] = post['text']
 			doc['date']=mydate.timestamp()
 			doc['likes']=post['likes']
 			doc['comments']=post['comments']
 			doc['shares']=post['shares']

 			doc['post_url']=post['post_url']
 			client.Ejercicio3.insert(doc)

 			print("Guardado correctamente")
 		except Exception as e:
 			print("No se pudo grabar:" + str(e))