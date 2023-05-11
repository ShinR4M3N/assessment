"""Trying different ways to create a quiz code.
Experimenting with different method.
Trying out 1-dimensional list in this code
"""

import random

# This uses two ordinary (1-dimensional) lists

# 1nd list
Maori_numbers = [["tahi", "1"], ["rua", "2"], ["toru", "3"], ["wha", "4"], ["rima", "5"],
                 ["ono", "6"], ["whitu", "7"], ["waru", "8"], ["iwa", "9"], ["tekau", "10"]]

quiz_1 = random.choice(Maori_numbers)

question_1 = input(f"What number is {quiz_1[0]}?: ")

# Using the index position of the question in one list to find the corresponding
# index position of the answer
quiz_1_answer = Maori_numbers.index(quiz_1)
answer = Maori_numbers[0]

if question_1 == Maori_numbers:
    print("Correct")
else:
    print("Incorrect")
