import requests
from bs4 import BeautifulSoup

url = "https://www.gov.uk/search/news-and-communications"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
titres = soup.find_all("a", class_="gem-c-document-list__item-title")
descriptions = soup.find_all("p", class_="gem-c-document-list__item-description")

print('TITRES :')
for titre in titres:
    print(titre.string)

print('DESCRIPTIONS :')
for desc in descriptions:
    print(desc.string)
