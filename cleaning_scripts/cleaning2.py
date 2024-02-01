import pickle
import os

# navigate into scraped folder
current_dir = os.getcwd()

# if not in the scraped directory, change into it
if not current_dir.endswith('scraped'):
    os.chdir('scraped')

#use pickle to read chords_songs_0-1000.pkl
with open("chords_songs_1000-2000.pkl", 'rb') as f:
    chords_songs_0_1000 = pickle.load(f)
print(chords_songs_0_1000[4])