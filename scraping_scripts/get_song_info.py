
from bs4 import BeautifulSoup
import requests

def get_song_info(URL):
    response = requests.get(URL)
    page = response.text
    pagesoup = BeautifulSoup(page, "html.parser")
    script_tag = pagesoup.find_all('script', type='application/ld+json')
    script_tag =list(script_tag)
    return script_tag[1]