from collections import namedtuple


Customer=namedtuple("Customer","name score")
promos=[globals()[name] for name in globals() if name.endswith('_promo')]

class Lineitem:

    def __init__(self,name,price,num):
        self.name=name
        self.price=price
        self.num=num

    def Ltotal(self):
        self.total=self.price * self.num
        return self.total


class Order:

    def __init__(self,cust,cards):
        self.cust=cust
        self.cards=cards
        self.best_dues=globals()['promos']
        
    def Ctotal(self):
        if not hasattr(self,'_total'):
            self._total=sum(litme.total for litme in self.cards)
        return self._total

    def Ototal(self):
        self.total=self._total-self.due()
        return self.total

    def due(self):
       return max(choice(self) for choice in self.best_dues)

    def best_due(self):
        if self.cust.score<1000:
            self.best_dues.remove('score_promo')
        itemnames=set()
        for item in self.cards:
            itemnames.add(item.name)
            if item.num<20:
                self.best_dues.remove('num_promo')
            if  len(itemnames)<10:
                self.best_dues.remove('qua_promo')
        return self.best_dues

def score_promo(order):
    return order._total*0.05

def num_promo(order):
    return order._total*0.1

def qua_promo(order):
    return order._total*0.07


