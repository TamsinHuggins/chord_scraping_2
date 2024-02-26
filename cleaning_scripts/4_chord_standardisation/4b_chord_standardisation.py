#this file deals with problems in the chords
# it is common for one chord to be encoded in multiple ways. e.g. EM9 means Emaj9

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

