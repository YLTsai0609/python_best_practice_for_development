"""
use attr for more eligant and time saving OOP programming

introduction 1 : https://blog.csdn.net/HHG20171226/article/details/103038077
introduction 2 : https://zhuanlan.zhihu.com/p/66267212

github : https://github.com/python-attrs/attrs

attr.s (s for self)
attr.ib (ib for attribute ? )

kw_only - set variable of class using keyword only
slots=True - use __slot__ for attributes(it's will be faster when you are creating short-lifetime object)

"""
import os

import attr


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
