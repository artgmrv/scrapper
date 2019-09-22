from abc import ABCMeta, abstractmethod
from typing import List, Type

from src.extractor.base import BaseExtractor
from src.loader.base import Loader
from src.saver.base import Saver
from src.formatter.base import Formatter

Urls = List[str]


class Scrapper:
    """Класс для извлечение полезной информации из веб страницы"""
    __metaclass__ = ABCMeta

    _extractor_class: Type[BaseExtractor] = None
    _loader: Type[Loader] = None
    _saver: Type[Saver] = None
    _formatter: Type[Formatter] = None

    def __init__(
        self,
        extractor_class: Type[BaseExtractor],
        loader: Type[Loader],
        saver: Type[Saver],
        formatter: Type[Formatter],
    ):
        self._extractor_class = extractor_class
        self._loader = loader
        self._saver = saver
        self._formatter = formatter

    @abstractmethod
    def process(self, url: Urls):
        """Обработка url"""

