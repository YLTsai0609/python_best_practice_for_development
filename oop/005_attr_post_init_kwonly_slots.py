from typing import Optional

import attr

# slots is an advance feature in dataclass, only python 3.10+....
# attr has it.
# immutable = attr.s(auto_attribs=True, frozen=True, kw_only=True, slots=True)
immutable = attr.define(auto_attribs=True, frozen=True, kw_only=True, slots=True)


@attr.define(auto_attribs=True, frozen=True, kw_only=True, slots=True)
class Spreadsheet:
    sheet_id: str
    gid: int = 0
    schema: Optional[dict] = {}
    share_url: str = attr.ib(init=False)
    download_url: str = attr.ib(init=False)

    def __attrs_post_init__(self):
        # https://www.attrs.org/en/stable/init.html
        # setattr, then frozen
        object.__setattr__(
            self, "share_url", f"https://abc/{self.sheet_id}/edf/{self.gid}"
        )
        object.__setattr__(
            self, "download_url", f"https://zxc/{self.sheet_id}/pdq/{self.gid}"
        )
        # self.share_url = f"https://abc/{self.sheet_id}/edf/{self.gid}"

    # @property
    # def share_url(self)
    #     return f"https://abc/{self.sheet_id}/edf/{self.gid}"


s1 = Spreadsheet(sheet_id=1, schema={"poi_name": str})

print(s1)
