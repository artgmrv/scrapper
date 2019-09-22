from bs4 import BeautifulSoup
from .base import BaseExtractor
from config.config import ANCHOR_TAG, BS_TAG, GRAPH_UP_COUNT
from typing import List


class Element:
    node = None
    cnt = 1


class GraphExtractor(BaseExtractor):
    """Класс для извлечения основной информации из html"""

    @staticmethod
    def extract_text_from_node(node):
        text = ''
        for sub_node in node:
            if str(type(sub_node)) == BS_TAG:
                if sub_node.name not in ['div', 'p', 'section', 'span', 'a']:
                    continue
                text += GraphExtractor.extract_text_from_node(sub_node)
                if sub_node.name == 'a' and 'href' in sub_node:
                    text += ' [' + sub_node['href'] + ']'
            else:
                rr = sub_node.strip()
                if rr != "" and rr != "\n\r" and rr != "\n" and rr != "\r\n":
                    text += sub_node
        return text

    @staticmethod
    def _extract_paragraphs(html: str) -> List[str]:
        """Извлечение параграфов из html"""
        paragraphs = []
        # try:
        tree: dict = {}
        soup = BeautifulSoup(html, 'html5lib')
        block = soup.find(ANCHOR_TAG)
        paragraphs.append(GraphExtractor.extract_text_from_node(block))

        paragraph_nodes = soup.find_all('p')
        # paragraph_nodes += soup.find_all('span')
        # paragraph_nodes += soup.find_all('div')
        for node in paragraph_nodes:
            txt = GraphExtractor.extract_text_from_node(node)
            if txt == "":
                continue
            i = 0
            current = node
            while i < GRAPH_UP_COUNT:
                i += 1
                current = current.parent
                h = id(current)
                if h in tree:
                    tree[h].cnt += 1
                else:
                    tree[h] = Element()
                    tree[h].node = current

        max_val = 0
        node_with_max_paragraphs = None
        for h, node in tree.items():
            if node.cnt > max_val:
                max_val = node.cnt
                node_with_max_paragraphs = node.node

        # current = node_with_max_paragraphs
        # while True:
        #     current = current.next
        #     if current is None:
        #         break
        #     sub_node_text = GraphExtractor.extract_text_from_node(current)
        #     paragraphs.append(sub_node_text)

        for sub_node in node_with_max_paragraphs:
            sub_node_text = GraphExtractor.extract_text_from_node(sub_node)
            paragraphs.append(sub_node_text)

        return paragraphs

    def __init__(self, content: str):
        super(GraphExtractor, self).__init__()
        self._content = content
        self._paragraphs = self._extract_paragraphs(content)

    def text(self, max_width: int) -> List[str]:
        """Представить страницу в виде текста"""
        return self._paragraphs
