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
  
  bookshelf= html_soup.find_all("div",{"class":"col-sm-6 product_main"})
  print(type(bookshelf))
  
  #create csv file or all products
  
  filename=("Books.csv")
  f=open(filename,"w")
  
  headers= "Book title, Price\n"
  f.write(headers)
  
  for books in bookshelf:

    #collect title of all books
     book_title = html_soup.find("h1")
     print(type(book_title))
     #print(html_soup.get_text())
     
   #collect book price of all books
     #book_price = books.find_All("p",{"class":"price_color"})
     #price = book_price[0].text.strip()
     
     #f.write(book_title + ","+ price+ "\n")
    
     #print("Title of the book :"+ book_title)
     #print("Price of the book :"+ price)
     f.write(book_title)
     
     #f.write(book_title + ","+ price+ "\n")
     
f.close()  




  
    


    
