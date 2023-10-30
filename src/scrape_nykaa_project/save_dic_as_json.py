import json
from typing import Dict

from scrape_nykaa_project.get_folder_path import get_folder_path


def save_dic_as_json(data: Dict[str, str], file_name: str):
    file_path = get_folder_path(file_name)

    # Save the data to a file
    with open(file_path, 'w') as file:
        json.dump(data, file)


def read_json_to_dic(file_name: str):
    file_path = get_folder_path(file_name)
    with open(file_path, 'r') as file:
        loaded_data = json.load(file)

    return loaded_data


if __name__ == '__main__':

    # Data to save to a file
    data = {
        'key1': 'value1 fdsds1234',
        'key2': 'value2',
        'key3': 'value3'
    }
    file_name = 'dummy.json'
    save_dic_as_json(data, file_name)
    print(read_json_to_dic(file_name))
