import requests
import json
import webbrowser
from bs4 import BeautifulSoup
import random
import logging

site = 'https://shop.extrabutterny.com'
logging.basicConfig(level=logging.INFO)
logging.info('### Shopify Roulette ##')
logging.info('Current Quicktask Bot: TheKickStation')
logging.info('Current site: {}'.format(site))

links = []

logging.info('Getting list of all products...')
sitemap = requests.get(site+'/sitemap_products_1.xml?from=139349587&to=2341962219568').text
y = BeautifulSoup(sitemap,"xml")
for item in y.findAll('loc'):
    if str(item).find('<loc>') > -1:
        link = str(item).replace('<loc>','').replace('</loc>','')
        links.append(link)



inStock = False

while inStock == False:
        logging.info('Choosing random link...')
        randomLink = random.choice(links)
        product_json = json.loads(requests.get(randomLink+'?view=json_extended').text)
        logging.info('Product found: {}'.format(product_json['title']))
        if product_json['inventory_quantity'] > 0:
                logging.info('Product in stock! Quicktasking, good luck!')
                inStock = True
                webbrowser.open('https://thekickstationapi.com/quick-task.php?link='+randomLink+'&autostart=true')
        else:
                logging.info('Out of stock, trying another product...')
                

# webbrowser.open(randomLink)
    

#?view=json_extended