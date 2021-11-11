from typing import List

from dotenv import dotenv_values
from notion.block import AudioBlock
from notion.block import DividerBlock
from notion.block import PageBlock
from notion.block import TextBlock
from notion.client import NotionClient

from .base import ExporterBase
from .tts import TtsExporter
from sumitup._notion.classes import ExtendedClient
from sumitup.structures import Article


class NotionExporter(ExporterBase):
    def __init__(self, audio_version=False) -> None:
        env_values = dotenv_values(".env")
        token = env_values.get("NOTION_TOKEN")
        page_url = env_values.get("NOTION_NEWS_PAGE")

        self.client = ExtendedClient(token_v2=token)
        self.page = self.client.get_block(page_url)

        if audio_version:
            self.audio_exporter = TtsExporter()
        else:
            self.audio_exporter = None

    def wipe_page(self):
        for child in self.page.children:
            child.remove()

    def export_list(self, items: List[Article]):
        self.wipe_page()

        for item in items:
            new_page = self.page.children.add_new(PageBlock, title=item.headline)
            new_page.icon = "📰"
            new_page.children.add_new(TextBlock, title=item.body)
            new_page.children.add_new(DividerBlock)
            new_page.children.add_new(TextBlock, title=f"[{item.url}]({item.url})")

            if self.audio_exporter:
                self.audio_exporter.export_item(article=item, path="data/_.mp3")
                audio_block = new_page.children.add_new(AudioBlock)
                audio_block.upload_file("data/_.mp3")
