---
title: "Mans Referats"
author: Arturs Bondarenko
date: "20-05-2020"
subject: "Python"
keywords: [Markdown, Example]
lang: "en"
subtitle: "Dabuham bildes no vietnes"
titlepage: true
titlepage-color: "3C9F53"
titlepage-text-color: "FFFFFF"
titlepage-rule-color: "FFFFFF"
titlepage-rule-height: 2
...

## Pieslēdzam moduli un dabujam HTML saturu 

```python
from bs4 import BeautifulSoup
from urllib.request import *
```

## Mainigas

```python
kategorija = input('velama ketegorija: ')
ciklapu = int(input('cik lapu lejupieladed '))
```


## Parsejam vietni 

Izmantojot modeli BeautifulSoup mēs apstradajam HTML. Dabujam to url un lasam visu ko satur vietne 


```python
def get_html(url):
    req = Request(url)
    html = urlopen(req).read()
    return html
```


## Dabujam bildes

Vispirms izveidojām funkciju kura palīdz mums ieiet vietne. Parsejam HTML lai dabūt bildes adressi. Pēc tam parējam uz "src" pec ID nosaukuma un lejupielādēt bildes

```python
 
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
```

#Uz prieksu

1. Ievadam kategoriju
2. Ievadam skaili no cikiem lappam dabut bildes
3. Finis