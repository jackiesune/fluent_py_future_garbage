
from collections import namedtuple


Card=namedtuple("Card","point color")


#poins=list(range(2,11))+list('JQKA')
#cols=["clubs","diamonds","hearts","spades"]

class dect:


    poins=list(range(2,11))+list('JQKA')
    cols=["clubs","diamonds","hearts","spades"]

    def __init__(self):
        self._cards=[Card(p,c) for p in self.poins for c in self.cols]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self,index):
        return self._cards[index]

    
