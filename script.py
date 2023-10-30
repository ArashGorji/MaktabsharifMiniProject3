from pathlib import Path
from subprocess import PIPE, run
from typing import List
import os
from check_icon import check_icon
from colortext import cstr
import re

# copy or moves icons from icons.txt details to desired path
def displace_icons(input_txt: Path, dest_path: Path, mode="copy"):
    if mode == "copy":
        command = "cp"
    elif mode == "move":
        command = "mv"

    check_icon(dest_path)

    with open(input_txt, 'r') as fp:
        files = fp.readlines()
        for file in files:
            result = run([command, file.replace("\n", ""), dest_path], stdout=PIPE, stderr=PIPE,
                         universal_newlines=True, shell=False)
            print(result.stderr) if result.returncode == 1 else ...
        print(cstr(f"{mode} done!","OKGREEN")) if result.returncode == 0 else print(cstr(f"{mode} failed!","WARNING"))


# icons to txt function
def icon_paths_to_txt(icon_list: List, export_file: Path):

    with open(export_file, "w") as fp:  # creates an icons.txt file, remove and recreate if exists!
        for icon in icon_list:
            # store absolute path of icons in each line
            fp.write(str(icon) + "\n")



def replace_file_content(file_utf8: Path, pattern, repr):
    with open(file_utf8,"r+") as fp:
        temp = fp.read()
        temp2 = re.sub(pattern, repr, temp)
        fp.seek(0)
        fp.write(temp2)
        fp.truncate()



# setting paths
project_path = Path("front")
images_path : Path = project_path / 'images'
icons_txt = Path("Icons.txt")
icons_dest_path = project_path / "icons"


# listing png files
images_list = list(images_path.glob("*"))

# sorting icons list
images_list.sort()

# printing icons

print(cstr("list of all files in images folder:","OKBLUE"))
for index, image in enumerate(images_list):
    print(cstr(f"\t{index+1}.{image.name}","OKBLUE"))


# listing png files where 'icon' included
icons_list = list(images_path.glob('*icon*.png'))

# sorting icons list
icons_list.sort()


icon_paths_to_txt(icons_list, icons_txt)
displace_icons(icons_txt, icons_dest_path, 'copy')



pattern = r'(?<=src=\")images(?=.*icon)'


html_list = list(project_path.glob("*.html"))


for html in html_list:
    replace_file_content(html,pattern,"icons")




