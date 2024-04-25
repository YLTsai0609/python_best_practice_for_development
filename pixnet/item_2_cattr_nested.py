import attr

@attr.s(frozen=True, auto_attribs=True)
class LifeCycle:
    hot2warm : int
    warm2cold : int

@attr.s(frozen=True, auto_attribs=True)
class Service:
    name:str

    