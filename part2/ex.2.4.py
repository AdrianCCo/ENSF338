import timeit

def test():
    with open("C:/ENSF338/lab_01/part2/pg2701.txt", "r", encoding="utf-8") as file:
        file.seek(915)
        vowels = ["a", "e", "i", "o", "u", "y", "A", "E", "I", "O", "U", "Y"]
        lines = file.readlines()
        i = 0
        vowel_count = 0
        word_count = 0

        for line in lines:
            temp = list(line)
            for i in temp:
                if i in vowels:
                    vowel_count += 1

            x = line.split()

            for i in x:
                word_count += 1

    avg_count = float(vowel_count / word_count)

    return avg_count

time_taken = timeit.repeat(stmt = "test()", setup = "from __main__ import test", repeat = 100, number = 1)

total = 0

for i in range(len(time_taken)):
    total += time_taken[i]

avg_time_taken = total / len(time_taken)

print("Average Time Taken: ", avg_time_taken)




        




        
