import requests

url = "https://www.daum.net/"

response = requests.get(url)

response.encoding="utf-8"

print(response.text)
