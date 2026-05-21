import requests

client_id = "v8OG_BCa6GegHdZfJ55J"
client_secret = "4C8fMvYJG_"

url = "https://openapi.naver.com/v1/search/blog.json"

headers = {
    "X-Naver-Client-Id": client_id, "X-Naver-Client-Secret": client_secret
    }

params={
    "query":"파이썬",
    "display":10,
    "start":1,
    "sort":"sim"
}

response=requests.get(url,headers=headers,params=params)

print(response.status_code)
print(response.json())
