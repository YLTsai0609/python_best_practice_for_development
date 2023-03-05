import os

import attr


@attr.s(frozen=True)
class DataUri:
    basename: str = attr.ib(converter=str) # 將輸入轉換成 string
    prefix: str = attr.ib(converter=str) # 並且是不可變的
    dummy = 1

    @property
    def fullpath(self):
        return os.path.join(self.prefix, self.basename)

d1 = DataUri(basename="abc.py", prefix=1)
print(d1, d1.fullpath)


# d1.basename = 4  # raise frozen error