#1. Checks if the if input is 1 or 0, if so then it will return the value of n
#   If the value is neither of the above, it will call the function twice recursively where the input is n - 1 
#   and n - 2 where they are added together and returned. Once n reaches 1, the function will return a value until
#   it reaches the initial caller of the function.

#2. No, this is not a divide and conquer algorithm 

#3. The big O notation for the recursive fibonacci function is O(2^n). This is because for each input of n, the 
#   function will call the function recursively twice more until the input reaches 0 or 1

#5. The big O notation for the fibonacci function using memorization is O(n). 


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

#5. The big O notation of the improved fibonacci function is O(n). 


import timeit
import matplotlib.pyplot as plt
import numpy as np

memory = dict()
time_dict_funci = {}
time_dict_func = {}


def func(n):
    
    if n == 0 or n == 1:
        return n
    else:
        return func(n-1) + func(n-2)


for i in range(36):
    elapsed_time = timeit.timeit(stmt = f"funci({i}, {memory})", setup = "from __main__ import funci", number = 1)
    time_dict_funci[i] = elapsed_time  

for i in range(36):
    elapsed_time = timeit.timeit(stmt = f"func({i})", setup = "from __main__ import func", number = 1)
    time_dict_func[i] = elapsed_time  

plt.style.use("fivethirtyeight")

plt.style.use
y_vals2 = time_dict_funci.values()
x_vals2 = time_dict_funci.keys()
plt.title("Data Set for funci()")
plt.xlabel("Value of n")
plt.ylabel("Execution Time")
plt.plot(x_vals2, y_vals2)
plt.savefig("ex1.6.2.jpg")
plt.show()

y_vals1 = time_dict_func.values()
x_vals1 = time_dict_func.keys()
plt.title("Data Set for func()")
plt.xlabel("Value of n")
plt.ylabel("Execution Time")
plt.plot(x_vals1, y_vals1)
plt.savefig("ex1.6.1.jpg")





