import requests
from bs4 import BeautifulSoup


def main():
    url = 'https://sinoptik.com.ru'
    html = requests.get(url).text
    bs = BeautifulSoup(html)
    main_div = bs.find('div', {'class', 'main'})
    print(main_div.prettify())


if __name__ == '__main__':
    main()
