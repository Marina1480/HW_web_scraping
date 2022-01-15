import requests
import bs4

KEYWORDS = ['дизайн', 'фото', 'web', 'python']

response = requests.get('https://habr.com/ru/all/')
response.raise_for_status()
soup = bs4.BeautifulSoup(response.text, features='html.parser')
articles = soup.find_all('article')

for article in articles:
    hubs = article.find_all(class_='tm-article-snippet__hubs-item')
    hubs = set(hub.find('span').text for hub in hubs)

    for key_ in KEYWORDS:
        for hub in hubs:
            if key_.casefold() == hub.casefold():
                href = article.find(class_='tm-article-snippet__title-link').attrs['href']
                link = 'https://habr.com' + href
                print(article.find('time').text, '-', article.find('h2').text, '-', link)
