
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

categories = [
    'skincare',
    'makeup',
    'haircare',
    'fragrances',
    'personal care'
]

url = 'https://www.nykaa.com/'


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
    img_parent_div = soup.find(class_='productSelectedImage')
    img_tag = img_parent_div.find('img')
    image = img_tag.attrs['src']
    print(image)

    return {
        'name': name,
        'price': price,
        'description': description,
        'image': image
    }


def run_scrape_nykaa():
    # Initialize a web browser (e.g., Chrome)
    browser = webdriver.Chrome()

    # Open a web page
    browser.get(url)
    data = {}
    for category in categories:
        browser.switch_to.window(browser.window_handles[0])
        input_element = browser.find_element(
            By.NAME, 'search-suggestions-nykaa')
        input_element.clear()
        input_element.send_keys(category)
        # Simulate pressing the "Enter" key
        input_element.send_keys(Keys.ENTER)

        # Find a link by its class attribute
        links = browser.find_elements(By.CLASS_NAME, 'css-qlopj4')
        data[category] = []
        for link in links:
            browser.switch_to.window(browser.window_handles[0])
            link.click()
            # Switch to the new tab (assuming it's the last one opened)
            browser.switch_to.window(browser.window_handles[-1])
            page_source = browser.page_source
            entry = scrape_single_page(page_source)
            data[category].append(entry)
            browser.close()
    # Close the web browser when you're done
    browser.quit()
    return data


if __name__ == '__main__':
    run_scrape_nykaa()
