"""Trying different ways to create a quiz code.
Experimenting with different method.
Trying out 2-dimensional list in this code
"""
import random


quiz_2 = [["Rahina", "MONDAY"], ["Ratu", "TUESDAY"], ["Raapa", "WEDNESDAY"], ["Rapare", "THURSDAY"],
                     ["Ramere", "FRIDAY"], ["Rahoroi", "SATURDAY"], ["Ratapu", "SUNDAY"]]


random.shuffle(quiz_2)

for i in quiz_2:
    question_1 = input("What is {}: ".format(i[0]))
    if question_1 == i[1]:
        print("correct")
    else:
        print("Wrong")

