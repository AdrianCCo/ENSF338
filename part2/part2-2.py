with open("C:/ENSF338/lab_01/pg2701.txt", "r", encoding="utf-8") as file:
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

print(vowel_count, word_count)
avg_count = float(vowel_count / word_count)

print(avg_count)

        




        
