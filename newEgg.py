import requests
from bs4 import BeautifulSoup as soup
import json
import sys


url = f"https://www.newegg.com/{sys.argv[1]}" if len(sys.argv) > 1 else "https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card"

page = soup(requests.get(url).content, 'html.parser')
containers = page.findAll("div", {"class":"item-container"})

obj = []


for i, cop in enumerate(containers):
    title = cop.find("a", {"class": "item-title"}).text.strip()
    img = cop.find("a", {"class": "item-img"}).img['src'].strip()
    price = cop.find("li", {"class": "price-current"}).text.strip()
    ship = cop.find("li", {"class": "price-ship"}).text.strip()
    rate = cop.find("a", {"class": "item-rating"})["title"] if cop.find("a", {"class": "item-rating"}) else ""
    promo = cop.find("p", {"class": "item-promo"})
    promo = promo.text if promo.text else ""
    id_name = "".join(title.split(" "))
    obj.append({"id": f"{i}", f"{id_name}" : {"title": f"{title}", "image": f"{img}",  "price": f"{price}", "rating": f"{rate}",  "promo": f"{promo}"}})

data = {"Products": []}
for i in obj:
    data["Products"].append(i)

with open ("new.text", "w") as pipe:
    json.dump(data, pipe)
