"""Made the previous version into a function.

"""

# Created a function of the previous version


def generate_question_1():
    import random
    number_of_quiz = 0
    point = 0

    # This uses two ordinary (1-dimensional) lists

    # 1nd list
    maori_numbers = [["tahi", "1"], ["rua", "2"], ["toru", "3"], ["wha", "4"], ["rima", "5"],
                     ["ono", "6"], ["whitu", "7"], ["waru", "8"], ["iwa", "9"], ["tekau", "10"]]

    # runs for 10 questions and stops
    while number_of_quiz <= 9:
        # Generates random question
        quiz_1 = random.choice(maori_numbers)

        # Asks for question
        question_1 = input(f"What number is {quiz_1[0]}?: ")
        number_of_quiz += 1
        maori_numbers.remove(quiz_1)

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
    print(f"Your score was {point} points")


# Main routine
generate_question_1()
play_again = input("Do you want to play again?")
if play_again == "yes":
    generate_question_1()
else:
    print("Goodbye")
