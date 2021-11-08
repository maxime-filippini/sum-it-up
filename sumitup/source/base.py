from abc import ABC
from abc import abstractmethod
from typing import List
from bs4 import BeautifulSoup


class SourceBase(ABC):
    @property
    @abstractmethod
    def index_url(self):
        pass

    @property
    @abstractmethod
    def index_parser(self):
        pass

    @property
    @abstractmethod
    def page_parser(self):
        pass

    @abstractmethod
    def get_page_urls(self):
        pass

    @abstractmethod
    def parse_pages(self, page_urls: List[str]):
        pass

    def get_page_urls(self):
        return self.index_parser.parse(url=self.index_url)

    def parse_pages(self, page_urls: List[str]):
        for url in page_urls:
            yield self.page_parser.parse(url=url)
