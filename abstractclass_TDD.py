import abc

class Baseab(abc.ABC):

    @abc.abstractmethod
    def load(self,iterable):
        '''子类必实现的:从可迭代对象添加元素'''

    @abc.abstractmethod
    def pick(self):
        '''随机删除元素,并返回,如果无元素则抛出LookupError'''


    def canpick(self):
        """有元素则返回True"""
        return bool(self.inspect)

    def inspect(self):
        '''返回由当前元素构成的元组'''
        items=[]
        while True:
            try:
                items.append(self.pick)
            except LookupError:
                break
        self.load(items)
        return tuple(items)
        

import random

class Obaseab(Baseab):
    
    def __init__(self,item):
        self._random=random.SystemRandom()
        self._items=[]
        self.load(item)

    def load(self,item):
        self._items.extend(item)
        self._random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('Can not pick from Empty Obaseab')

    def __call__(self):
        self.pick()

