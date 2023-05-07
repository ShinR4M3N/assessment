"""Made a list inside the list and removed a 2nd list from v1
The code generates question and gets the answer from its list.
"""

import random

# This uses two ordinary (1-dimensional) lists

# 1nd list
Maori_numbers = [["tahi", "1"], ["rua", "2"], ["toru", "3"], ["wha", "4"], ["rima", "5"],
                ["ono", "6"], ["whitu", "7"], ["waru", "8"], ["iwa", "9"], ["tekau", "10"]]

# Generates random question
quiz_1 = random.choice(Maori_numbers)

# Asks for question
question_1 = input(f"What number is {quiz_1[0]}?: ")

# There is a list inside the list and the answer is in the 2nd position
answer = quiz_1[1]

if question_1 == answer:
    print("correct")
else:
    print("wrong")



