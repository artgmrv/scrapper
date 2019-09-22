from abc import ABCMeta, abstractmethod
from typing import List
from config.config import BS_TAG


class BaseExtractor:
    __metaclass__ = ABCMeta

    @abstractmethod
    def text(self, max_width: int) -> List[str]:
        """Получение основной информации со страницы в виде списка"""

    @staticmethod
    def extract_text_from_node(node):
        text = ''
        for sub_node in node:
            if str(type(sub_node)) == BS_TAG:
                text += BaseExtractor.extract_text_from_node(sub_node)
                if sub_node.name == 'a':
                    text += ' [' + sub_node['href'] + ']'
            else:
                text += sub_node
        return text
