"""
pydantic will do data convertion
https://docs.pydantic.dev/usage/types/
"""
import time
from typing import List

from pydantic import BaseModel


class Image(BaseModel):
    url: str = None
    width: int = None
    height: int = None


class Article(BaseModel):
    article_id: int = None
    images: List[Image] = None
    error_msg : str = None

    @classmethod
    def from_api(cls, endpoint: str = None, api_error : bool = False):
        time.sleep(0.5)  # to simulate request
        if not api_error:
            fetched = {
            "article_id": "50",
            "images": [
                {"url": "i1", "width": "1", "height": "2"},
                {"url": "i2", "width": "3", "height": "4"},
                ],
            }

            return cls(**fetched)
        else:
            err = {"err_msg" :'您沒有權限'}
            return cls(**err)


    def infer_spark_schema():
        pass


print(Article.from_api())
print(dict(Article.from_api()), Article.from_api().dict(), Article.from_api().json(), sep="\n\n")
print(Article.from_api(api_error=True).dict())
