"""Trying different ways to create a quiz code.
Experimenting with different method.
Trying out 2-dimensional list in this code
"""
import random
question_asked = 0
play_again = ""
# This is using two multidimensional (2-dimensional) list

# 1nd list

Quiz_1 = [["tahi", "1"], ["rua", "2"], ["toru", "3"], ["wha", "4"], ["rima", "5"],
          ["ono", "6"], ["whitu", "7"], ["waru", "8"], ["iwa", "9"], ["tekau", "10"]]

# 2st list
Quiz_2 = [["rahina", "monday"], ["ratu", "tuesday"], ["raapa", "wednesday"], ["rapare", "thursday"],
          ["ramere", "Friday"], ["rahoroi", "Saturday"],
          ["ratapu", "Sunday"]]
while question_asked <= 10:
    choice = input("Enter 'o' for question 1, 't' for question 2, and press 'x' to exit")
    question_asked += 1
    if choice == "o":
        choice = Quiz_1
    elif choice == "t":
        choice = Quiz_2
    elif choice == "x":
        print("Goodbye")
    else:
        print("Try again")

    random.shuffle(choice)

    for i in choice:
        answer = input("What is {}: ".format(i[0]))
        if answer == i[1]:
            print("correct")
        else:
            print("Wrong")

