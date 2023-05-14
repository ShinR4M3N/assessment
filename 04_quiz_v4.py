"""Made v2 into a loop.
Added points system and number of rounds, however, it can still generate the same question
"""

import random
number_of_quiz = 0
point = 0

# This uses two ordinary (1-dimensional) lists

# 1nd list
Maori_numbers = [["tahi", "1"], ["rua", "2"], ["toru", "3"], ["wha", "4"], ["rima", "5"],
                ["ono", "6"], ["whitu", "7"], ["waru", "8"], ["iwa", "9"], ["tekau", "10"]]

# runs for 10 questions and stops
while number_of_quiz <= 9:
    # Generates random question
    quiz_1 = random.choice(Maori_numbers)

    # Asks for question
    question_1 = input(f"What number is {quiz_1[0]}?: ")
    number_of_quiz += 1
    Maori_numbers.remove(quiz_1)

    # There is a list inside the list and the answer is in the 2nd position
    answer = quiz_1[1]

    if question_1 == answer:
        print("correct")
        # Adds one point when user gets question correct
        point += 1
    else:
        print("wrong")
        # minus one point when user gets question wrong
        point -= 1

# Main routine
print(f"Your score was {point} points")
print(Maori_numbers)
play_again = input("Do you want to play again?")
if play_again == "yes":
    print("Quiz function")
else:
    print("Goodbye")

