import os
import re

num = 0
chords_lyrics = f"song_{num}_chords_lyrics.txt"
song_info = f"song_{num}_info.txt"

# navigate into scraped folder
current_dir = os.getcwd()
print(current_dir)

# if not in the scraped directory, change into it
if not current_dir.endswith('scraped'):
    os.chdir('scraped')


# pull the text info in from the chords_lyrics file
with open(chords_lyrics, "r", encoding='utf-8') as f:
    chords_lyrics = f.read()

# print(chords_lyrics)
    
#get first chord. extract all text up to the first instance of [/ch]
first_chord = re.findall(r'(.*?)\[\/ch\]', chords_lyrics, re.I)[0]
print(first_chord)

# ? important here. non-greedy match so will match as few characters as possible between ch tags. Gets just the chords rather than the whole thing
chords = re.findall(r'\[ch\](.*?)\[\/ch\]', chords_lyrics, re.I)

#append the first chord to the start of the chords list
chords.insert(0, first_chord)

print(chords)

print(type(chords))
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

