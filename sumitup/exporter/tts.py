import re
from pathlib import Path
from typing import List

import gtts.tokenizer.pre_processors as pre_processors
from gtts import gTTS

from .base import ExporterBase
from sumitup.structures import Article


class TtsExporter(ExporterBase):
    def __init__(self, folder_path: str) -> None:
        self.preprocess = [
            pre_processors.tone_marks,
            pre_processors.end_of_line,
            pre_processors.abbreviations,
            pre_processors.word_sub,
        ]

        self.folder_path = folder_path

    def export_item(self, article: Article, path: str):
        def break_up(text):
            broken_up = []
            punc = [",", ";", ". ", " - ", "\n"]

            text = text.replace("\n", " ")
            text = re.sub(r"\s+", " ", text)
            text = text.strip()

            while text:
                if len(text) > 100:
                    next_100 = text[:100]
                    found = [next_100.rfind(p) for p in punc]

                    if max(found) <= 0:
                        idx = next_100.rfind(" ")

                    else:
                        idx = max(found)

                    broken_up.append(next_100[:idx])
                    text = text[idx + 1 :]

                else:
                    broken_up.append(text)
                    text = None

            return broken_up

        tts = [gTTS(txt) for txt in break_up(article.headline)] + [
            gTTS(txt) for txt in break_up(article.body)
        ]

        with open(path, "wb") as f:
            for t in tts:
                t.write_to_fp(f)

    def export_list(self, items: List[Article]):
        folder = Path(self.folder_path)

        for i, item in enumerate(items):
            self.export_item(article=item, path=folder / f"{i}.mp3")
