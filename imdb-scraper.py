import requests
from bs4 import BeautifulSoup
import redis

url = 'https://www.imdb.com/chart/top'

r = redis.Redis(host='localhost', port=6379, db=0)
if r.get('imdb_top250') is None:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    movies = soup.select('td.titleColumn')
    for i, movie in enumerate(movies):
        title = movie.select('a')[0].text
        year = movie.select('span.secondaryInfo')[0].text
        r.hset('imdb_top250', title, year)
        print(f'{i+1}. {title} ({year})')
else:
    movies = r.hgetall('imdb_top250')
    for i, (title, year) in enumerate(movies.items()):
        print(f'{i+1}. {title.decode()} ({year.decode()})')
