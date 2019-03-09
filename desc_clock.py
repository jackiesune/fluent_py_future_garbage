#desc_clock.py

import time

def clock(func):
    """装饰器函数"""
    def inner(*args):
        t0=time.perf_counter()
        result=func(*args)
        t0=time.perf_counter()-t0
        print("the result:{} used time {}".format(result,t0))
        return result
    return inner


@clock
def funced(strs):
    print(strs)
    time.sleep(.123)
    return 43


#if __name__=="__main__":
#    funced("I'm thinking")



@clock
def fy(n):
    if n<2:
        return n
    else:
        return fy(n-2) + fy(n-1)

if __name__=="__main__":
   fy(7)

