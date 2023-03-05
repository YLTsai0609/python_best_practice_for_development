"""
https://zhuanlan.zhihu.com/p/66267212
"""
import attr


# 自動處理所有魔術方法
@attr.s
class GreaterColor(object):
    r = attr.ib(default=255, type=int)
    g = attr.ib(default=255, type=int)
    b = attr.ib(default=255, type=int)


# 還要寫 attr.ib 很麻煩


@attr.s(auto_attribs=True)
class EvenGreaterColor:
    r: int = 255
    g: int = 255
    b: int = 255


c2 = GreaterColor()
c3 = EvenGreaterColor()

for c in [c2, c3]:
    print()
    print(c)
    print()
    print(dir(c))
