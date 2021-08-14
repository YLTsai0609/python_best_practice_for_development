# Learned in pixnet

## item 1 use attrs for your python OOP development

1. 如果需要寫到大量的OOP，使用attrs可以節省非常多開發時間，且增加可讀性
2. attrs透過一個裝飾器來自動地幫撰寫的class新增各種功能，例如`__init__`, `__repr__`, `__hash__`, `__eq__`, `__gt__`, `__ge__`,`__lt__`, `__le__`，並且是使用`functools.wrap`，並沒有修改到class原本的名稱
3. 使用`attr.asdict`, `attr.filed`可以查看目前class以及屬性的相關狀況
4. `@attr.s(auto_attribs=True)`可以讓你撰寫更簡潔的class，僅需宣告屬性名稱以及型態即可
5. `forzen=True` --> immutable instance
6. `kw_only` --> accept keyword argument only
7. `slots` --> use slots in stead of `__dict__`