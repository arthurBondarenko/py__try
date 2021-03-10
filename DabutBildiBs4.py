from bs4 import BeautifulSoup
from urllib.request import *
 
url = 'https://wallhaven.cc/search?q={}&search_image=&page={}'


kategorija = input('velama ketegorija: ')
ciklapu = int(input('cik lapu lejupieladed '))

def get_html(url):
    req = Request(url)
    html = urlopen(req).read()
    return html
 
def main():
    opener = build_opener()
    opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
    install_opener(opener)
    for i in range(1, ciklapu):
        html = get_html(url.format(kategorija, i))
        soup = BeautifulSoup(html, 'html.parser')
        saraksts = soup.find_all(class_='preview')
        j = 0
        for a in saraksts:
            secondary_html = get_html(a['href'])
            secondary_soup = BeautifulSoup(secondary_html, 'html.parser')
            bilde = secondary_soup.find(id='wallpaper')['src']
            urlretrieve(bilde, f"bilde_{j}.jpg"  )
            print('Download')
            j=j+1
 
main()
