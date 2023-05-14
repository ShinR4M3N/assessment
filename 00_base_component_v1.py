""" 00 Base component of maori quiz
"""
import random


def yes_no(question_text: object) -> object:
    while True:

        # Ask the user if they have played before
        answer = input(question_text).lower()

        # If they say yes, output 'Program Continues'
        if answer == "yes" or answer == "y":
            answer = "Yes"
            return answer

        # If they say no, output 'Display Instruction'
        elif answer == "no" or answer == "n":
            answer = "No"
            return answer


        # Otherwise - show error
        else:
            print("Please answer 'yes' or 'no'")


def instructions():
    print("**** How to play ****")
    print()
    print("The rule of the game will go here")
    print()


def question(question_text):
    while True:

        # Ask the user what question they want to play
        answer = input(question_text).lower()

        # If they say "o", Program displays question set 1 and continues
        if answer == "one" or answer == "o":
            answer = "one"
            return answer

        # If they say "t", Program displays question set 2 and continues
        elif answer == "two" or answer == "t":
            answer = "two"
            return answer
        # If they say "x", it displays "Thank you for using our program," and exits
        elif answer == "x":
            return answer

        # Otherwise - show error
        else:
            print("Please answer 'o' or 't' or press 'x' to exit")


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
            point -= 1

    print(f"Your score was {point} points")


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
            point -= 1

    print(f"Your score was {point} points")


def formatter(symbol, text):
    sides = symbol * 3
    formatted_text = f"{sides} {text} {sides}"
    top_bottom = symbol * len(formatted_text)
    return f"{top_bottom}\n{formatted_text}\n{top_bottom}"


# main routine
print(formatter("-", "Welcome to Maori Quiz"))
print()
played_before = yes_no("Have you play this game before?")
if played_before == "No":
    instructions()
    start = yes_no("Are you ready to start? (yes to continue no to exit)")
else:
    start = "Yes"

while start == "Yes":
    question_no = question("What question would you like to play?"
                           "\nPress 'o' for question set 1"
                           "\nPress 't' for question set 2"
                           "\nOr 'x' to exit")
    play_again = "yes"
    if question_no == "one":
        generate_question_1()

    elif question_no == "two":
        generate_question_2()

    elif question_no == "x":
        print(formatter("#", "Thank you for using our program"))
        start = "No"


