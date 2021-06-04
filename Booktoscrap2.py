import requests
from bs4 import BeautifulSoup
import urllib

# -*- coding: utf-8 -*-


def main():
#Open a connection to a URL using urllib
  webUrl = urllib.request.urlopen("http://www.meteociel.fr/observations-meteo/temps-reel.php")
      
# get the result code and print it
  print("resultat code " +str(webUrl.getcode()))

#read the data from the URL and print it
  data=webUrl.read()
  print(data)

if __name__=="__main__":
   main()

#webUrl.close()
#f = open("data1.txt","w")
#f.write(fich)
#f.close()

soup=BeautifulSoup(data.text,"html parser")

    
