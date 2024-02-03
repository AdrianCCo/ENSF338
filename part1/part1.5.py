import timeit

memory = dict()

def funci(n, my_dict = dict()):

    if n in my_dict:
        return my_dict.get(n)
    
    if n == 0 or n == 1:
        my_dict[n] = n
        return n

    else:
        result = funci(n - 1, my_dict) + funci(n - 2, my_dict)
    
    my_dict[n] = result

    return result

def func(n):

    if n == 0 or n == 1:
        return n
    
    else:
        return func(n-1) + func(n-2)
    
def execute_funci():
    for i in range(36):
        funci(i, memory)

def execute_func():
    for i in range(36):
        func(i) 

elapsed_time = timeit.timeit(stmt = "execute_funci()", setup = "from __main__ import execute_funci", number = 1)

print("Execution Time for funci(): ", elapsed_time)    

elapsed_time = timeit.timeit(stmt = "execute_func()", setup = "from __main__ import execute_func", number = 1)

print("Execution Time for func(): ", elapsed_time) 