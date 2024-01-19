from get_page_URLs import generate_list_of_chord_page_links
from get_song_info import get_song_info
from get_song_chords import get_song_chords

JAN24_CHORD_INDEX_PAGE = "https://www.ultimate-guitar.com/explore?type[]=Chords"
JAN24_COOKIES_BUTTON_CLASS = "css-197f1ny"
JAN24_CHORD_PAGE_LINK_CLASSNAME= "aPPf7 HT3w5 lBssT" # this may change, use the inspector to check

page_URLs = generate_list_of_chord_page_links(JAN24_CHORD_INDEX_PAGE, JAN24_COOKIES_BUTTON_CLASS, JAN24_CHORD_PAGE_LINK_CLASSNAME)

song_1_info = get_song_info(page_URLs[1])
print(song_1_info)

song_1_chords = get_song_chords(page_URLs[1], "fciXY _Oy28::after")
print(song_1_chords)