pip install lxml

pip install beautifulsoup4

pip install requests

from bs4 import BeautifulSoup
import requests

source = requests.get('http://quotes.toscrape.com/').text
soup = BeautifulSoup(source,'lxml')

dados = soup.find_all('div', class_='col-md-8')
dados

for lista_d in dados:
    lista = lista_d.find_all('span', class_='text' )
    for nova_lista_d in lista:
        print(nova_lista_d.next_element)
        
        
list = []
for x in range(0, 10):
    url = 'http://quotes.toscrape.com/'
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')
    for lista_d in dados:
        lista = lista_d.find_all('span', class_='text' )
        for nova_lista_d in lista:
            new_dados = nova_lista_d.next_element
            list.append(new_dados)
            
            
for lista_d_autor in dados:
    lista_a = lista_d_autor.find_all('small', class_='author')
    for nova_lista_d_autor in lista_a:
        print(nova_lista_d_autor.next_element)
        
        
list = []
for x in range(0, 10):
    url = 'http://quotes.toscrape.com/'
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')
    for lista_a in dados:
        lista = lista_a.find_all('small', class_='author' )
        for nova_lista_d_a in lista:
            new_dados_a = nova_lista_d_a.next_element
            list.append(new_dados_a)
            
import pandas as pd

df_author = pd.DataFrame(list,columns=['author'])
df_author

df_frases = pd.DataFrame(list,columns=['frases'])
df_frases

df_frases['frases'].to_csv('frases.csv', encoding='ansi', index=False)

df_author['author'].to_csv('author.csv', encoding='ansi', index=False)

pip install mysql-connector-python

import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "blog"
)

print(mydb)

for i in range(0,len(frases)):
    mycursor = mydb.cursor()
    sql = "INSERT INTO frases (frase,autor) VALUES ('%s','%s')" %(frases[i],autores[i])
    mycursor.execute(sql)
    mydb.commit