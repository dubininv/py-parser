import requests
from bs4 import BeautifulSoup


def main():
    url = 'https://www.avito.ru/krasnodar/avtomobili?pmax=200000&pmin=100000&radius=200&s_trg=3&i=1'
    html = requests.get(url).text
    bs = BeautifulSoup(html, 'html.parser')


if __name__ == '__main__':
    main()
