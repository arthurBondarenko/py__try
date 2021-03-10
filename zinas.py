from bs4 import BeautifulSoup
import requests

url = 'https://www.delfi.lv/'

page = requests.get(url)

zinas_jaunas = []
zinas = []
soup = BeautifulSoup(page.text, "html.parser")
zinas = soup.findAll('a', class_='text-mine-shaft')
for i in range(len(zinas)):
    if zinas[i].find('h1', class_='headline__title') is not None:
        zinas_jaunas.append(zinas[i].text)
for i in range(len(zinas_jaunas)):
    print(zinas_jaunas[i])