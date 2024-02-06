# 5.4) The linear search is a linear function, and then binary search is a logarithmic function. The parameters of the linear plot
# are vector_sizes and linear_avgtimes. The parameters of the binary plot are x (vector_sizes), a, and b. 

import timeit
import random
from matplotlib import pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

vector_sizes = [1000, 2000, 4000, 8000, 16000, 32000]

def linear_search(arr, target):
    for i, num in enumerate(arr):
        if num == target:
            return i
    return -1

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def search_performance(function):
    avgtimes = []
    for vector_size in vector_sizes:
        target = random.randint(0, vector_size - 1)
        arr = [random.randint(0, 1000) for _ in range(vector_size)]
        rez = []
        for _ in range(1000):
            tm = timeit.timeit(lambda: function(arr, target), number=100)
            rez.append(tm/100)
        avg = sum(rez) / len(rez)
        avgtimes.append(avg)
    return avgtimes

linear_avgtimes = search_performance(linear_search)
binary_avgtimes = search_performance(binary_search)

def log_function(x, a, b):
    return a * np.log(b * x)

# Plot Linear Search
plt.figure()
plt.scatter(vector_sizes, linear_avgtimes)
slope, intercept = np.polyfit(vector_sizes, linear_avgtimes, 1)
linevalues = [slope * x + intercept for x in vector_sizes]
plt.plot(vector_sizes, linevalues, 'r', label='Linear Search')
plt.title("Linear Search Performance")
plt.xlabel("Vector Size")
plt.ylabel("Average Processing Time (seconds)")
plt.legend()

# Plot Binary Search
plt.figure()
plt.scatter(vector_sizes, binary_avgtimes)
popt, pcov = curve_fit(log_function, vector_sizes, binary_avgtimes)
plt.plot(vector_sizes, log_function(np.array(vector_sizes), *popt), 'g', label='Binary Search')
plt.title("Binary Search Performance")
plt.xlabel("Vector Size")
plt.ylabel("Average Processing Time (seconds)")
plt.legend()

plt.show()