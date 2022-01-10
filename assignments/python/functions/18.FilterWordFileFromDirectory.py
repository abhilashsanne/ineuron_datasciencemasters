import os
import pathlib
from glob import glob


def print_all_file_names(folder_name: str = None):
    """
    Print all word document file names from given folder name
    :param folder_name: Folder name to get the file names from, if not provided takes current folder
    :return: None, prints the word file names
    """
    if folder_name is None:
        folder_name = os.getcwd()

    for filename in glob(folder_name + '\*'):
        if os.path.isfile(filename):
            if pathlib.Path(filename).suffix.lower() in [".doc", ".docx", ".docm", ".dot", ".dotx"]:
                print(os.path.basename(filename))


print_all_file_names(r'C:\Users\abhilashs\Desktop')
