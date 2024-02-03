import timeit
import matplotlib.pyplot as plt
import numpy as np

memory = dict()
time_dict_funci = {}
time_dict_func = {}

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


for i in range(36):
    elapsed_time = timeit.timeit(stmt = f"funci({i}, {memory})", setup = "from __main__ import funci", number = 1)
    time_dict_funci[i] = elapsed_time  

for i in range(36):
    elapsed_time = timeit.timeit(stmt = f"func({i})", setup = "from __main__ import func", number = 1)
    time_dict_func[i] = elapsed_time  

print(time_dict_func)

print(time_dict_funci)

plt.style.use("fivethirtyeight")

plt.style.use
x_vals2 = time_dict_funci.values()
y_vals2 = time_dict_funci.keys()
plt.title("Data Set for funci()")
plt.xlabel("Execution Time")
plt.ylabel("Value of n")
plt.plot(x_vals2, y_vals2)
plt.savefig("ex1.6.2.jpg")
plt.show()

x_vals1 = time_dict_func.values()
y_vals1 = time_dict_func.keys()
plt.title("Data Set for func()")
plt.xlabel("Execution Time")
plt.ylabel("Value of n")
plt.plot(x_vals1, y_vals1)
plt.savefig("ex1.6.1.jpg")

