"""Trying different ways to create a quiz code.
Experimenting with different method.
Trying out 2-dimensional list in this code
"""
import random
# This is using two multidimensional (2-dimensional) list

# 1nd list

Quiz_1 = [["tahi", 1], ["rua", 2], ["toru", 3], ["wha", 4], ["rima", 5],
          ["ono", 6], ["whitu", 7], ["waru", 8], ["iwa", 9], ["tekau", 10]]

question_1 = input(f"What number is {Quiz_1}?: ")

random.shuffle(Quiz_1)

for i in Quiz_1:
    question_1 = input("What is {}: ".format(i[0]))
    if question_1 == i[1]:
        print("correct")
    else:
        print("Wrong")

