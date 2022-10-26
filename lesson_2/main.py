import requests
from bs4 import BeautifulSoup
import csv

def create_csv(data):
    with open('data.csv', 'w') as file:
        writer = csv.writer(file)
        for _ in data.items():
            # print(_)
            writer.writerow(_)
        # writer.writerow((
        #         data['name'],
        #         data['url'],
        #         data['reviews']
        #     ))

def refined(s):
    return int(s.split(' ')[0].strip('(').replace(',', ''))

def get_html(url):
    response = requests.get(url)
    return response.text

def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    popular = soup.find_all('section')[3]
    plugins = popular.find_all('article')
    for plugin in plugins:
        name = plugin.find(class_='entry-header').text
        url = plugin.find('a').get('href')
        reviews = refined(plugin.find(class_='rating-count').text)
        data = {
            'name': name,
            'url': url,
            'reviews': reviews
        }
        create_csv(data)

def main():
    url = 'https://wordpress.org/plugins/'
    print(get_data(get_html(url)))

if __name__ == '__main__':
    main()