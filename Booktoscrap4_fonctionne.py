import requests
from bs4 import BeautifulSoup
import urllib
import csv
# -*- coding: utf-8 -*-



#urllib.request.Request()
#This class is an abstraction of a URL request.
#url should be a string containing a valid URL.

req = urllib.request.Request("https://books.toscrape.com/")

#Open the URL url, which can be either a string or a Request object.
response = urllib.request.urlopen(req)
   
#Type is a great function that will tell us what 'type' a variable is. Here, response is a http.response object.
print(type(response))
    
#To read function for our reponse object will store the html as bytes to
# our variable. Again type() will verify this.
htmlBytes = response.read()
print(type(htmlBytes))

#Now we use the decode function for our bytes variable to get a single string.
htmlStr = htmlBytes.decode("utf8")
print(type(htmlStr))

#if you do want to split up this string into separate lines, you can do so with
#the split() function.

#In this form we can easily iterate through to print out the entire page
#or do any other processing
htmlSplit = htmlStr.split('\n')
print(type(htmlSplit))

soup = BeautifulSoup(response,'lxml')
print(soup.prettify())

for line in htmlSplit:
    print(line)
    
#soup.find_all("a") return a list of all links in the HTML source.

links=[]

for link in soup.find_all("a"):
    link_url=link.get('href')
    print(link_url)
    links.append("https://books.toscrape.com/"+ link_url)
    print(links)
    
#for title in soup.find_all("a"):
   # title_url=title.get('a href')
#print(title_url)
    #titles.append("https://books.toscrape.com/"+titles_url)
    #print(titles)
       
with open("donnees.csv", "w", encoding="utf-8") as fichier:
    writer = csv.writer(fichier)
    i=0
    j = len(links)
    while i < j:
        writer.writerow(links)
        i=i+1
                        


    
