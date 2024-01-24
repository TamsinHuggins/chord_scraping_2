from bs4 import BeautifulSoup
import requests
# URL = 'https://tabs.ultimate-guitar.com/tab/ed-sheeran/perfect-chords-1956589'
URL = "https://tabs.ultimate-guitar.com/tab/noah-kahan/stick-season-chords-4271572"
response = requests.get(URL)

page = response.text

pagesoup = BeautifulSoup(page, "html.parser")

script_tag = pagesoup.find_all('script', type='application/ld+json')

script_tag =list(script_tag)

print(script_tag[1])

# # Access the JSON data inside the script tag
# if script_tag:
#     json_data = script_tag.string
#     # You now have the JSON data as a string

#     # You can parse it into a Python dictionary using a JSON library like json
#     import json
#     data = json.loads(json_data)

#     # Now you can access the data in the JSON object
#     print(data['name'])
#     # print(data['composer']['name'])
#     print(data['datePublished'])
#     print(data['dateModified'])
#     print(data['musicalKey'])
# else:
#     print("Script tag not found.")