"""
use attr for more eligant and time saving OOP programming

introduction 1 : https://blog.csdn.net/HHG20171226/article/details/103038077
introduction 2 : https://zhuanlan.zhihu.com/p/66267212

github : https://github.com/python-attrs/attrs

"""
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


# automatic generate __init__, __repr__, __eq__, __ne__, __lt__, __le__, __gt__, __ge__, __hash__

# __ge__ greater equal
# __gt__ geater than


@attr.s
class GreaterColor(object):
    r = attr.ib(default=255, type=int)
    g = attr.ib(default=255, type=int)
    b = attr.ib(default=255, type=int)


c1 = Color(255, 255, 255)
print(c1)
c2 = GreaterColor()
print(c2)  # automatic generate __repr__
print(attr.asdict(c2))  # __dict__
print(c2 == GreaterColor(255, 255, 255))  # __eq__
print(c2 > GreaterColor(255, 254, 0))  # __le__

print(c2.__class__.__name__, dir(c2))
print(attr.fields(c2))
print()
print(c1.__class__.__name__, dir(c1))
