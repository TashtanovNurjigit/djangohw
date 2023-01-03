import requests
from bs4 import BeautifulSoup as BS
from django.views.decorators.csrf import csrf_exempt


URL = 'https://aldebaran.ru'

HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}


@csrf_exempt
def get_html(url, params=''):
    req = requests.get(url, headers=HEADERS)
    return req


@csrf_exempt
def get_data(html):
    soup = BS(html, 'html.parser')
    items = soup.find_all('div', class_='wrap')
    book_list = []

    for item in items:
        book_list.append(
            {
                'title': item.find("div", class_='book_info clearfix').find('a').get_text(),
                'author': URL + item.find("div", class_='book_info clearfix').find('a').get('href'),
                'image': item.find('div', class_='img').find('img', class_='cwr').get('src')
            }
        )
    return book_list


@csrf_exempt
def parser():
    html = get_html(URL)
    if html.status_code == 200:
        book_list1 = []
        for page in range(0, 1):
            html = get_html(f'https://aldebaran.ru/knigi/', params=page)
            book_list1.extend(get_data(html.text))
        return book_list1
    else:
        raise Exception('Error in parser func.....')

