from get_page_URLs import generate_list_of_chord_page_links
from get_song_info import get_song_info
from get_song_chords import get_song_chords

# JAN24_CHORD_INDEX_PAGE = "https://www.ultimate-guitar.com/explore?type[]=Chords"
JAN24_COOKIES_BUTTON_CLASS = "css-197f1ny"
JAN24_CHORD_PAGE_LINK_CLASSNAME= "aPPf7 HT3w5 lBssT" # this may change, use the inspector to check
test_chord_page= "https://tabs.ultimate-guitar.com/tab/ed-sheeran/perfect-chords-1956589"
counter = 0 # this number will label the song files


for num in range(1, 4900): # num refers to the index page number
    #try to generate a list of page URLs, if failed continue to the next page
    try:
        page_URLs = generate_list_of_chord_page_links(f"https://www.ultimate-guitar.com/explore?page={num}&type[]=Chords", JAN24_COOKIES_BUTTON_CLASS, JAN24_CHORD_PAGE_LINK_CLASSNAME)
    except:
        continue
    # for every url, get the song info and the song chords
    for song in page_URLs:
        song_num = counter
        # try to call both functions, if failed continue to the next song
        try:
            get_song_info(song, song_num)
            get_song_chords(song, song_num)
        except:
            continue
        counter += 1

