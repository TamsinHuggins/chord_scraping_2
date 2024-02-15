# "Pop-Science": Analysing the Most Popular Songs on UltimateGuitar.com

This collaborative project is in progress. So far, chord data, lyric data, and song metadata for the most popular 4955 songs on UltimateGuitar.com have been scraped. We are currently in the analysis phase, using NLP techniques to uncover insights about chord progressions and chord-lyric relationships in popular music.

## Components of this project
### The webscraper
* Scrapes song lyrics, chords, and additional song information from over 4000 songs on UltimateGuitar.com.
* Stores the scraped songs, batched into thousands, in pickle files for easy retrieval and analysis.

### The analysis
#### Chord-only analysis
* Regexes are used to extract just the chord information from chord + lyric files.
* [Word2Vec] (https://www.tensorflow.org/text/tutorials/word2vec) is used to characterise chords based on their context. (in progress).
* Dimensionality reduction on the Word2Vec vectors in order to visualise chord similarity.

### 3D representation of chord embeddings

The tensorflow model created a 128-dimension vector to describe each chord based on context (which chords are common neighbors to the chord). This was dimenstionality-reduced to 3 dimensions such that it could be visualised (below).
In theory, distance in the 3D space relates to chord similarity. Chords that are closer in the 3D space are more similar than those further away. 

![image](https://github.com/TamsinHuggins/pop-chord-analysis-ultimateguitar/assets/32196191/f126a7ca-5e09-49dc-ad84-37c6b272e832)



#### Lyric-chord association
* Chords are mapped to the lyrics which are sung while that chord is played (in progress)

## Technologies and skills used
* Webscraping using Requests, Selenium and BeautifulSoup Python libraries.
* Textual data wrangling and cleaning with use of regexes, Python re library.
* NLP techniques to preprocess and analyse chords and lyrics.
* Deep learning using TensorFlow's Word2Vec method.
* Project management using Asana to delegate and track tasks.
* Collaboration and teamwork: Tamsin and Roshani held regular in-person meetings to plan and execute the project.


### Requirements
* Python 3
* Requests library
* BeautifulSoup library
* Selenium library
* Pickle library
* Re library


### Disclaimer
This project is intended for educational purposes only. Please respect the terms of service of UltimateGuitar.com and do not use this scraper for commercial purposes or in a way that could harm the website's performance.
