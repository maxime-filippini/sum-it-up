# Standard library imports
import re

from .base import ParserBase
from .loaders import PageLoader
from sumitup.structures import Article

# Third party imports
# Local imports


class IndexParser(ParserBase):
    root_url = "https://edition.cnn.com"

    def __init__(self, page_loader: PageLoader) -> None:
        self.page_loader = page_loader

    def parse(self, url: str):
        html = self.page_loader.url_to_html(url)

        headlines = html.find_all("h3", class_="cd__headline")
        re_no_videos = re.compile(r"\/videos\/")

        out = []

        for headline in headlines:
            link = headline.find("a")
            href = link["href"]

            if href.startswith("/"):
                if not re_no_videos.findall(href):
                    url = self.root_url + href
                    out.append(url)

        return out


class PageParser(ParserBase):
    def __init__(self, page_loader: PageLoader) -> None:
        self.page_loader = page_loader

    def parse(self, url: str):
        html = self.page_loader.url_to_html(url)

        headline_html = html.find_all("h1", class_="pg-headline")
        headline = headline_html[0].text

        paragraphs_html = html.find_all("div", class_="zn-body__paragraph")
        body = "\n".join([p.text for p in paragraphs_html])

        return Article(headline=headline, body=body, url=url)
