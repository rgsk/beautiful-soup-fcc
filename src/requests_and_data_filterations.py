import requests
from bs4 import BeautifulSoup

url = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation='


def run_requests_and_data_filterations():
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    print(jobs[0])


if __name__ == '__main__':
    run_requests_and_data_filterations()
