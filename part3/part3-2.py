import json
import timeit

num_of_records = [1000, 2000, 5000, 10000]

#read file
with open(r"C:\ENSF338\lab_01\part2\large-file.json", 'r', encoding = "utf-8") as file:
    data = json.load(file)


    for i in range(len(data)): 
        data[i]["size"] = 42 




    data2 = [None] * len(data)

    for j in range(len(data) - 1, -1, -1):
        data2[j] = data[(len(data) - 1) - j]
    json_object = json.dumps(data2, indent=1)


with open(r"C:\ENSF338\lab_01\part2\output.2.3.json", 'w', encoding= "utf-8") as file2:
    file2.write(json_object)


