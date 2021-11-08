from bs4 import BeautifulSoup
import requests
import re

ROOT_URL = "https://edition.cnn.com"
BUS_URL = ROOT_URL + "/business"

page = requests.get(BUS_URL)
soup = BeautifulSoup(page.content, "html.parser")

headlines = soup.find_all("h3", class_="cd__headline")
re_no_videos = re.compile("\/videos\/")

for headline in headlines:
    link = headline.find("a")

    if link["href"].startswith("/"):

        url = ROOT_URL + link["href"]

        if not re_no_videos.findall(url):
            article_page = requests.get(url)
            article_soup = BeautifulSoup(article_page.content, "html.parser")

            paragraphs = article_soup.find_all("div", class_="zn-body__paragraph")

            # Find text by looking for h tags
            # Normal paragraph are straight text in div
