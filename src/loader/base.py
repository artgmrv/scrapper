from abc import ABCMeta, abstractmethod


class Loader:
    __metaclass__ = ABCMeta

    @staticmethod
    @abstractmethod
    def pull(url: str)->str:
        """Получение страницы"""
