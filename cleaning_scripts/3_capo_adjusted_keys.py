# this script takes in two lists: one list of keys and one list of capo info
# the resulting data is one list of key signatures adjusted for the capo: i.e. key of F with capo 1 gives chord progressions in E

import os
import pickle

# list of notes
notedict = {
    "A": 0,
    "B": 1,
    "C": 2,
    "D": 3,
    "E": 4,
    "F": 5,
    "G": 6
}

# inverted dictionary
inv_notedict = {v: k for k, v in notedict.items()}

def key_capo(key, capo_number):

    # strip out everything but the first character of key
    letter = key[0]

    # convert key to numbers
    key_number = notedict[letter]

    # find new key number modulo 7
    new_key_number = (key_number - capo_number) % 7

    # convert number into note for key
    new_key = inv_notedict[new_key_number]

    # overwrite the first character of key with new_key
    key = new_key + key[1:]

    return key


#  navigate into the scraped directory
os.chdir("scraped")

# open the .pkl file called "keys.pkl"

with open("keys.pkl", "rb") as f:
    keys = pickle.load(f)

# open the .pkl file called "capos.pkl"
with open("capos.pkl", "rb") as f:
    capos = pickle.load(f)


# create a new list of keys adjusted for the capo
# zip the two lists together
# if the capo is not None, call the function on each pair in the resulting iterable

adjusted_keys = []

for key, capo in zip(keys, capos):
    if capo == None:
        adjusted_keys.append(key)
    else:
        adjusted_keys.append(key_capo(key, capo))

# save the adjusted keys to a .pkl file
with open("adjusted_keys.pkl", "wb") as f:
    pickle.dump(adjusted_keys, f)

    