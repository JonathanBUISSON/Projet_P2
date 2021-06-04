import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

links=[]
#Afin de parcourir les 50 pages
for i in range(51):    
  url = "https://books.toscrape.com/" + str(i)
#importer le code de la page
response = requests.get(url)
print(response),

if response.ok:
    print(response)
    #print("Page: "+str(i))
soup = BeautifulSoup(response.text, "lxml")

#print(soup.get_text())

b=soup.title.string #permet d'afficher ce qui est entre les balises <title>
#print(b)

#soup.find_all("a") return a list of all links in the HTML source.
#You can loop over this list to print out all the links on the webpage

for link in soup.find_all("a"):
    link_url = link["href"]
    print(link_url)
    links.append("http://books.toscrape.com"+ link_url)
    #time.sleep(1)
    print(len(links))
    image=soup.find_all("img")
    print(image)
    product_page_url=soup.find_all("product_pod")
    print(product_page_url)
    Universal_product_code=soup.find_all("UPC")
    print(Universal_product_code)
    title=soup.find_all("A light in the Attic")
    print(title)
    Price_including_tax=soup.find_all("<td>£51.77</td>")
    print(Price_including_tax)
    Price_excluding_tax=soup.find_all("<td>£51.77</td>")
    print(Price_excluding_tax)
    number_available=soup.find_all("<td>In stock (22 available)</td>")
    print(number_available)

#product_description=soup.find_all() #Je ne sais pas remplir la description
    category=soup.find_all("/category/books/poetry_23/index.html>Poetry")
    print(category)
    review_rating=soup.find_all("<td>0</td>")
    print(review_rating)
    image_url=soup.find_all("<img src=/media/cache/fe/72/fe72f0532301ec28892ae79a629a293c.jpg alt=A Light in the Attic>")
    print(image_url)    



