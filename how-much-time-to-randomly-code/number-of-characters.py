dif_characters = []
number_of_caracters = 0

with open("steermaster-code.txt", "r", encoding="utf-8") as f:
    
    all_lines = f.readlines()

    for line in all_lines:
        for char in line:
            if char not in dif_characters and char != '\n':
                dif_characters.append(char)
            number_of_caracters += 1

dif_characters
print(len(dif_characters))
print(number_of_caracters)




