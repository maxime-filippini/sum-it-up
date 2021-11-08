# Standard library imports
from abc import ABC
from abc import abstractmethod
from collections import Counter

# Third party imports
import spacy
from spacy.lang.en.stop_words import STOP_WORDS

# Main body
class Model:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")
        self.stop_words = list(STOP_WORDS)
        self.punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~" + "\n"


class FrequencySummarizer(Model):
    def tokens(self, doc):
        return [
            token.text.lower()
            for token in doc
            if (token.text.lower() not in self.stop_words)
            and (token.text not in self.punctuation)
        ]

    def run(self, text: str):
        doc = self.nlp(text)

        tokens = self.tokens(doc)

        counter = Counter(tokens)
        n = len(tokens)

        sents = [
            {
                "sent": sent,
                "score": sum([counter[word.text.lower()] for word in sent]) / n,
            }
            for sent in doc.sents
        ]

        top_sents = sorted(sents, key=lambda x: x["score"], reverse=True)[:5]
        out_sents = [sent["sent"].text for sent in sents if sent in top_sents]

        return "\n".join(out_sents)
