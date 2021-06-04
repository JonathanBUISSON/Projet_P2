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
  
  table = html_soup.find("table", {"class":"table table-striped"})
  results = table.find_all("td")
  title = html_soup.find("h1").text.strip()
  UPC = results[0].text.strip() #la methode .strip() enlève les espaces en début et en fin de mot.
  Product_type = results[1].text.strip()
  Price_excluding_tax = results[2].text.strip()
  Price_including_tax = results[3].text.strip()
  Tax = results[4].text.strip()
  Availability = results[5].text.strip()
  Numbers_of_review = results[6].text.strip()
  
  #Image = html_soup.find("img src")
  print(title)
  print(UPC)
  print(Product_type)
  print(Price_excluding_tax)
  print(Price_including_tax)
  print(Tax)
  print(Availability)
  print(Numbers_of_review)
 
  #print('Number of results', len(results))


def tableau(result):
    tab=[]
    for result in results:
         #result = results.find("td")
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
        i+=1

    
