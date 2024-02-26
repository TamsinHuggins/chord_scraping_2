
import os
import re
import pickle

song_num = 0
file_name = f"song_{song_num}_info.txt"

# navigate into scraped folder
os.chdir('scraped')

# for every song_x_info.txt file, parse the file as a dictionary and accsss the musicalKey
# then save the key to a list
keys = []
for song_num in range(0, 4956):
    file_name = f"song_{song_num}_info.txt"
    with open(file_name, 'r') as f:
        song_info = f.read()

        #try to parse the file as a dictionary
        # if it fails, print the file name and the error 
        # then pass to the next file
        try:
            song_info = eval(song_info)
        except:
            song_info = {}
            print(f"Error with file {file_name}")
            continue

        #try to access the musicalKey. If it fails, print the file name and the error
        # then pass to the next file
        try:
            key = song_info['musicalKey']
            keys.append(key)
        except:
            key = None
            keys.append(key)
            print(f"Error with file {file_name}")
            continue

# use pickle to save the list of keys to a file
with open('keys.pkl', 'wb') as f:
    pickle.dump(keys, f)