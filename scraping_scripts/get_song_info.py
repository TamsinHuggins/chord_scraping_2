
from bs4 import BeautifulSoup
import requests
import os


def get_song_info(URL, num):
    """given a URL of a song page, writes the song info (Artist, Song Name, Key, Capo Information, Difficulty)
    to a text file.
    Parameters:
    URL (str): URL of the song page
    num (int): number to label the song file
    """
    response = requests.get(URL)
    page = response.text
    pagesoup = BeautifulSoup(page, "html.parser")
    script_tag = pagesoup.find_all('script', type='application/ld+json')
    script_tag =list(script_tag)
    tag =  script_tag[1].text

    # write the file into the folder called scraped
    # Check if the current directory is not 'scraped'
    current_dir = os.getcwd()
    if not current_dir.endswith('scraped'):
        # If not, change to the 'scraped' directory
        os.chdir('scraped')

    with open( f"song_{num}_info.txt", "w") as f:
        f.write(str(tag))