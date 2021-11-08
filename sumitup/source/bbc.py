from .base import SourceBase
import sumitup.parsers.bbc as bbc
from sumitup.parsers.loaders import SimplePageLoader

from bs4 import BeautifulSoup


class BbcNewsSource(SourceBase):
    index_url = "https://www.bbc.com/news"
    index_parser = bbc.IndexParser(page_loader=SimplePageLoader())
    page_parser = bbc.PageParser(page_loader=SimplePageLoader())
