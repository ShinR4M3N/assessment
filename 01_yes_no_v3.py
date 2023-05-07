"""Maori games Yes/No
Puts the code created in v2 into a loop to make testing easier and more
efficient
"""
show_instruction = ""
while show_instruction != "x":
    # Ask the user if they have played before
    show_instruction = input("What quiz would you like to play?: ").lower()

    # If they say yes, output 'Program Continues'
    if show_instruction == "yes" or show_instruction == "y":
        print("Program continues")

    # If they say no, output 'Display Instruction'
    elif show_instruction == "no" or show_instruction == "n":
        print("Display instruction")

    # Otherwise - show error
    else:
        print("Please answer 'yes' or 'no'")

print("Goodbye")
