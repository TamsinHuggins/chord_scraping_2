
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


def generate_list_of_chord_page_links(index_url, cookie_class, link_classname):
    """Given a URL to a chord index page, returns a list of links to the individual chord pages."""
        
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)

    #open the page using the URL
    driver.get(index_url)

    # implicit wait for cookies pop-up
    driver.implicitly_wait(10)

    # find the first element with the class  css-197f1ny and click it
    driver.find_element(By.CLASS_NAME, cookie_class).click()

    # # get the page source
    page_source = driver.page_source
    MAIN_SOUP = BeautifulSoup(page_source, 'html.parser')

    #takes in a link containing a list of pages, finds all links to chord pages, returns list of these links.
    links_to_chord_page = MAIN_SOUP.find_all('a', { 'class' : link_classname}, href=True)
    list_of_chord_page_links = []
    for chord_page in links_to_chord_page:
        list_of_chord_page_links.append(chord_page['href'])

    #quit the driver and give out the list of links
    driver.quit()
    return list_of_chord_page_links