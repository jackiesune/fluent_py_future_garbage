#abclass_test.py



#Every concrete subclass should pass the following test.


creat concrete subclass ,test load from iterator::


    >>> balls=[3,4,5,6]
    >>> con=ConcreteB(balls)
    >>> con.canpick()
    True
    >>> con.inspect()
    (3,4,5,6)

concrete subclass of pick::
    >>> picks=[]
    >>> picks.append(con.pick())
    >>> picks.append(con.pick())
    >>> picks.append(con.pick())
    >>> picks.append(con.pick())
    >>> con.canpick()
    False
    >>> len(picks)===len(balls)
    >>> sorted(picks)==sorted(balls)

test loaded from iterabtor::
    >>> con.load(balls)
    >>> con.canpick()
    >>> con.inspect()
    (3,4,5,6)

check Exception LookupError::
    >>> con2=ConcreteB([])
    >>> try:
    ...     con2.pick()
    ... except LookupError:
    ...     print('ok')
    ...
    ok




    




