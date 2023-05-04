"""Maori games Yes/No
based on 01_yes_no_v3
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


#  Main routine goes here...
show_instruction = yes_no("Have you played this game before?")
print(f"You entered '{show_instruction}'")
print()
if show_instruction == "No":
    print("Instruction")
    print()
else:
    print("program continues")
