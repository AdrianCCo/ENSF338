import json
import random
import timeit
from matplotlib import pyplot as plt
plt.rcParams['figure.figsize'] = [10, 5]
import numpy as np

#read file
with open(r"C:\Users\HP\Documents\ENSF338\Lab1\large-file.json", 'r', encoding = "utf-8") as file:
    data = json.load(file)
    num_of_records = [1000]

    def changeSize():
        for i in range(1000): 
            data[i]["size"] = 42 

    rez = []
    for i in range (1000):
        tm = timeit.timeit(stmt = "changeSize()", setup="from __main__ import changeSize", number=100)
        rez.append(tm/100)
    # Then, compute the average execution times across all
    # and add it to our list of average times
        
    data2 = [None] * len(data)

    for j in range(len(data) - 1, -1, -1):
        data2[j] = data[(len(data) - 1) - j]
    json_object = json.dumps(data2, indent=1)


with open(r"C:\Users\HP\Documents\ENSF338\Lab1\output.2.3.json", 'w', encoding= "utf-8") as file2:
    file2.write(json_object)


plt.hist(rez)
plt.xlabel("Time (seconds)")
plt.ylabel("Number of Records")
plt.title("Time Taken Vs. Number of Recods")
plt.savefig("output.3.3.png")
plt.show