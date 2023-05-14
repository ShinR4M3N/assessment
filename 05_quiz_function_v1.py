"""
Made the previous version into a function.
"""
import random


def generate_question_2():
    number_of_quiz = 0
    point = 0
    # shows what question you are on
    rounds = 1

    # 1nd list
    maori_days = [["Rahina", "MONDAY"], ["Ratu", "TUESDAY"], ["Raapa", "WEDNESDAY"], ["Rapare", "THURSDAY"],
                  ["Ramere", "FRIDAY"], ["Rahoroi", "SATURDAY"], ["Ratapu", "SUNDAY"]]

    # Generates random question
    random.shuffle(maori_days)

    # adds a round to the number of quiz
    number_of_quiz += 1
    rounds += 1

    # There is a list inside the list and the answer is in the 2nd position
    for i in maori_days:
        # added .upper so that it returns true if letters are uppercase
        question_2 = input("What day is '{}': ".format(i[0])).upper()
        if question_2 == i[1]:
            print("Correct")
            point += 1
        else:
            print("wrong")
            point -= 0

    print(f"Your score was {point} points")


# Main routine
generate_question_2()
# end user testing y/n
play_again = input("Do you want to play again?")
if play_again == "yes":
    generate_question_2()
else:
    print("Goodbye")
# more short simple efficient
