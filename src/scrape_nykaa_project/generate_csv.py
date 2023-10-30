import csv

from scrape_nykaa_project.get_folder_path import get_folder_path


def generate_csv(data):
    for key in data:
        # Create the CSV file
        file_path = get_folder_path(f'{key}.csv')

        with open(file_path, mode='w', newline='') as file:
            fieldnames = data[key][0].keys()
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()

            for product in data[key]:
                writer.writerow(product)

        print(
            f'CSV file "{key}.csv" has been created and saved to {file_path}.')


if __name__ == '__main__':
    # Define the data
    data = {
        'dummy': [
            {
                'name': 'Rahul',
                'price': '123',
                'description': 'fdsfds',
                'image': 'imagfdse'
            }
        ]
    }
    generate_csv(data)
