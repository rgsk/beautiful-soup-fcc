import os


def get_folder_path(filename):
    folder_path = 'src/scrape_nykaa_project/generated'
    # Ensure the folder exists, create it if necessary
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Create the CSV file
    file_path = os.path.join(folder_path, filename)
    return file_path


if __name__ == '__main__':
    print(get_folder_path('data.json'))
