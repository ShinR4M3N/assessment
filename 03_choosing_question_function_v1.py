""" Created a Function of the instruction program based of v3
"""


# Function goes here...


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


#  Main routine goes here...
question_no = question("What question would you like to play?"
                       "\nPress o for question set 1"
                       "\nPress t for question set 2"
                       "\nOr 'x' to exit")

print()
if question_no == "one":
    print("question set one")
    print()
elif question_no == "two":
    print("Question set two")
else:
    print("Thank you for using our program")
