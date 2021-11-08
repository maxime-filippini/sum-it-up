from abc import abstractmethod
from typing import List

from .base import SourceBase
import sumitup.parsers.cnn as cnn
from sumitup.parsers.loaders import SimplePageLoader
from sumitup.parsers.loaders import JavascriptPageLoader


class CnnBusinessSource(SourceBase):
    index_url = "https://edition.cnn.com/business"
    index_parser = cnn.IndexParser(page_loader=SimplePageLoader())
    page_parser = cnn.PageParser(page_loader=SimplePageLoader())


class CnnEntertainmentSource(SourceBase):
    index_url = "https://edition.cnn.com/entertainment"
    index_parser = cnn.IndexParser(page_loader=SimplePageLoader())
    page_parser = cnn.PageParser(page_loader=SimplePageLoader())


class CnnPoliticsSource(SourceBase):
    index_url = "https://edition.cnn.com/politics"
    index_parser = cnn.IndexParser(page_loader=JavascriptPageLoader())
    page_parser = cnn.PageParser(page_loader=SimplePageLoader())
