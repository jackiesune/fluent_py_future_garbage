#desc_clock.py

import time
import functools
def clock(func):
    """装饰器函数"""
    def inner(*args):
        t0=time.perf_counter()
        result=func(*args)
        t0=time.perf_counter()-t0
        print("the result:{} used time {}".format(result,t0))
        return result
    return inner

DEFAULT_FORMAT="the results:{} used time {}"

def des_fac(fmt=DEFAULT_FORMAT):
    """装饰器工厂函数"""
    def des(func):
        '''装饰器函数'''
        def inner(*args):
            t0=time.perf_counter()
            result=func(*args)
            t0=time.perf_counter()-t0
            print(fmt.format(result,t0))
            return result
        return inner
    return des

@des_fac()
def funced2(strs):
    print(strs)
    time.sleep(.124)
    return 42



@clock
def funced(strs):
    print(strs)
    time.sleep(.123)
    return 43


#if __name__=="__main__":
#    funced("I'm thinking")

#记录相同参数的结果,避免重复运算
@functools.lru_cache()
@clock
def fy(n):
    if n<2:
        return n
    else:
        return fy(n-2) + fy(n-1)

if __name__=="__main__":
   funced2("now Thinking adout it")


