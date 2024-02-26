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


def get_unique_chords(nested_song_list):
    """ given a list of lists of chords, flattens to a 1D list and returns a set of unique chords"""
    #flatten
    flattened = []
    for batch in nested_song_list:
        for song in batch:
            for chord in song:
                flattened.append(chord)
    #find unique
    allchords_arr = np.array(flattened)
    unique_chords = np.unique(allchords_arr)
    return unique_chords


# create a vocabulary dictionary holding just the unique chords labelled with numbers
def create_vocabs(unique_chords):
    """ given a list of unique chords, returns 2 dictionaries to translate between chords and their numeric labels
     vocab: chord -> integer
     inv_vocab: integer -> chord"""
    vocab = {chord: i+1 for i, chord in enumerate(unique_chords)}
    inv_vocab = {v: k for k, v in vocab.items()}
    return vocab, inv_vocab

def create_sequences(song_list, vocab):
    """ given a list of songs and a vocabulary dictionary, returns:
    sequences: a 2d numpy array, in which each inner array is a sequence of integers representing chords.
    Each inner array in sequences must have a length of 100
    truncated at 100, padded with 0s if shorter than 100."""
    sequences = []
    for song in song_list:
        sequence = [vocab[chord] for chord in song if chord in vocab]
        if len(sequence) > 100:
            sequence = sequence[:100]
        else:
            sequence = sequence + [0]*(100-len(sequence))
        sequences.append(sequence)
    return np.array(sequences)


unique_chords = get_unique_chords(allsongs)
vocab, inv_vocab = create_vocabs(unique_chords)

#flatten allsongs from 3D to 2D
all_songs_flat = list(chain.from_iterable(allsongs))

sequences = create_sequences(all_songs_flat, vocab)


os.chdir('..')
os.chdir('word2vec')
# save the sequences to a numpy .npy file
np.save('sequences.npy', sequences)
# save the vocab and inv_vocab to a pickle file
with open('vocab.pkl', 'wb') as f:
    pickle.dump(vocab, f)
with open('inv_vocab.pkl', 'wb') as f:
    pickle.dump(inv_vocab, f)