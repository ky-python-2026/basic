import requests

response = requests.get("https://finance.daum.net/")

print(response.status_code)
