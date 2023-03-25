from bs4 import BeautifulSoup
import requests

url = "http://books.toscrape.com/"

tag = requests(url)
tag['value'] = 'new value'

print(tag)

