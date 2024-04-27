import requests
from bs4 import BeautifulSoup

data = requests.get("https://rahulshettyacademy.com")
soup = BeautifulSoup(data.content, 'html.parser')
print(soup.prettify())
