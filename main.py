import requests
from bs4 import BeautifulSoup


def main():
    base_url = 'https://www.dns-shop.ru'
    url = 'https://www.dns-shop.ru/catalog/17a892f816404e77/noutbuki/'
    html = requests.get(url).text
    bs = BeautifulSoup(html, 'html.parser')
    items: BeautifulSoup = bs.find('div', {'class', 'catalog-items-list view-list'}).find_all('div', {'class', 'item'})

    item_links = []

    for item in items:
        link = item.find('a')['href']
        item_links.append(base_url + link)

    for l in item_links:
        print(l)


if __name__ == '__main__':
    main()
