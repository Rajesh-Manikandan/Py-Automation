import requests
from bs4 import BeautifulSoup


URL = "https://pythonprogramming.net/navigating-pages-scraping-parsing-beautiful-soup-tutorial/?completed=/introduction-scraping-parsing-beautiful-soup-tutorial/"

html = requests.get(URL)

page = BeautifulSoup(html.content, 'lxml')


print(page.h5.get_text())
