"""Maori games Yes/No
Puts the code created in v2 into a loop to make testing easier and more
efficient
"""
question = ""
while question != "x":
    # Ask the user what quiz they would like to play
    show_instruction = input("What quiz would you like to play?: ").lower()

    # If they say 'o', proceeds to quiz 1'
    if question == "o" or question == "one":
        print("Displays quiz set one")

    # If they say 't', proceeds to quiz 2'
    elif question == "t" or question == "two":
        print("Display quiz set two")

    # Otherwise - show error
    else:
        print("Please answer 'yes' or 'no'")

print("Goodbye")
