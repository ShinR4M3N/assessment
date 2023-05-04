"""Creating function code of instruction and adding on to yes_no
Gets the result of yes or no from yes_no function
Displays instruction when you input no into yes no function
"""


# Function goes here...


def yes_no(question_text):
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


# function to display instruction
def instructions():
    print("**** How to play ****")
    print()
    print("The rule of the game will go here")
    print()
    print("Program continues")
    print()

#  Main routine goes here...


show_instruction = yes_no("Have you played this game before?")
print(f"You entered '{show_instruction}'")
print()
if show_instruction == "No":
    instructions()
else:
    print("program continues")
