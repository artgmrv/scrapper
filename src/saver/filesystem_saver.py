import os
from .base import Saver


class FileSystemSaver(Saver):

    url_based_structure: bool = False
    file_name: str = "index.txt"

    def save(self, url: str, content: str):
        super().save(url, content)

        if self.url_based_structure:
            path = url[url.find('://') + 2:url.rfind('/')]
            filename = url[url.rfind('/'):]
        else:
            path = ''
            filename = f'/{self.file_name}'

        article_path = os.getcwd()
        try:
            os.chdir(article_path + path)
        except FileNotFoundError:
            os.makedirs(article_path + path)
        os.chdir(article_path + path)

        if filename == '/':
            filename = "/index.txt"
        f = open(article_path + path + filename, 'w')
        f.write(content)
        print('File was written: ' + article_path + path + filename)
        f.close()

