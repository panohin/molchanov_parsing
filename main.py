import requests
from bs4 import BeautifulSoup

def main():
    url = 'https://wordpress.org/'
    print(get_data(get_html(url)))

def get_html(url):
    response = requests.get(url)
    return response.text

def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    h1 = soup.find(
        'div',
        class_="is-layout-flow wp-block-column"
    ).find('h1').text
    return h1

if __name__ == '__main__':
    main()
