#fromabsclass.py

from abstractclass_TDD import Baseab
import random

class Tbaseab(Baseab):

    def __init__(self,iterator):
        self._balls=list(iterator)

    def load(self,item):
        self._balls.extend(item)

    def pick(self):
        try:
            position=random.randrange(len(self._balls))
        except ValueError:
            raise LookupError('Cannot pick from empth Tbaseab')
        return self._balls.pop(position)

    def canpick(self):
        bool(self._balls)

    def inspect(self):
        return tuple(sorted(self._balls))


@Baseab.register
class Fbaseab(list):

    def pick(self):
        if self:
            position=random.randrange(len(self))
            self.pop(position)
        else:
            raise LookupError("Pop from empty register baseab")

    load=list.extend
    
    def canpick(self):
        return bool(self)

    def inspect(self):
        return tuple(self)
        

