from dataclasses import dataclass
from dataclasses import field
from typing import List


@dataclass
class Article:
    headline: str
    body: str
    url: str
    sentences: List[str] = field(default_factory=list)
