import os
from glob import glob


def print_all_file_names(folder_name: str = None):
    """
    Print all file names from given folder name
    :param folder_name: Folder name to get the file names from, if not provided takes current folder
    :return: None, prints the file names
    """
    if folder_name is None:
        folder_name = os.getcwd()

    for filename in glob(folder_name + '\*'):
        print(os.path.basename(filename))


print_all_file_names(r'C:\Users\abhilashs\Desktop')
