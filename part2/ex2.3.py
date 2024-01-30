import json

#read file
f = open('part2\large-file.json', 'r', encoding = "utf8")
data = json.load(f)
f.close

#data.reverse()

for i in range(len(data)):
    data[i]["size"] = 42

data.reverse()

f = open('part2\output.2.3.json', 'w', encoding = "utf8")
f.write(json.dumps(data))
f.close()
