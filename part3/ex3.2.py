import json
import random
import timeit
from matplotlib import pyplot as plt
plt.rcParams['figure.figsize'] = [10, 5]
import numpy as np

#read file
with open(r"C:\Users\HP\Documents\ENSF338\Lab1\large-file.json", 'r', encoding = "utf-8") as file:
    data = json.load(file)
    num_of_records = [1000, 2000, 5000, 10000]

    def changeSize():
        for i in range(record): 
            data[i]["size"] = 42 

    avgtimes = []
    for record in num_of_records:
        rez = []
        tm = timeit.timeit(stmt = "changeSize()", setup="from __main__ import changeSize", number=100)
        rez.append(tm/100)
        avg = sum(rez) / len(rez)
        avgtimes.append(avg)
        print("Average time for the first %d records: %f" % (record, avg))
        
data.reverse()

f = open('output.2.3.json', 'w', encoding = "utf8")
f.write(json.dumps(data))
f.close()


from IPython.display import Video
Video("linear.mp4", embed=True)
slope, intercept = np.polyfit(num_of_records, avgtimes, 1)
plt.scatter(num_of_records, avgtimes)
linevalues = [slope * x + intercept for x in num_of_records]
plt.plot(num_of_records, linevalues, 'r')
plt.title("Number of Records VS. Average Processing Time")
plt.xlabel("Number of Records")
plt.ylabel("Average Processing Time (seconds)")
plt.savefig("output.3.2.png", format = "png")
# Finally, print out the linear relationship between input length and time.
#print("The linear model is: t = %.2e * n + %.2e" % (slope, intercept))
