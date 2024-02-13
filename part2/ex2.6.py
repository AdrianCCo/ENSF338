import timeit
import sys

sys.setrecursionlimit(10500)

def for_pow2(n):
    num = 1
    for i in range(n):
        num *= 2 
    return num

def listComp_pow2(n):
    power = [1] * (n + 1)
    result = [2**num for num in range(n + 1)]
    return result[n]

def pow2(n):
    if(n == 0):
        return 1
    return 2 * pow2(n - 1)


print("pow2(10000) Function Time Taken to execute 10000 times:", timeit.timeit(stmt = "for_pow2(10000)", setup = "from __main__ import for_pow2", number = 10000), "seconds")

print("for_pow2(1000) Function Time Taken to execute 1000 times:", timeit.timeit(stmt = "for_pow2(1000)", setup = "from __main__ import for_pow2", number = 1000), "seconds")

print("listComp_pow2(1000) Function Time Taken to execute 1000 times:", timeit.timeit(stmt = "listComp_pow2(1000)", setup = "from __main__ import listComp_pow2", number = 1000), "seconds")




