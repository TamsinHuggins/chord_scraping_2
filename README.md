# "Pop-Science": Analysing the Most Popular Songs on UltimateGuitar.com

This is a collaborative project is in progress. So far, chord data, lyric data, and song metadata for the most popular 4600 songs on UltimateGuitar.com have been scraped, ready for analysis.

### Features
* Scrapes song lyrics, chords, and additional song information.
* Batches the scraping process into groups of ~1000 songs.
*Stores the scraped data in pickle files for easy retrieval and analysis.

### How it Works
The scraper uses Python's Requests, Selenium and BeautifulSoup libraries to send HTTP requests to UltimateGuitar.com and parse the HTML of the song pages. It uses regular expressions to extract the lyrics and chords from the page content.

### Usage
To run the scraper, simply execute the cleaning1.py script. This will start the scraping process. The script will print progress updates to the console as it completes each batch of 1000 songs.

The scraped data is stored in a pickle file in the scraped directory. Each batch of 1000 songs is stored in a separate file. The files are named chords_songs_0-1000.pkl, chords_songs_1000-2000.pkl, etc.

### Requirements
* Python 3
* Requests library
* BeautifulSoup library
* Selenium library
* Pickle library
* Re library

### Future plans

NLP techniques will be used to analyse the chords to create a chord substitution tool for data-driven songwriting and musical experimentation.


### Disclaimer
This project is intended for educational purposes only. Please respect the terms of service of UltimateGuitar.com and do not use this scraper for commercial purposes or in a way that could harm the website's performance.
