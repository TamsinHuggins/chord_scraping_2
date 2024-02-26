# this script looks over all the chords and translates them into their roman numeral chord encodings according to the key.
import pickle
import os
import numpy as np
from itertools import chain
import numpy as np


# navigate down into the scraped folder
os.chdir('scraped')

#  use pickle to load all songs
file_names = ["chords_songs_0-999.pkl", "chords_songs_1000-1999.pkl", "chords_songs_2000-2999.pkl", "chords_songs_3000-4955.pkl"]
allsongs = []

for file_name in file_names:
    with open(file_name, 'rb') as f:
        allsongs.append(pickle.load(f))

# load in the keys
with open('keys.pkl', 'rb') as f:
    keys = pickle.load(f)

# concatenate the 4 lists in allsongs into one list
all_songs = list(chain(*allsongs))
print(len(all_songs))
 

###############    CHECK THE KEYS MATCH THE LIST POSITION OF THE RIGHT SONGS   ####################

# print th key for song 0 and the chords
print(keys[0])
print(all_songs[0])
