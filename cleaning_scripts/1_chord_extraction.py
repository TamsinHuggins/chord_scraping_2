#  this file contains 2 functions: get_chords and get_lyrics
# these functions are able to work through all the song_x_chords_lyrics.txt files from Ultimate Guitar, 
# which are located in the scraped folder.
# get_chords will take in the song number and return just a list of chords for that song.
# this funciton is called on batches of 1000 songs, generating 1000 lists for each batch.
# the resulting lists of lists are saved as pkl files such as chords_songs_0-999.pkl.



import os
import re
import pickle

num = 0

# navigate into scraped folder
current_dir = os.getcwd()

# if not in the scraped directory, change into it
if not current_dir.endswith('scraped'):
    os.chdir('scraped')

#  try with 100 songs

def get_chords(song_num):
    chords_lyrics = f"song_{num}_chords_lyrics.txt"

    # pull the text info in from the chords_lyrics file

    with open(chords_lyrics, "r", encoding='utf-8') as f:
        chords_lyrics = f.read()
        
    #get first chord. extract all text up to the first instance of [/ch]
    first_chord = re.findall(r'(.*?)\[\/ch\]', chords_lyrics, re.I)[0]

    # ? important here. non-greedy match so will match as few characters as possible between ch tags. Gets just the chords rather than the whole thing
    chords = re.findall(r'\[ch\](.*?)\[\/ch\]', chords_lyrics, re.I)

    #append the first chord to the start of the chords list. inplace operation.
    chords.insert(0, first_chord)
    
    # use join method to convert to a string
    return chords



# batching into a thousand songs at a time
song_ranges = [[0,1000],[1000,2000],[2000,3000],[3000,4956]]

for song_range in song_ranges:
    chords_1000_songs = []
    #for every song in the range, get the chords (example range is 0-1000)
    for num in range(song_range[0], song_range[1]):
        try:
            chords_1000_songs.append(get_chords(num))
            print(f"Got chords for song {num}")
        except:
            print(f"Error with song {num}")

    #use pickle to save the list of chords to a file
    with open(f'chords_songs_{song_range[0]}-{song_range[1]-1}.pkl', 'wb') as f:
        pickle.dump(chords_1000_songs, f)
    print(f"Saved chords_songs_{song_range[0]}-{song_range[1]-1}.pkl")





def get_lyrics(song_num):
    chords_lyrics = f"song_{num}_chords_lyrics.txt"
    # remove all text enclosed between [ch] and [/ch] tags, including the tags themselves
    lyrics = re.sub(r'\[ch\](.*?)\[\/ch\]', '', chords_lyrics)

    #remove from lyrics any instances of [/tab],[tab] \r and\n
    lyrics = re.sub(r'\[\/tab\]', '', lyrics)
    lyrics = re.sub(r'\[tab\]', '', lyrics)
    lyrics = re.sub(r'\\r', '', lyrics)
    lyrics = re.sub(r'\\n', '', lyrics)
    #remove any instances of more than 6 consecutive spaces with a comma
    lyrics = re.sub(r'\s{6,}', ', ', lyrics)

    #remove any instanse of [Interlude]
    lyrics = re.sub(r'\[Interlude\]', '', lyrics)

    #remove any instances of Verse 1, Verse 2, etc.
    lyrics = re.sub(r'\[Verse \d\]', '', lyrics)

    #remove sny instanves of [Chorus]
    lyrics = re.sub(r'\[Chorus\]', '', lyrics)

    #remove any instances of [Bridge]
    lyrics = re.sub(r'\[Bridge\]', '', lyrics)

    #remove any instances of [Outro]
    lyrics = re.sub(r'\[Outro\]', '', lyrics)

    return lyrics






