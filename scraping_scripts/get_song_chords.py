
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import re

test_URL= "https://tabs.ultimate-guitar.com/tab/ed-sheeran/perfect-chords-1956589"

def get_lyrics_chords(URL):
#  use beautifulsoup to make a soup object of the whole page
    response = requests.get(test_URL)
    page = response.text
    page_soup = BeautifulSoup(page, "html.parser")
    #find all the divs with the class js-store
    info = page_soup.find_all('div', { 'class' : 'js-store'})[0]
    print(page_soup)
    info = str(info)
    # use regex to find any text after the first [ch]
    begin = re.findall(r'\[ch\](.*)', info)[0]
    snipped = begin.split("&quot;")[0]
    return snipped


#  call get lyrics on the URL, then save to a file called buckleyInfo.txt
lyrics = get_lyrics_chords(test_URL)
with open("sheeranChordsLyrics.txt", "w") as f:
    f.write(lyrics)