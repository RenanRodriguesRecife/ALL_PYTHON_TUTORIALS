from urllib import response
import requests

API_KEY =  '' #'SUA CHAVE DE API'
url = f'https://jgalat.github.io/ds-weapons-api/{API_KEY}' #API de DarkSOULs

response = requests.request('GET',url)

print(response.text)