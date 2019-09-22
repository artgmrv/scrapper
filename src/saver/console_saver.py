from .base import Saver
import time


class ConsoleSaver(Saver):
    """Класс для вывода текста в консоль c возможностью постепенного вывода"""

    def __init__(self, pause: bool = False):
        super().__init__()
        self._pause = pause

    def save(self, url: str, content: str):
        if self._pause:
            arr = content.splitlines()
            for row in arr:
                print(row)
                time.sleep(1)
        else:
            print(content)
        return super().save(url, content)
