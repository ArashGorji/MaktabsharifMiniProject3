from pathlib import Path
import os
from colortext import cstr
def check_icon(dest_path):
    if not dest_path.exists():  # check if icons path not exists
        dest_path.mkdir()  # create icons path if exists
    if os.listdir(dest_path) != []:
        print(cstr(f"There is some files in {dest_path}","WARNING",bold=True))
        while True:
            prompt = input(
                cstr("Do you want to delete all files in icons folder? [y/n]: ","WARNING",bold=True))
            if prompt == "y":
                for child in dest_path.glob('*'):
                    child.unlink()
                print(cstr("files deleted!","OKGREEN"))
                break
            elif prompt == "n":
                break
            else:
                pass