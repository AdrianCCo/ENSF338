import timeit

def for_pow2(n):
    num = 1
    for i in range(n):
        num *= 2 
    return num

def listComp_pow2(n):
    power = [1] * (n + 1)
    result = [2**num for num in range(n + 1)]
    return result[n]

print("For Loop Time Taken:", timeit.timeit(stmt = "for_pow2(1000)", setup = "from __main__ import for_pow2"), "seconds")

print("List Comprehension Time Taken:", timeit.timeit(stmt = "listComp_pow2(1000)", setup = "from __main__ import listComp_pow2"), "seconds")




