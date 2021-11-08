from abc import ABC, abstractmethod
from bs4 import BeautifulSoup


class ParserBase(ABC):
    @abstractmethod
    def parse(html: BeautifulSoup):
        pass
