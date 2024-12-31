import urllib3
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/117.0"
}

year_range = range(1988, 2010)

for year in year_range:
    url = "http://www.imdb.com/search/title?release_date=" + str(year) + "," + str(year) + "&title_type=feature"
    our_url = urllib3.PoolManager().request('GET', url, headers=headers).data
    soup = BeautifulSoup(our_url, "lxml")
    movie_list = soup.findAll('h3', attrs={'class':'ipc-title__text'})
    print()
    print("Movies from", year)
    for movie in movie_list:
        print(movie.text)
