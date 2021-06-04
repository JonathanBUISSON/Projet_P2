import requests
from bs4 import BeautifulSoup
import csv
# -*- coding: utf-8 -*-

from requests import get

url ="https://books.toscrape.com/"
response = get(url)
print(response.text[:500])

#Type is a great function that will tell us what 'type' a variable is. Here, response is a http.response object.
print(type(response))

if response.ok:
  html_soup = BeautifulSoup(response.text,features='html.parser')
  type(html_soup)
  
  bookshelf= html_soup.find_all("li",{"class":"col-xs-6 col-sm-4 col-md-3 col-lg-3"})
  print(type(bookshelf))
  
  #create csv file or all products
  
  #filename=("Books.csv")
  #f=open(filename,"w")
  #headers= "Book title, Price\n"
  #f.write(headers)

  #table=html_soup.find("table", {"class":"table table-striped"})
  #results=table.find_all("tr")
  #print('Number of results', len(results))
  #print(results)

 # pages=html_soup.find("div", {"class":"col-sm-8 col-md-9"})

#def Pages(page):
 #     P=[]
  #    for page in pages:
   #     P.append(page)
    #  return P
    
def tableau(results):
    tab=[]
    for result in results:
     result=results.string.strip()
     tab.append(result)
     return tab
  
   for books in bookshelf :
    #collect title of all books
       book_title = books.h3.a["title"]
       print(type(book_title))

     #print(html_soup.get_text())
     
   #collect book price of all books
     #book_price = books.find_All("p",{"class":"price_color"})
     #price = book_price[0].text.strip()
    
     #f.write(book_title)
     
#f.close()



#with open("donnees.csv", "w", encoding="utf-8") as fichier:
 #   writer = csv.writer(fichier)
    
#j = len(results)
#i = 0
#with open("donnees.csv", "w", encoding="utf-8") as fichier:
 #   writer = csv.writer(fichier)
  #  while i < j:
   #     writer.writerow(results[i])
    #    i=i+1

    
