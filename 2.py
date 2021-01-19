import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient




if __name__ == '__main__':

    db_client = MongoClient('localhost:27017')
    olx = db_client.olx
    datos = olx.posts


    response = requests.get("https://www.olx.com.ec/")
    soup = BeautifulSoup(response.content, "lxml")

    post_titles = soup.find_all("img", class_="_1N079")

    extracted = []
    for post_title in post_titles:
        extracted.append({
            'title' : post_title['alt'],
            'link'  :  post_title['src'],
            'sizes' : post_title['sizes']
        })


    for post in extracted:
       if db_client.olx.datos.find_one({'link': post['link']}) is None:

            print("Found a new listing at the following url: ", post['link'])
            db_client.olx.datos.insert_one(post)