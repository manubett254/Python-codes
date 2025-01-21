# 8. File Organizer by Extension (Moves files into folders by type)
import os
import shutil

def organize_files(directory):
    for file in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, file)):
            ext = file.split('.')[-1]
            folder = os.path.join(directory, ext)
            os.makedirs(folder, exist_ok=True)
            shutil.move(os.path.join(directory, file), os.path.join(folder, file))

directory = input("Enter the directory to organize: ")
organize_files(directory)
