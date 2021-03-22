'''
Use @classmethod polomorphism to construct object generically

@classmethod provide another way to call the method without construct your instance!
Also , yuo can check here to konw the @classmethod and @staticmethod
https://zhuanlan.zhihu.com/p/28010894
'''

# Consider that you're implementing a Map-Reduce algorithm

import os
import threading
import random


# the base input data
class InputData(object):
    def read(self):
        raise NotImplementedError


class PathInputData(InputData):
    def __init__(self, path):
        super().__init__()
        self.path = path

    def read(self):
        return open(self.path).read()

# you can construct the other child class to support reading data like
# network, decompress data transparently


# the base worker
class Worker(object):
    def __init__(self, input_data):
        self.input_data = input_data
        self.result = None

    def map(self):
        raise NotImplementedError

    def reduce(self):
        raise NotImplementedError

# a specific work called LineCountWorker


class LineCountWorker(Worker):
    def map(self):
        data = self.input_data.read()
        self.result = data.count('\n')

    def reduce(self, other):
        self.result += other.result

# Now we need to write the Map-Reduce algorithm to operate files by using worker and path input data


def generate_inputs(data_dir):
    for name in os.listdir(data_dir):
        yield PathInputData(os.path.join(data_dir, name))


def create_workers(inputs_list):
    workers = []
    for input_data in inputs_list:
        workers.append(LineCountWorker(input_data))
    return workers


def execute(workers):
    threads = [threading.Thread(target=w.map) for w in workers]
    print('There are n workers : ', len(threads))
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    first, rest = workers[0], workers[1:]
    for worker in rest:
        first.reduce(worker)
    return first.result


def mapreduce(data_dir):
    inputs = generate_inputs(data_dir)
    workers = create_workers(inputs)
    return execute(workers)


def write_test_files(tmpdir):
    for idx in range(10):
        rdn_f_name = os.path.join(tmpdir, f'{idx}.txt')
        print(rdn_f_name)
        temp_f = open(rdn_f_name, 'w')
        for _ in range(random.randint(1, 20)):
            temp_f.write('random lines\n')
    print(os.listdir(tmpdir))


write_test_files('tmp')
result = mapreduce('tmp')

print('There are', result, 'lines')

#################### So what's the problem now? #######################

# if wanna write another Input data or Worker subclass, you would
# also have to rewrite the generate_inputs, create_workers, and mapreduce
# functions to match

# If there a way to construct a generic constrcuct object?
# In other language, you'd solve this problem with constrctor polymorphism
# requiring that each InputData subclass provides a special constrctor
# that can be used generacially by helper methods that orchestrate the Mapreduce


# use generates_input take a dictionary with a set of configuration

class GenericInputData(object):
    def read(self):
        raise NotImplementedError

    @classmethod
    def generate_inputs(cls, config):
        raise NotImplementedError

# combine the generate_inputs into PathInputData


class PathInputData(GenericInputData):
    def __init__(self, path):
        super().__init__()
        self.path = path

    def read(self):
        return open(self.path).read()

    @classmethod
    def generate_inputs(cls, config):
        data_dir = config['data_dir']
        for name in os.listdir(data_dir):
            yield cls(os.path.join(data_dir, name))

# similarly, make create_workers help par of the GenericWorker class


class GenericWorker(object):
    def __init__(self, input_data):
        self.input_data = input_data
        self.result = None

    def map(self):
        raise NotImplementedError

    def reduce(self):
        raise NotImplementedError

    @classmethod
    def create_worker(cls, input_class, config):
        workers = []
        for input_data in input_class.generate_inputs(config):
            workers.append(cls(input_data))
        return workers

# Note that the call to input_class.generate_inputs above is the class
# polymorphism.
# you can also see how create_workers calling cls provide an alternative way
# to constrcut GenericWorker objects besides
# using the __init__ method directly

# the effect on my concrete GenericWorker subclass is nothing more than
# change its parent class


class LineCountWorker(GenericWorker):
    def map(self):
        data = self.input_data.read()
        self.result = data.count('\n')

    def reduce(self, other):
        self.result += other.result

# I can rewrite the mapreduce function to be completely generic


def mapreduce(worker_calss, input_class, config):
    workers = worker_calss.create_worker(input_class, config)
    return execute(workers)


write_test_files('tmp')
config = {'data_dir': 'tmp'}
result = mapreduce(LineCountWorker, PathInputData, config)

print('There are', result, 'lines')

# Now you can write other GenericInputData and GenericWorker classes as you
# wish and not have to rewrite any of the glue code

# 1. Python only supports a single constructor per class, the __init__ method
# 2. Use @classmethod to define alternatvie constrcutors for your classes
# 3. Use class method polymorphism to provide generic ways to build and connect
# concrete subclasses
