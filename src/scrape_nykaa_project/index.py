
from scrape_nykaa_project.generate_csv import generate_csv
from scrape_nykaa_project.save_dic_as_json import save_dic_as_json
from scrape_nykaa_project.scrape_nykaa import run_scrape_nykaa


def scrape_and_save_nykaa():
    # Load the data from the file
    data = run_scrape_nykaa()
    save_dic_as_json(data, 'data.json')

    generate_csv(data)


if __name__ == '__main__':
    scrape_and_save_nykaa()
