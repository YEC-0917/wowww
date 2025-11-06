from bs4 import BeautifulSoup
import requests

r = requests.get("https://zh.wikipedia.org/wiki/%E5%9B%BD%E5%AE%B6%E6%96%87%E7%89%A9%E5%B1%80", headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36"})
soup = BeautifulSoup(r.content)

aw = soup.find_all("h2")
for x in aw:
    print(x.text)

div = soup.find("div")
print(div.get_text())

