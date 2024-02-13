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

    tm = timeit.repeat(stmt = "changeSize()", setup="from __main__ import changeSize", repeat = 1000, number=100)
        
data.reverse()

f = open('output.2.3.json', 'w', encoding = "utf8")
f.write(json.dumps(data))
f.close()


#bins = [0.00006, 0.00007, 0.00008, 0.00009, 0.00010, 0.00011, 0.00012, 0.00013]
n, bins, edges = plt.hist(tm)
plt.xticks(bins)
plt.xlabel("Time (seconds)")
plt.ylabel("Number of Records")
plt.title("Time Taken Vs. Number of Recods")
plt.savefig("output.3.3.png")
plt.show
