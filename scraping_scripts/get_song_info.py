
from bs4 import BeautifulSoup
import requests

test_URL= "https://tabs.ultimate-guitar.com/tab/ed-sheeran/perfect-chords-1956589"

def get_song_info(URL):
    response = requests.get(URL)
    page = response.text
    pagesoup = BeautifulSoup(page, "html.parser")
    script_tag = pagesoup.find_all('script', type='application/ld+json')
    script_tag =list(script_tag)
    return script_tag[1].text

tag = get_song_info(test_URL)

# save tag to a text file
with open("sheeranInfo.txt", "w") as f:
    f.write(str(tag))