
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import re
import os

# test_URL= "https://tabs.ultimate-guitar.com/tab/jeff-buckley/hallelujah-chords-198052"

#  use beautifulsoup to make a soup object of the whole page
def get_song_chords(URL, num):
    """ given a URL of a song page, writes the chords and lyrics of the song to a text.
    Parameters:
    URL (str): URL of the song page
    num (int): number to label the song file"""

    response = requests.get(URL)
    page = response.text
    page_soup = BeautifulSoup(page, "html.parser")
    #find all the divs with the class js-store
    info = page_soup.find_all('div', { 'class' : 'js-store'})[0]
    info = str(info)

    # use regex to find any text after the first [ch]
    chords_lyrics = re.findall(r'\[ch\](.*)', info)[0]

    # cut all the junk after the end of the chords lyrics section
    snipped_chords_lyrics = chords_lyrics.split("&quot;")[0]

    # write the file into the folder called scraped
    current_dir = os.getcwd()
    if not current_dir.endswith('scraped'):
        # If not, change to the 'scraped' directory
        os.chdir('scraped')

    with open( f"song_{num}_chords_lyrics.txt", "w") as f:
        f.write(str(snipped_chords_lyrics))