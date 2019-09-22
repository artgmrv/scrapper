from bs4 import BeautifulSoup
from .base import BaseExtractor
from config.config import ANCHOR_TAG, TEXT_WRAPPER_TAG, \
    ANCHOR_DEEPNESS, MIN_PARAGRAPH_COUNT, BS_TAG
from typing import List


class Extractor(BaseExtractor):
    """Класс для извлечения основной информации из html"""

    @staticmethod
    def _extract_paragraphs(html: str) -> List[str]:
        """Извлечение параграфов из html"""
        paragraphs = []
        try:
            soup = BeautifulSoup(html, 'html5lib')
            block = soup.find(ANCHOR_TAG)
            paragraphs.append(Extractor.extract_text_from_node(block))
            i = 0
            while i < ANCHOR_DEEPNESS:
                i += 1
                block = block.parent
                node = block.find_all(TEXT_WRAPPER_TAG)
                if len(node) > MIN_PARAGRAPH_COUNT:
                    break
            for sub_node in node:
                sub_node_text = Extractor.extract_text_from_node(sub_node)
                paragraphs.append(sub_node_text)
            return paragraphs
        except:
            return []

    def __init__(self, content: str):
        super(Extractor, self).__init__()
        self._content = content
        self._paragraphs = self._extract_paragraphs(content)

    def text(self, max_width: int) -> List[str]:
        """Представить страницу в виде текста"""
        return self._paragraphs
