from get_page_URLs import generate_list_of_chord_page_links
from get_song_info import get_song_info
from get_song_chords import get_song_chords

JAN24_CHORD_INDEX_PAGE = "https://www.ultimate-guitar.com/explore?type[]=Chords"
JAN24_COOKIES_BUTTON_CLASS = "css-197f1ny"
JAN24_CHORD_PAGE_LINK_CLASSNAME= "aPPf7 HT3w5 lBssT" # this may change, use the inspector to check
test_chord_page= "https://tabs.ultimate-guitar.com/tab/ed-sheeran/perfect-chords-1956589"
counter = 0

page_URLs = generate_list_of_chord_page_links(JAN24_CHORD_INDEX_PAGE, JAN24_COOKIES_BUTTON_CLASS, JAN24_CHORD_PAGE_LINK_CLASSNAME)


# for every url, get the song info and the song chords
for song in page_URLs:
    song_num = counter
    get_song_info(song, song_num)
    get_song_chords(song, song_num)
    counter += 1



#song_1_info = get_song_info(page_URLs[1])
# print(song_1_info)

# # call get_song_info for the first link in the list



# get_song_info(page_URLs[0], 1)
# get_song_chords(page_URLs[0], 1)
# # get the song 
