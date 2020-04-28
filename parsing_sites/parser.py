import requests
from bs4 import BeautifulSoup

URL = 'https://auto.ru/moskovskaya_oblast/cars/tesla/all/'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36',
    'Accept': '*/*'
}

def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    r.encoding = 'utf-8'
    return r

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='ListingItem-module__main')
    cars = []
    for item in items:
        cars.append({
            'title': item.find('a', class_='Link ListingItemTitle-module__link').get_text(strip=True),
            'link': item.find('a', class_='Link ListingItemTitle-module__link').get('href'),
            'price': item.find('div', class_='ListingItemPrice-module__content').get_text(strip=True).replace('\xa0',''),
            'city': item.find('span', class_='MetroListPlace__regionName MetroListPlace_nbsp').get_text(),
        })

    return cars

def parse():
    html = get_html(URL)
    if html.status_code == 200:
        cars = get_content(html.text)
    else:
        print('Error')

parse()