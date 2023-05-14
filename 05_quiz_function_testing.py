"""Copy and pasted 04 function as this will have the 2nd load of questions.

"""

# Changed the name of this function as its going to be a seperate function.


def generate_question_2():
    import random
    number_of_quiz = 0
    point = 0
    # shows what question you are on
    rounds = 1

    # This uses two ordinary (1-dimensional) lists

    # 1nd list
    maori_days = [["Rahina", "MONDAY"], ["Ratu", "TUESDAY"], ["Raapa", "WEDNESDAY"], ["Rapare", "THURSDAY"],
                     ["Ramere", "FRIDAY"], ["Rahoroi", "SATURDAY"], ["Ratapu", "SUNDAY"]]

    # runs for 10 questions and stops
    while number_of_quiz <= 6:
        # Generates random question
        quiz_1 = random.choice(maori_days)

        # Asks for question
        question_1 = input(f"#{rounds} What day is {quiz_1[0]}?: ").upper()
        # adds a round to the number of quiz
        number_of_quiz += 1
        rounds += 1
        # When a question has been displayed, remove that question so that questions would not overlap
        maori_days.remove(quiz_1)

        # There is a list inside the list and the answer is in the 2nd position
        answer = quiz_1[1]

        if question_1 == answer:
            print("Well done !correct")
            # Adds one point when user gets question correct
            point += 1
        else:
            print("Nice try:( wrong")
            # minus one point when user gets question wrong
            point -= 1
    print(f"Your score was {point} points")


# Main routine
generate_question_2()
play_again = input("Do you want to play again?")
if play_again == "yes":
    generate_question_2()
else:
    print("Goodbye")
