import requests
from bs4 import BeautifulSoup
import csv
import os

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36',
    'Accept': '*/*'
}
FILE = 'cars.csv'

def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    r.encoding = 'utf-8'
    return r

def get_pages_count(html):
    soup = BeautifulSoup(html, 'html.parser')
    pagination = soup.find_all('a', class_='Button Button_color_whiteHoverBlue Button_size_s Button_type_link Button_width_default ListingPagination-module__page')
    if pagination:
        return int(pagination[-1].get_text())
    else:
        return 1

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='ListingItem-module__main')
    cars = []
    for item in items:
        cars.append({
            'title': item.find('a', class_='Link ListingItemTitle-module__link').get_text(strip=True),
            'link': item.find('a', class_='Link ListingItemTitle-module__link').get('href'),
            'price': item.find('div', class_='ListingItemPrice-module__content').get_text(strip=True).replace('\xa0',' '),
            'city': item.find('span', class_='MetroListPlace__regionName MetroListPlace_nbsp').get_text(),
        })

    return cars

def save_file(items, path):
    with open(path, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Марка', 'Ссылка', 'Цена', 'Город'])
        for item in items:
            writer.writerow([item['title'], item['link'], item['price'], item['city']])

def parse():
    URL = input('Введите URL: ')
    URL = URL.strip()
    html = get_html(URL)
    if html.status_code == 200:
        pages_count = get_pages_count(html.text)
        cars = []
        for page in range(1, pages_count + 1):
            print(f'Парсинг страницы {page} из {pages_count}...')
            html = get_html(URL, params={'page': page})
            cars.extend(get_content(html.text))

        print(f'Получено {len(cars)} автомобилей')
        save_file(cars, FILE)
        os.startfile(FILE)
    else:
        print('Error')

parse()