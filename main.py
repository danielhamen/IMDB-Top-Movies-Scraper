import requests
from bs4 import BeautifulSoup

def scrape(i:int, includeYear:bool=True) -> list:
    """
    Returns `x` movies from IMDb

    Make sure `1 <= i <= 250`
    """

    includeYear = int(includeYear)+3

    return [" ".join(x.text.split('\n')[2:includeYear]).strip() for x in BeautifulSoup(requests.get('https://www.imdb.com/chart/top/').text, 'lxml').find_all(class_='titleColumn')][0:i]
