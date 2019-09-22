from abc import ABCMeta, abstractmethod


class Saver:
    __metaclass__ = ABCMeta

    @abstractmethod
    def save(self, url: str, content: str) -> str:
        """Сохранение данных"""
