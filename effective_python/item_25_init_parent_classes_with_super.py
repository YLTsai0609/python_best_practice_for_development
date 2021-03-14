'''
Initialize parent classes with super
'''

from pprint import pprint

# The old way to initialize a parent class from a child class is to
# directly call the parent class's __init__ method with the child instance.


class MyBaseClass(object):
    def __init__(self, value):
        self.value = value


class MyChildClass(MyBaseClass):
    def __init__(self):
        MyBaseClass.__init__(self, 5)

# This appriach works fine for simple hierarchies but breaks down
# in many cases

# If your class is affected by multiple ingeritance(something to avoid in general, check item26)
# calling the "superclass" __init__ method directly can lead to unpredictable behavior
# One problem is that the __init__ call order isn't specified across all subclass

# For example, here I define two parent classes that operate on the instance's value field:


class TimesTwo(object):
    def __init__(self):
        self.value *= 2


class PlusFive(object):
    def __init__(self):
        self.value += 5

# This class defines its parent classes in one ordering


class OneWay(MyBaseClass, TimesTwo, PlusFive):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        TimesTwo.__init__(self)
        PlusFive.__init__(self)


foo = OneWay(7)
print("First ordering is (7*2)+5 = ", foo.value)

# Here's another class that defines the same parent class but
# in a different ordering


class AnotherWay(MyBaseClass, PlusFive, TimesTwo):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        TimesTwo.__init__(self)
        PlusFive.__init__(self)

# The initialize order is different between the inherent order
# But it still work(which is weired)
# Times first or plus first(?)


bar = AnotherWay(7)

print("Second ordering still is ", bar.value)

# Diamond inheritance
# Diamond inheritance happens when a subclass ingert from two
# separate classes that have the same superclass somewhere hierarchy


class TimesFive(MyBaseClass):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        self.value *= 5


class PlusTwo(MyBaseClass):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        self.value += 2

# Then I define a child class that inhert it from both these classes


class ThisWay(TimesFive, PlusTwo):
    def __init__(self, value):
        TimesFive.__init__(self, value)
        PlusTwo.__init__(self, value)


foo = ThisWay(5)

print("Should be (5*5)+2 = 27, but we got : ", foo.value)

# Why we get 7 instead of 27?
# Because the call to the second parent class's constructor, PlusTwo.__init__,
# cause self.value to be reset back to 5 when MyBaseClass.IIint__ get a second time

# Python 2.2 add the super built-in function and defined the
# method resolution order(MRO)
# MRO standardize which superclasses are initialized before others
# (e.g. depth-first, left-to-right)
# It's also ensure that common superclass in diamond hierarchies are only run onces.

# Now, let's try it again but we use super


class TimesFiveCorrect(MyBaseClass):
    def __init__(self, value):
        super(TimesFiveCorrect, self).__init__(value)
        self.value *= 5


class PlusTwoCorrect(MyBaseClass):
    def __init__(self, value):
        super(PlusTwoCorrect, self).__init__(value)
        self.value += 2


class GoodWay(TimesFiveCorrect, PlusTwoCorrect):
    def __init__(self, value):
        super(GoodWay, self).__init__(value)


foo = GoodWay(5)
print("Should be 5*(5+2) = 35, and the value is ", foo.value)

# why the answer is not (5*5)+2 = 27?
# The ordering matches what the MRO defines for this class
# The MRO ordering available on a class method called mro

pprint(GoodWay.mro())
# [<class '__main__.GoodWay'>,
#  <class '__main__.TimesFiveCorrect'>, 7*5 = 35
#  <class '__main__.PlusTwoCorrect'>, 5+2 = 7
#  <class '__main__.MyBaseClass'>, - the top of diamond (5)
#  <class 'object'>]

# So if we change the ordering, we might get 27 like:


class AnotherGoodWay(PlusTwoCorrect, TimesFiveCorrect):
    def __init__(self, value):
        super(AnotherGoodWay, self).__init__(value)


bar = AnotherGoodWay(5)
print(bar.value)
pprint(AnotherGoodWay.mro())

# [<class '__main__.AnotherGoodWay'>,
#  <class '__main__.PlusTwoCorrect'>, 25+2 = 27
#  <class '__main__.TimesFiveCorrect'>, 5x5 = 25
#  <class '__main__.MyBaseClass'>, 5
#  <class 'object'>]

# However, the sytax is too verbose
# So Python 3 simplify the syntax


class Explicit(MyBaseClass):
    def __init__(self, value):
        super(__class__, self).__init__(value * 2)


class Implicit(MyBaseClass):
    def __init__(self, value):
        super().__init__(value * 2)


assert Explicit(10).value == Implicit(10).value

# Things to remember

# 1. Python standard method resolution order (MRO) solves the problem to
# super class initilization order and diamond inheritance
# 2. Always use super bulit-in function to initialize parent classes
