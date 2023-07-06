import requests
from bs4 import BeautifulSoup

req = requests.get("https://hammadkhan999.github.io/CSS-SITE/")

soup = BeautifulSoup(req.content, "html.parser")

res = soup.title

print(soup.prettify())