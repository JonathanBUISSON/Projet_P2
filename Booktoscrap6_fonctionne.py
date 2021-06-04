#import requests
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
  html_soup = BeautifulSoup(response.text,features='html.parser'),
  type(html_soup)
    
#for line in htmlSplit:
    #print(line)
    
#soup.find_all("a") return a list of all links in the HTML source.


book_containers= html_soup.find('div', Class='container-fluid page')
print(type(book_containers))
print(len(book_containers))

for link in book_containers:

  first_book= book_containers[0],
  print(first_book)
  
#soup.find_all("a"):
    #link_url=link.get('href')
    #print(link_url)
    #links.append("https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"+ link_url)
    #print(links)
    
    
#for title in soup.find_all("a"):
   # title_url=title.get('a href')
#print(title_url)
    #titles.append("https://books.toscrape.com/"+titles_url)
    #print(titles)
       
with open("donnees.csv", "w", encoding="utf-8") as fichier:
    writer = csv.writer(fichier)
    i=0
    j = len(book_containers)
    while i < j:
        writer.writerow(links)
        i=i+1
                        


    
