import attr

@attr.s
class C(object):
    x = attr.ib()
    @x.validator
    def check(self, attribute, value):
        if value > 42:
            raise ValueError("x must be smaller or equal to 42")
print(C(42))

try:
    print(C(43))
except Exception as e:
    print(e)


def x_smaller_than_y(instance, attribute, value):
    if value >= instance.y:
        raise ValueError("'x' has to be smaller than 'y'!")

@attr.s
class C(object):
    x = attr.ib(validator=[attr.validators.instance_of(int),
                           x_smaller_than_y])
    y = attr.ib()

print(C(x=3, y=4))
try:
    print(C(x=4,y=3))
except Exception as e:
    print(e)

