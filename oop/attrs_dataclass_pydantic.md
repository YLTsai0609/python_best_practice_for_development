
# item 1 use attrs for your python OOP development

1. 如果需要寫到大量的OOP，使用attrs可以節省非常多開發時間，且增加可讀性
2. attrs透過一個裝飾器來自動地幫撰寫的class新增各種功能，例如`__init__`, `__repr__`, `__hash__`, `__eq__`, `__gt__`, `__ge__`,`__lt__`, `__le__`，並且是使用`functools.wrap`，並沒有修改到class原本的名稱
3. 使用`attr.asdict`, `attr.filed`可以查看目前class以及屬性的相關狀況
4. `@attr.s(auto_attribs=True)`可以讓你撰寫更簡潔的class，僅需宣告屬性名稱以及型態即可
5. `forzen=True` --> immutable instance
6. `kw_only` --> accept keyword argument only
7. `slots` --> use slots in stead of `__dict__`

* attrs 也支援其他常用功能 - 屬性驗證(pydantic)、屬性資料型態轉換(pydantic)、屬性值不可變(dataclass need python 3.10+)

## Additional discussion

1. `attrs`, `dataclass` - 都是為了讓開發者可以用更少的程式碼、達成更好的可讀性及維護性的工具
2. `dataclass` 在 python 3.7 被納入官方套件中，PEP 557 中，對於 `dataclass` 的使用方式有非常詳細的解說，但兩派都有擁護者
3. 相關討論 
   1. [attrs 和 Python3.7 的 dataclasses](https://zhuanlan.zhihu.com/p/34963159)
   2. [Python 工匠：做一个精通规则的玩家](https://github.com/YLTsai0609/one-python-craftsman/blob/master/zh_CN/10-a-good-player-know-the-rules.md)
   3. [Why I use attrs instead of pydantic (attrs, cattrs, python, pydantic)](https://threeofwands.com/why-i-use-attrs-instead-of-pydantic/#:~:text=attrs%20is%20a%20library%20for,somewhere%2C%20or%20send%20it%20somewhere.)

   
### Why I use attrs instread of pydantic

1. dataclass is a subset of attrs, only python 3.7+, attr support 2.7 ~ 3.x
2. attrs is a library for generating the boring parts of writing classes; Pydantic is that but also a complex validation library.
3. Validation
    * attrs - opt-in - you define your validators - componeet-based, you could also install `attr.validators`
    * pydantic - opt-out - validation happends in backend, you need to turn it off. - `BaseModel.construct()`
    * what if we face a list with 1k+ string?
4. Convertion
    * attrs - opt-in, you define your converters - component-based, you could also install `attr.converters`, or write yourself
    * pydantic - opt-out, automantically convert datetime to int or float

attrs - you define the convert yourself, or it doesn't exist, If you define it, you choose how it works exactly.
pydantic - rules defined inside pydantic, you get convenience, and if you wanna do something customize, it will be harder 

5. performance in construction and deconstruction
    * attrs don't construct by default, use cattrs - it's more flexible such as pendulum datetime, msgpack, ujson, ...

short answer - if we need to use 1 package and getting start fast, use pydantic. if we need to make our code-base long term maintained, use attrs and cattrs
