import timeit

with open("part2/pg2701.txt", "r", encoding="utf-8") as file:
    file.seek(915)
    vowels = ["a", "e", "i", "o", "u", "y", "A", "E", "I", "O", "U", "Y"]
    lines = file.readlines()

def test():

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

time_taken = timeit.timeit(stmt = "test()", setup = "from __main__ import test", number = 100)

avg_time_taken = time_taken / 100

print("Average Time Taken: ", avg_time_taken)




        




        
