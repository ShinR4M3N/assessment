"""Trying different ways to create a quiz code.
Experimenting with different method.
Trying out 2-dimensional list in this code
"""

import random

# This uses two multi dimensional (2-dimensional) lists

# 1nd list
Maori_numbers = ["tahi", "rua", "toru", "wha", "rima", "ono", "whitu", "waru", "iwa", "tekau"]

# 2st list
number = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]

choice = input("Enter quiz: 'o' for quiz 1 and 't' for quiz 2")

if choice == "o":
    choice == "o"
else:
    choice == "t"

random.shuffle(choice)

for i in choice:
    answer = input("What is {}?: ".format(i[0]))
    if answer == i[1]:
        print("Correct")

    else:
        print("incorrect")


