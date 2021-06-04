import requests
from bs4 import BeautifulSoup
import pandas as pd

#Parcourir l'ensemble des pages du site Book.toscrape.com
'''
token = 'https://books.toscrape.com/'
def get_pages(token, nb):
    pages = []
    for i in range(1,nb+1):
        j = token + str(i)
        pages.append(j)
    return pages
pages = get_pages(token,50)

#importer le code de la page
for i in pages:
    response=requests.get(i)
print(response)
'''

url="https://books.toscrape.com/"
response=requests.get(url)
print(response)

#on met un parser et on met le tout dans une variable soup qui utilise la fonction Beautiful Soup
soup=BeautifulSoup(response.text,"html.parser")
product_page_url=soup.findAll("title", class={"default"})

The_books=[]

for i in product_page_url:
   books={}
   books['table', class="table table-striped"]=i.universal_product_code_upc.text
   books['table', class="table table-striped"]=i.title.text
   books['table', class="table table-striped"]=i.price_including_tax.text
   books['table', class="table table-striped"]=i.price_excluding_tax.text
   books['table', class="table table-striped"]=i.number_available.text
   books['table', class="table table-striped"]=i.product_description.text
   The_books.append(books)


parameters = ['upc','title','price_including_tax','price_excluding_tax','number_available','product_description']
df_f = pd.DataFrame()
for par in parameters:
    l = []
    for el in product_page_url:
        j = el[par]
        l.append(j)
    l = pd.DataFrame(l, columns = [par])
    df_f = pd.concat([df_f,l], axis = 1)
    df = df_f.append(df_f, ignore_index=True)
    df.to_csv('product.csv', index=False, encoding='utf-8')

#convertir la liste en base de données
#df=pd.DataFrame(news_items,columns=['title','description','pubdate'])
#df.head(10)

#générer le fichier csv
#df.to_csv('web_scrapping.csv', index=False, encoding='utf-8')
