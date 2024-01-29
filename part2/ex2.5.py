import json
import timeit

total = 0

#read file
with open(r"C:\ENSF338\lab_01\part2\large-file.json", 'r', encoding = "utf-8") as file:
    data = json.load(file)


    def changeSize():
        for i in range(len(data)): 
            data[i]["size"] = 42 

    changeSize()
        
    time_taken = timeit.repeat(stmt = "changeSize()", setup = "from __main__ import changeSize", repeat = 10, number = 1)

    for i in time_taken:
        total += i
    
    avg_time_taken = total / len(time_taken)

    print("Average Time Taken:", avg_time_taken, "seconds")


data.reverse()

f = open('output.2.3.json', 'w', encoding = "utf8")
f.write(json.dumps(data))
f.close()
