import requests
from bs4 import BeautifulSoup
import urllib
import csv
# -*- coding: utf-8 -*-

links=[]
url = requests.get("https://books.toscrape.com/")
htmltext = url.text
print(htmltext)

request = urllib.request.Request("https://books.toscrape.com/")

#Always use a"try/except" when requesting a web page as thing
#can easily go wrong.urlopen()requests the page

try:
    response = urllib.request.urlopen(request)
except:
    print("something wrong")
   
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

soup = BeautifulSoup(htmltext,'lxml')
                  
for line in htmlSplit:
    print(line)
    
#soup.find_all("a") return a list of all links in the HTML source.

for link in soup.find_all("a"):
    link_url=link["href"]
    print(link_url)
    links.append("https://books.toscrape.com/"+ link_url)
    print(links)
    
#soup=BeautifulSoup(data.text,"html parser")


#fichier= csv.reader(open("monfichier.dat", "rb"), delimiter='|')
#for ligne in fichier:
 #   print ligne[0], ligne[1]

    
