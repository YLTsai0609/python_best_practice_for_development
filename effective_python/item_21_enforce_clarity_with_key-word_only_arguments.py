# Item 21: Enforce clarity with key-word only arguments

def safe_division(number, divisor, ignore_overflow, ignore_zero_division):
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise


result = safe_division(1, 100**500, True, False)
print(result)
# 0.0

# This call will ignore the error from dividing by zero and will return
# infinity.
result = safe_division(1, 0, False, True)
print(result)
# inf

# The problem is that it's east to confuse the position of the two Boolean arguments
# that control the exception-ignoring behavior

# * means the end of positional argument
# the followling arguments should all be keyword-only!


def safe_division_c(number, divisor, *,
                    ignore_overflow=False,
                    ignore_zero_division=False):
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise


result = safe_division_c(1, 0, ignore_zero_division=True)  # OK
print(result)
# inf
# result = safe_division_c(1, 0, True)
# Will Failed
# TypeError: safe_division_c() takes 2 positional arguments but 3 were given


# Things to remember
# 1. Keyword arguments make the intention of a function call more clear.
# 2. Use keyword-only arguments to force callers to supply keyword arguments
#    for potentially confusing functions, especially those that accept
#    multiple Boolean flags.
# 3. Python 3 supports explicit syntax for keyword-only arguments in
#    functions.
# 4. Python 2 can emulate keyword-only arguments for functions by using
#    **kwargs and manually raising TypeError exceptions.
