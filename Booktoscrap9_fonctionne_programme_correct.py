import requests
from bs4 import BeautifulSoup
import csv
# -*- coding: utf-8 -*-

from requests import get

url ="https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
response = get(url)
print(response.text[:500])

#Type is a great function that will tell us what 'type' a variable is. Here, response is a http.response object.
print(type(response))

if response.ok:
  html_soup = BeautifulSoup(response.text,features='html.parser')
  type(html_soup)
  
  bookshelf = html_soup.find_all("div",{"class":"col-sm-6 product_main"})
  print(type(bookshelf))
  

  table = html_soup.find("table", {"class":"table table-striped"})
  results = table.find_all("td")
  UPC=results[0].text.strip() #la methode .strip() enlève les espaces en début et en fin de mot.

  print(UPC)
  print('Number of results', len(results))
  print(results)

def tableau(result):
    tab=[]
    for result in results:
         result = results.find("td")
         tab.append(result)
         return tab
  
with open("donnees.csv", "w", encoding="utf-8") as fichier:
    writer = csv.writer(fichier)
    
j = len(results)
i = 0
with open("donnees.csv", "w", encoding="utf-8") as fichier:
    writer = csv.writer(fichier)
    while i < j:
        writer.writerow(results[i])
        i=i+1

    
