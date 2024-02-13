import json
import timeit

total = 0

#read file
with open(r"part2\large-file.json", 'r', encoding = "utf-8") as file:
    data = json.load(file)


    def changeSize():
        for i in range(len(data)): 
            data[i]["size"] = 42 

    changeSize()
        
    time_taken = timeit.timeit(stmt = "changeSize()", setup = "from __main__ import changeSize", number = 10)

    avg_time_taken = time_taken / 10
    
    print("Average Time Taken:", avg_time_taken, "seconds")


data.reverse()

f = open('output.2.3.json', 'w', encoding = "utf8")
f.write(json.dumps(data))
f.close()
