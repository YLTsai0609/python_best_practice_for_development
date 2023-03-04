"""
pydantic will do data convertion
https://docs.pydantic.dev/usage/types/
"""
import time
from typing import List

from pydantic import BaseModel


class Image(BaseModel):
    url: str
    width: int
    height: int


class Article(BaseModel):
    article_id: int
    images: List[Image]

    @classmethod
    def from_api(cls, endpoint: str = None):
        time.sleep(0.5)  # to simulate request

        fetched = {
            "article_id": "50",
            "images": [
                {"url": "i1", "width": "1", "height": "2"},
                {"url": "i2", "width": "3", "height": "4"},
            ],
        }

        return cls(**fetched)

    def infer_spark_schema():
        pass


print(Article.from_api())
print(dict(Article.from_api()), Article.from_api().dict(), Article.from_api().json(), sep="\n\n")
