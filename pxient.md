# Learned in pixnet

## item 1 use attrs for your python OOP development

1. 如果需要寫到大量的OOP，使用attrs可以節省非常多開發時間，且增加可讀性
2. attrs透過一個裝飾器來自動地幫撰寫的class新增各種功能，例如`__init__`, `__repr__`, `__hash__`, `__eq__`, `__gt__`, `__ge__`,`__lt__`, `__le__`，並且是使用`functools.wrap`，並沒有修改到class原本的名稱
3. 使用`attr.asdict`, `attr.filed`可以查看目前class以及屬性的相關狀況
4. `@attr.s(auto_attribs=True)`可以讓你撰寫更簡潔的class，僅需宣告屬性名稱以及型態即可
5. `forzen=True` --> immutable instance
6. `kw_only` --> accept keyword argument only
7. `slots` --> use slots in stead of `__dict__`

### Additional discussion

1. `attrs`, `dataclass` - 都是為了讓開發者可以用更少的程式碼、達成更好的可讀性及維護性的工具
2. `dataclass` 在 python 3.7 被納入官方套件中，PEP 557 中，對於 `dataclass` 的使用方式有非常詳細的解說，但兩派都有擁護者
3. 相關討論 
   1. [attrs 和 Python3.7 的 dataclasses](https://zhuanlan.zhihu.com/p/34963159)
   2. [Python3.7 特色(1)-dataclasses](https://www.smalldragon.tw/python37-1-dataclasses/)
   3. [Python 工匠：做一个精通规则的玩家](https://github.com/YLTsai0609/one-python-craftsman/blob/master/zh_CN/10-a-good-player-know-the-rules.md)