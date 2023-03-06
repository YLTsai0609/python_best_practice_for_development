from functools import wraps

import attr


class BasicColor:
    def __init__(self, r):
        self.r = r


# # worked


@attr.s
class AttrColor1:
    """Some docx"""

    r: int


# eq

some_rename = attr.s(auto_attribs=True)


@some_rename
class AttrColor2:
    r: int


# apply function@wrap here
