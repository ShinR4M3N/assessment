""" Final version of the program
All the feedbacks from the end user has been included (Format, Adding round numbers)

"""
import random


# Yes no checker. It asks for an answer of either yes or no. When something else it entered, it outputs an error

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
            print("Please answer 'yes' or 'no': ")

# Function that generates instructions on how to play this game


def instructions():
    print("**** How to play ****")
    print()
    print("This is a Maori quiz game\nThere are 2 sets of quiz.\nQuiz One being Maori Numbers from 1 to 10"
          " and Quiz Two being Maori Day of the week\nYou can select the questions by typing"
          " o or one for set 1 and t or two for set 2\n"
          "You will gain 1 point from getting question correct and lose 1 when you get something wrong\n"
          "Now good luck and have fun!")
    print()

# A Menu function where it asks the user what game they would like to play.


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
            print("Please answer 'o' or 't' or press 'x' to exit program: ")

# Generates Maori numbers from 1 to 10 randomly with no repetitive question. Runs until all the words has run out from
# the list


def generate_question_1():
    point = 0
    # shows what question you are on
    rounds = 1

    # 1nd list
    maori_numbers = [["tahi", "1"], ["rua", "2"], ["toru", "3"], ["wha", "4"], ["rima", "5"],
                     ["ono", "6"], ["whitu", "7"], ["waru", "8"], ["iwa", "9"], ["tekau", "10"]]

    # Generates random question
    random.shuffle(maori_numbers)

    # There is a list inside the list and the answer is in the 2nd position
    for i in maori_numbers:
        print(f"Round {rounds}")
        rounds += 1
        question_1 = input("What number is '{}': ".format(i[0]))
        if question_1 == i[1]:
            print("Correct")
            point += 1
        else:
            print("wrong")
            point -= 1

    print(f"Your score was {point} points")

# 2nd quiz function where it generates Days of the week in Maori. It also runs until all the words has run out/


def generate_question_2():
    point = 0
    # shows what question you are on
    rounds = 1

    # 1nd list
    maori_days = [["Rahina", "MONDAY"], ["Ratu", "TUESDAY"], ["Raapa", "WEDNESDAY"], ["Rapare", "THURSDAY"],
                  ["Ramere", "FRIDAY"], ["Rahoroi", "SATURDAY"], ["Ratapu", "SUNDAY"]]

    # Generates random question
    random.shuffle(maori_days)

    # There is a list inside the list and the answer is in the 2nd position
    for i in maori_days:
        print(f"Round {rounds}")
        rounds += 1
        # added .upper so that it returns true if letters are uppercase
        question_2 = input("What day is '{}': ".format(i[0])).upper()
        if question_2 == i[1]:
            print("Correct")
            point += 1
        else:
            print("wrong")
            point -= 1

    print(f"Your score was {point} points")

# It formats text to make it more interesting instead of being empty and mid


def formatter(symbol, text):
    sides = symbol * 3
    formatted_text = f"{sides} {text} {sides}"
    top_bottom = symbol * len(formatted_text)
    return f"{top_bottom}\n{formatted_text}\n{top_bottom}"


# main routine
print(formatter("-", "Welcome to Maori Quiz!"))
print()
played_before = yes_no("Have you play this game before? Please enter 'yes or 'no': ")
# Displays instruction when answer equals no
if played_before == "No":
    instructions()
    start = yes_no("Are you ready to start? (type 'yes' to continue 'no' to exit): ")

# When answer equals yes, it directs into the menu function called question
else:
    start = "Yes"

# The user can choose what to play by typing "o" or "t" or they can press x to exit
while start == "Yes":
    question_no = question("What question would you like to play?"
                           "\nPress 'o' for question set 1"
                           "\nPress 't' for question set 2"
                           "\nOr 'x' to exit: ")
    play_again = "yes"
    # When the user enters "o" it generates question set 1
    if question_no == "one":
        generate_question_1()

    # When the user enters "t" it generates question set 2
    elif question_no == "two":
        generate_question_2()

    # Exits program when "x" is entered
    elif question_no == "x":
        start = "No"
# Exits program
if start == "No":
    print(formatter("#", "Thank you for using our program"))
