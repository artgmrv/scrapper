from .base import Formatter
from typing import List
from config.config import DEFAULT_TEXT_WIDTH


class SimpleFormatter(Formatter):
    """Класс для форматирования текствовых данных"""

    width: int = DEFAULT_TEXT_WIDTH

    def format(self, text: List[str]):
        merged = ''
        for par in text:
            # off = '     ' if offset else ''
            off = ''
            merged += self._format(off+par)+'\n'
        return merged

    def _format(self, text: str) -> str:
        result = ''
        if len(text) > self.width:
            current_width = text[0: self.width].rfind(' ')
            if current_width == -1:
                result = text[0: self.width-1]+'-'+'\n'
                result += self._format(text[self.width:])
            else:
                result = text[0:current_width]+'\n'
                result += self._format(text[current_width+1:])
        else:
            result += text+'\n'
        return result

