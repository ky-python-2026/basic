import requests
from bs4 import BeautifulSoup


url = "https://news.daum.net/"

response = requests.get(url)
html=response.text

soup= BeautifulSoup(html,"html.parser")

print(soup)