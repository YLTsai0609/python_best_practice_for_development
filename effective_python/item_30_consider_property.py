# Item 30 : Consider @property instead of refactoring attributes


# @property decorator make it east for simple accesses of an instance's attribute to act smarter
# one common use of @property is transitioning what was once a simple numerical attribute into an
# on-the-fly calculations
# This is helpful because it lets you migrate any of the call sites
# It also provides an important stopgap for improving your interfaces over time

from datetime import timedelta
import datetime

# Consider a leaky bucket quota here
# The Bucket class represnts how much quota remains and the duration for which the quota will be available


class Bucket(object):
    def __init__(self, peroid):
        self.period_delta = timedelta(seconds=peroid)
        self.reset_time = datetime.datetime.now()
        self.quota = 0

    def __repr__(self):
        return 'Bucket(quota=%d)' % self.quota

# The leaky bucket algorithm works bt ensuring that, whenever the bucket is filled
# the amount of quota does not carry over from one peroid to the next.


def fill(bucket, amout):
    now = datetime.datetime.now()
    if now - bucket.reset_time > bucket.period_delta:
        bucket.quota = 0
        bucket.reset_time = now
    bucket.quota += amout


def deduct(bucket, amount):
    now = datetime.datetime.now()
    if now - bucket.reset_time > bucket.period_delta:
        return False
    if bucket.quota - amount < 0:
        return False
    bucket.quota -= amount
    return True

# To use this class, first I fill the bucket.


bucket = Bucket(60)
fill(bucket, 100)
print(bucket)  # Bucket(quota=100)

# Then, I deduct the quota that I need.

if deduct(bucket, 99):
    print('Had 99 quota')
else:
    print('Not enough for 99 quota')
print(bucket)

if deduct(bucket, 3):
    print('Had 3 quota')
else:
    print('Not enough for 3 quota')
print(bucket)

# Not enough for 3 quota
# Bucket(quota=1)

# The problem with this implementation is that I never know
# that quota level the buck started with
# It would be useful to know whether callers to deduct are being blocked


class Bucket(object):
    def __init__(self, period):
        self.period_delta = timedelta(seconds=period)
        self.reset_time = datetime.datetime.now()
        self.max_quota = 0
        self.quota_consumed = 0

    def __repr__(self):
        return ('Bucket(max_quota=%d, quota_consumed=%d)' %
                (self.max_quota, self.quota_consumed))

# I use a @property method to compute the current level of quota on-the-fly
# using these new attributes.
    @property
    def quota(self):
        return self.max_quota - self.quota_consumed

# When the quota attribute is assigned, I take special action matching the
# current interface of the class used by fill and decuct.
    @quota.setter
    def quota(self, amount):
        delta = self.max_quota - amount
        if amount == 0:
            '''quota being reset for a new period'''
            self.quota_consumed = 0
            self.max_quota = 0
        elif delta < 0:
            '''quota being filled for the new period'''
            assert self.quota_consumed == 0
            self.max_quota = amount
        else:
            '''quota being consumed during the period'''
            assert self.max_quota >= self.quota_consumed
            self.quota_consumed += delta


bucket = Bucket(60)
print('Initial', bucket)
fill(bucket, 100)
print('Filled', bucket)

if deduct(bucket, 99):
    print('Had 99 quota')
else:
    print('Not enough for 99 quota')
print('Now', bucket)

if deduct(bucket, 3):
    print('Had 3 quota')
else:
    print('Not enough for 3 quota')
print('Still', bucket)

# The best part is that the code using BUcket.quota doesn't have
# to change or know the the class has changed.
# New usage can do the right thing and accee max_quota and quota_consumed directly

# @property because it lets you make incremental progress
# toward a better data model over time. Reading the Bucket example above

# @property is a tool to help you address problems you'll come across in real-world code
# Don't overuse it. When you find yourself repeatedly extending @property methods.
# it's probably time to refacetor your class instrad of futher paving over your code's poor design


# Thnigs to remember

# 1. Use @peoperty to give existing instance attributes new functionality
# 2. Make incremental progess toward better data models by using @peoperty
# 3. Consider refactoring a class and all calls sites when you find yourself using @property too heavily.
