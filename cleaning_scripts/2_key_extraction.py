
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
capo_infos = []
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
        except:
            key = None
            
            print(f"Error with file {file_name}")
            continue

        keys.append(key)

        # access the text key and save its value to a variable
        # use re to find all text after the word "Capo:" and save to a variable
        
        capo_info = re.findall(r'Capo: (.*)', song_info['text'])
        # if capo_info contains any of the numbers 1,2,3,4,5,6,7,8,9,10,11,12, then save the first number to the capo_info variable
        try:
            capo_info = int(re.findall(r'\d+', capo_info[0])[0])
        except:
            capo_info = None

        # append capo info to capo_infos
        capo_infos.append(capo_info)
        
# use pickle to save the list of keys to a file
with open('keys.pkl', 'wb') as f:
    pickle.dump(keys, f)

# use pickle to save the capo_infos list to a file
with open('capos.pkl', 'wb') as f:
    pickle.dump(capo_infos, f)



