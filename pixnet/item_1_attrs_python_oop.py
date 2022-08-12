"""
use attr for more eligant and time saving OOP programming

introduction 1 : https://blog.csdn.net/HHG20171226/article/details/103038077
introduction 2 : https://zhuanlan.zhihu.com/p/66267212

github : https://github.com/python-attrs/attrs
official document : attrs.org/en/stable/

attr.s (s for self)
attr.ib (ib for attribute ? )

auto_attribs : lay off self stuff
forzen : make the instance immutable when it initilized
kw_only :  set variable of class using keyword only
slots = True : use __slot__ for attributes(it's will be faster when you are creating short-lifetime object)

"""
import os
<<<<<<< HEAD
from typing import List
=======
from typing import Optional

>>>>>>> d2b61ecee4340269db14f3ec4e098f9a1e38fed7
import attr

immutable = attr.s(auto_attribs=True, frozen=True, kw_only=True, slots=True)


class Color:
    """
    Color Object for RGB
    """

    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def __repr__(self):
        return f"{self.__class__.__name__}(r={self.r}, g={self.g}, b={self.b})"

    def __lt__(self):
        pass

    def __eq__(self):
        pass


# automatic generate __init__, __repr__, __eq__,
# __ne__, __lt__, __le__, __gt__, __ge__, __hash__

# __ge__ greater equal
# __gt__ geater than


@attr.s
class GreaterColor(object):
    r = attr.ib(default=255, type=int)
    g = attr.ib(default=255, type=int)
    b = attr.ib(default=255, type=int)


@attr.s(frozen=True, auto_attribs=True)
class DataUri:
    basename: str = attr.ib(converter=str)
    prefix: str = attr.ib(converter=str)

    @property
    def fullpath(self):
        return os.path.join(self.prefix, self.basename)


c1 = Color(255, 255, 255)
print(c1)
c2 = GreaterColor()
print(c2)  # automatic generate __repr__
print(attr.asdict(c2))  # __dict__
print(c2 == GreaterColor(255, 255, 255))  # __eq__
print(c2 > GreaterColor(255, 254, 0))  # __le__

print(c2.__class__.__name__, dir(c2))
print()
print(c1.__class__.__name__, dir(c1))


d1 = DataUri(basename="abc.py", prefix="root")
print(d1, d1.fullpath)
# d1.basename = 4  # raise frozen error


# @attr.s
# class C:
#     x = attr.ib()
#     y = attr.ib()
#     z = attr.ib()

#     @z.default
#     def z_default(self, attribute):
#         return self.x + self.y


# @attr.s
# class C(object):
#     x: attr.ib()
#     y = attr.ib(init=False)

#     def __attrs_post_init__(self):
#         self.y = self.x + 1


# print(C(x=1))


@immutable
class Spreadsheet:
    sheet_id: str
    gid: int = 0
    schema: Optional[dict] = {}
    share_url: str = attr.ib(init=False)
    download_url: str = attr.ib(init=False)

    def __attrs_post_init__(self):
        # https://www.attrs.org/en/stable/init.html
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


s1 = Spreadsheet(sheet_id="a", schema={"poi_name": str})

print(s1)
