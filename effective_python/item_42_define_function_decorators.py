'''
Item 42 : Define function decorators with functools.wraps
'''

from functools import wraps

# Python has special syntax for decorators that can be applied to functions.
# Decorators have the ability to run additional code before and after any calls
# to the functions they wrap.
# This allows them to access and modify input arguments and return values.
# This functionality can be useful for
# enforcing semantics, debugging, registering functions, and more.


# For example
# You want to print the arguments and return value of a function call
# This is especially helpful when debugging s stack of function calls from a recursive function

def trace(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(
            '%s(%r, %r -> %r' % (func.__name__, args, kwargs, result)
        )
        return result
    return wrapper

# then I can apply this to a function using @ symbol


@trace
def fibonacci(n):
    """
    Return the n-th Fibonacci number
    """
    if n in (0, 1):
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)

# The @ symbol is equivalent to calling the decoratro on  the function it wraps
# and assigning the return value to the original name in the same scope
# just like

# fibonacci = trace(fibonacci)


fibonacci(3)

# fibonacci((1,), {}) -> 1
# fibonacci((0,), {}) -> 0
# fibonacci((1,), {}) -> 1
# fibonacci((2,), {}) -> 1
# fibonacci((3,), {}) -> 2

# This works well, but it has an unintended(意外的) side effect.
# The value retuened by the decorator-- the function that called above--doesn't thikn it's named
# fibonacci

print(fibonacci)

# <function trace.<locals>.wrapper at 0x7fac26042a60>

# This cause of this isn't hard to see.
# The trace function returns the wrapper it defines
# The wrapper function is what's assigned to the fibonacci name in
# the containing module because it undermines tools that do introspection


def raw_fibonacci(n):
    """
    Return the n-th FIbonacci number
    """
    if n in (0, 1):
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)

# for example, help() on the fibonacci doesn't work at all


# help(raw_fibonacci)
# help(fibonacci)

# The solution is to use the wraps helper function from the functools built-in module
# This is a decorator that helps you write decorator.
# Applying it to the wrapper function will copy all of the important-meta-data about the innfer function
# to the outer function

def trace(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(
            '%s(%r, %r) -> %r',
            (func.__name__, args, kwargs, result)
        )
        return result
    return wrapper


@trace
def fibonacci(n):
    """
    Return the n-th Fibonacci number
    """
    if n in (0, 1):
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)


help(fibonacci)
# Now the "help" is working

# Calling help is just one example of how decoratros can subtly cause problems!
# python functions have many other standard attributes
# e.g. __name__, __module__, that must be preserved to maintian the interface of functions
# in the language
# Using wraps ensures that you'll always get the correct behavior

# Things to remember
# 1. Decorators are Python syntax for allowing one function to modify another function st runtime
# 2. Using decorators can cause strange behavior in tools that do introspection, such as debuggers
# 3. Use the wraps decorator from the functools built-in module
# when you define your own decorators to avoid any issues.
