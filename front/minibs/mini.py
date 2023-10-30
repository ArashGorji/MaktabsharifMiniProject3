from pathlib import Path
import re

class Front:
    def sortUrl(self):
        images_folder = Path("images")
        files = sorted(images_folder.glob("*"))
        self.file_name = [file.name for file in files]
        for i in self.file_name:
            print(i)

    def showIIcon(self):
        pattern = r"(.+)-icon(-1)?\.[a-z]+"
        match_url = list(filter(lambda x: re.match(pattern, x), self.file_name))
        with open("icons.txt", "a+") as file:
            for i in match_url:
                file.write(i + "\n")
        print("Ok")


def main():
    front = Front()
    front.sortUrl()
    # front.showIIcon()


if __name__ == 'main':
    main()