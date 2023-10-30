import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://www.nykaa.com/skin/c/8377?search_redirection=True'


def scrape_single_page(page_source):
    soup = BeautifulSoup(page_source, 'lxml')

    h1_tag = soup.find('h1')
    name = h1_tag.text
    print(name)

    price_tag = soup.find(class_='css-1jczs19')
    price = price_tag.text
    print(price)

    div_content_details = soup.find(id='content-details')
    description = ""
    if div_content_details:
        description = div_content_details.text
    # print(description)


def run_scrape_nykaa():
    # Initialize a web browser (e.g., Chrome)
    browser = webdriver.Chrome()

    # Open a web page
    browser.get(url)

    time.sleep(1)

    # Find a link by its class attribute
    links = browser.find_elements(By.CLASS_NAME, 'css-qlopj4')

    for link in links:
        browser.switch_to.window(browser.window_handles[0])
        link.click()
        # Switch to the new tab (assuming it's the last one opened)
        browser.switch_to.window(browser.window_handles[-1])
        page_source = browser.page_source
        scrape_single_page(page_source)
        browser.close()

    # Add a delay to keep the browser open for a specified period (e.g., 10 seconds)
    time.sleep(1000000)

    # Close the web browser when you're done
    # browser.quit()


if __name__ == '__main__':
    run_scrape_nykaa()
