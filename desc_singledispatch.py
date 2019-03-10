import functools
import numbers
from collections import abc
import time



@functools.singledispatch
def normalize(obj):
    print("original")

@normalize.register(str)
def _text(obj):
    print("str")

@normalize.register(numbers.Integral)
def _number(obj):
    print("int")

@normalize.register(tuple)
@normalize.register(abc.MutableSequence)
def _mut(obj):
    print(" tuple Sequence")



