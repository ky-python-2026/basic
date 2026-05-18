import time
import requests

urls = ["https://www.daum.net/", "https://www.naver.com/", "https://www.inflearn.com/"]


for url in urls:
    response = requests.get(url)

    print(response.status_code)

    time.sleep(1)