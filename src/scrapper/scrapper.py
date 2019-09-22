from .base import Scrapper
from typing import List


class SimpleScrapper(Scrapper):
    """Класс управления процессом извлечения информации из html"""

    def process(self, urls):
        """Основной метод обработки"""
        for url in urls:
            page_content = self._loader.pull(url)
            extractor = self._extractor_class(page_content)
            text: List[str] = extractor.text(80)
            text = self._formatter.format(text)
            self._saver.save(url, text)
