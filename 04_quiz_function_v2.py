"""
Removed while loop from v1 and removed .choice and .remove by replacing it with .shuffle
"""
import random


def generate_question_1():
    number_of_quiz = 0
    point = 0
    # shows what question you are on
    rounds = 1

    # 1nd list
    maori_numbers = [["tahi", "1"], ["rua", "2"], ["toru", "3"], ["wha", "4"], ["rima", "5"],
                     ["ono", "6"], ["whitu", "7"], ["waru", "8"], ["iwa", "9"], ["tekau", "10"]]

    # Generates random question
    random.shuffle(maori_numbers)

    # adds a round to the number of quiz
    number_of_quiz += 1
    rounds += 1

    # There is a list inside the list and the answer is in the 2nd position
    for i in maori_numbers:
        question_1 = input("What number is '{}': ".format(i[0]))
        if question_1 == i[1]:
            print("Correct")
            point += 1
        else:
            print("wrong")
            point -= 0

    print(f"Your score was {point} points")


# Main routine
generate_question_1()
# end user testing y/n
play_again = input("Do you want to play again?")
if play_again == "yes":
    generate_question_1()
else:
    print("Goodbye")
# more short simple efficient
