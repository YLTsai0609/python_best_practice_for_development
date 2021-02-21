# example, divide function
from typing import Union, Tuple
from numbers import Number
# Number is the same as Union[int, float, complex]


def divide(a: Number, b: Number) -> Union[Number, None]:
    try:
        return a / b
    except ZeroDivisionError:
        return None


x, y = 1, 2
# Result is not None
# x, y = 1, 0
# Invalid inputs
result = divide(x, y)
if result is None:
    print('Invalid inputs')
else:
    print('Result is not None')

# What will happened x = 0, y = 5?
x, y = 0, 5
result = divide(x, y)
if not result:
    print('Invalid inputs')

# It's will be hard to detect what error is happening!

# A better way


def divide(a: Number, b: Number) -> Tuple[bool, Union[Number, None]]:
    """
    devide two number

    Args:
        a (Number): 
        b (Number): 

    Returns:
        Tuple[bool, Union[Number, None]]: succeed of not, return value
    """
    try:
        return True, a / b
    except ZeroDivisionError:
        return False, None


success, result = divide(x, y)
if not success:
    print('Invalid inputs')
else:
    print('Success')
# Success

# if you don't care about the success_flag or not

_, result = divide(x, y)
if not success:
    print('Invalid inputs')
else:
    print('Success')

# actually, raise error is a clear eay to split the type of error


def divide(a: Number, b: Number) -> Number:
    """divide two number

    Args:
        a (Number): 
        b (Number): 

    Raises:
        ValueError: when b goes to zero
        If you wanna catach the error, 

    Returns:
        Number: divided result
    """
    try:
        return a / b
    except ZeroDivisionError as e:
        raise ValueError('Invalid inputs') from e


x, y = 5, 2
try:
    result = divide(x, y)
except ValueError:
    print('Invalid inputs')
else:
    print('Result is %.2f' % result)

# Things to remember

# 1. Functions that return None to indicate special meaning are error prone
#     because None and other values (e.g., zero, the empty string) all
#     evaluate to False in conditional expressions.
# 2. Raise exceptions to indicate special situations instead of returning
#     None. Expect the calling code to handle exceptions properly when they
#     are documented.
