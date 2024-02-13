import json
import numpy as np
from matplotlib import pyplot as plt

#read file
with open("C:/ENSF338/lab_01/part3/internetdata.json", 'r', encoding = "utf-8") as file:
    data = json.load(file)


data_set1 = {}
data_set2 = {}

for i in range(len(data)):
    if data[i]["incomeperperson"] is None or data[i]["internetuserate"] is None:
        continue
    elif data[i]["incomeperperson"] < 10000.0:
        data_set1[data[i]["internetuserate"]] = data[i]["incomeperperson"]
    elif data[i]["incomeperperson"] >= 10000.0:
        data_set2[data[i]["internetuserate"]] = data[i]["incomeperperson"]    
    else:
        continue  

plt.style.use('seaborn-v0_8-deep')

iur1 = data_set1.keys()
ipp1 = data_set1.values()


iur2 = data_set2.keys()
ipp2 = data_set2.values()

bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

plt.hist(x = iur1, bins=bins, edgecolor = 'tomato')
plt.title("Data Set 1")
plt.xlabel("Internet Usage Rate")
plt.ylabel("Number of Countries")
plt.savefig("hist1.png")
plt.show()

plt.hist(x = iur2, bins=bins, edgecolor = 'tomato')
plt.title("Data Set 2")
plt.xlabel("Internet Usage Rate")
plt.ylabel("Number of Countries")
plt.savefig("hist2.png")
plt.show

