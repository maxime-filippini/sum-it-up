# Standard library imports
import re

from .base import ParserBase
from .loaders import PageLoader
from sumitup.structures import Article

# Third party imports
# Local imports


class IndexParser(ParserBase):
    root_url = "https://bbc.com"

    def __init__(self, page_loader: PageLoader) -> None:
        self.page_loader = page_loader

    def parse(self, url: str):
        html = self.page_loader.url_to_html(url)
        for header in html.find_all(("header", "nav")):
            header.decompose()

        links = html.find_all("a")

        re_ = re.compile(r"(\/news)(?!\/live\/).*[0-9]")
        out = []

        def is_valid_link(link):
            href = link["href"]
            entity_id = link.get("data-entityid", "")
            play_bullet = link.find("span", class_="nw-o-bullet__icon")
            icons = [
                item
                for item in link.find_all("span")
                if "video" in item.get("data-icon", "")
            ]

            return (
                re_.match(href) is not None
                and ("heading" not in entity_id)
                and (not play_bullet)
                and (not icons)
            )

        for link in links:
            href = link["href"]
            if is_valid_link(link):
                out.append(self.root_url + href)

        return list(set(out))


class PageParser(ParserBase):
    def __init__(self, page_loader: PageLoader) -> None:
        self.page_loader = page_loader

    def parse(self, url: str):
        html = self.page_loader.url_to_html(url)

        article = html.find("article")
        headline_html = article.find("b")
        headline = headline_html.text
        headline_html.decompose()

        paragraphs_html = [
            item
            for item in article.find_all("div")
            if item.get("data-component", "") == "text-block"
        ]
        body = "\n".join([p.text for p in paragraphs_html if p.text])

        return Article(headline=headline, body=body, url=url)
