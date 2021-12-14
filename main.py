import csv
import requests
from bs4 import BeautifulSoup

url = "https://www.gov.uk/search/news-and-communications"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
titles_data = soup.find_all("a", class_="gem-c-document-list__item-title")
descriptions_data = soup.find_all("p", class_="gem-c-document-list__item-description")
titles = []
descriptions = []

for title in titles_data:
    titles.append(title.string)

for description in descriptions_data:
    descriptions.append(description.string)

header = ['title', 'description']

with open('data.csv', 'w') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    writer.writerow(header)
    for title, description in zip(titles, descriptions):
        writer.writerow([title, description])
