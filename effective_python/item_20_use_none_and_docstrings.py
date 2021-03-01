# Item 20: Use None and Docstrings to specify dynamic default arguments
import datetime
import time
import json

# Case 1


def log(message, when=datetime.datetime.now()):
    print('%s: %s' % (when, message))


log('Hi there!')
time.sleep(0.1)
log('Hi again!')
# 2017-02-23 18:27:27.045710: Hi there!
# 2017-02-23 18:27:27.045710: Hi again!
# The timestamps are the same because datatime.now is only excuted a single time
# when the function is defined
# Default argument values are evaluated once per module load!

# So here is the solution for this hard-found bug


def log(message, when=None):
    """Log a message with a timestamp.
    Args:
        message: Message to print.
        when: datetime of when the message occurred. Defaults to the present
        time.
    """
    when = datetime.datetime.now() if when is None else when
    print('%s: %s' % (when, message))


log('Hi there!')
time.sleep(0.1)
log('Hi again!')
# 2017-02-23 18:38:27.510581: Hi there!
# 2017-02-23 18:38:27.610755: Hi again!


# Case 2
# If the argument is metuable, using None is more important
# below is the case, if decode faild, return empty dict
def decode(data, default={}):
    try:
        return json.loads(data)
    except ValueError:
        return default


foo = decode('bad data')
foo['stuff'] = 5
bar = decode('also bad')
bar['meep'] = 1
print('Foo:', foo)
print('Bar:', bar)

# Foo: {'stuff': 5, 'meep': 1}
# Bar: {'stuff': 5, 'meep': 1}

# The defualt {} is shared cross different function calls,
# Once again, the argument is initialized when the module was called.
# is state will compare the id of two objects
print('Is foo is bar?', foo is bar, 'foo id : ', id(foo), 'bar id : ', id(bar))

# Solution


def decode(data, default=None):
    """Load JSON data from a string.
    Args:
        data: JSON data to decode.
        default: Value to return if decoding fails. Defaults to an empty
        dictionary.
    """
    if default is None:
        default = {}
    try:
        return json.loads(data)
    except ValueError:
        return default


foo = decode('bad data')
foo['stuff'] = 5
bar = decode('also bad')
bar['meep'] = 1
print('Foo:', foo)
print('Bar:', bar)

# Foo: {'stuff': 5}
# Bar: {'meep': 1}
