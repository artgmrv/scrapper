import requests
from requests.exceptions import ConnectionError
from .base import Loader


class WebLoader(Loader):
    """Загрузчик данных из сети"""

    @staticmethod
    def pull(url: str)->str:
        """Получение страницы по адресу"""
        try:
            response = requests.get(url)
            return response.content
        except ConnectionError:
            return ""
