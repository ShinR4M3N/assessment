"""Trying different ways to create a quiz code.
Experimenting with different method.
Trying out 1-dimensional list in this code
"""

import random

# This uses two ordinary (1-dimensional) lists

# 1nd list
Maori_numbers = ["tahi", "rua", "toru", "wha", "rima", "ono", "whitu", "waru", "iwa", "tekau"]

# 2st list
number = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]


quiz_1 = random.choice(Maori_numbers)

question_1 = input(f"What number is {quiz_1}?: ")

# Using the index position of the question in one list to find the corresponding
# index position of the answer
quiz_1_answer = Maori_numbers.index(quiz_1)
answer = number[quiz_1_answer]

if question_1 == answer:
    print("Correct")

else:
    print("Incorrect")
