import requests
from bs4 import BeautifulSoup

url: str = "https://en.wikipedia.org/wiki/List_of_exoplanets_discovered_by_the_Kepler_space_telescope:_1%E2%80%93500"
path: str = "/home/needjobcoder/Documents/Development/web/webPythonProject/django/django-practice/backend/scrapedData/base.html"

def getFile():
    response = requests.get(url)
    html_content = " "
    if response.status_code == 200:
        html_content = response.content
    else:
        print(f"Failed to fetch the page. Status code: {response.status_code}")
        exit()

    soup = BeautifulSoup(html_content, "html.parser")

    with open(path, 'w', encoding='utf-8') as file:
        file.write(str(soup))

getFile()