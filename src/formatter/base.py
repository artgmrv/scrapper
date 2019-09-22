from abc import ABCMeta, abstractmethod


class Formatter:
    __metaclass__ = ABCMeta

    @abstractmethod
    def format(self, text: str)->str:
        """Получение страницы"""
