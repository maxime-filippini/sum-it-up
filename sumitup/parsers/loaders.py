# Standard library imports
import requests
from abc import ABC, abstractmethod

# Third party imports
from bs4 import BeautifulSoup
from requests_html import HTMLSession


class PageLoader(ABC):
    @abstractmethod
    def url_to_html(url: str):
        pass


class SimplePageLoader(PageLoader):
    def url_to_html(self, url: str):
        page = requests.get(url, timeout=(1, 1))
        return BeautifulSoup(page.content, "html.parser")


class JavascriptPageLoader(PageLoader):
    def url_to_html(self, url: str):
        session = HTMLSession()
        resp = session.get(url)
        resp.html.render()
        html = BeautifulSoup(resp.html.raw_html, "html.parser")
        return html
