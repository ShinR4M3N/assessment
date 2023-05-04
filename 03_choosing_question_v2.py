"""Maori games Yes/No
Simplifies the input by converting it to lower case. Also, accepts y or n as
abbreviation. Prints result of user choice as well as input - for testing
"""

# Ask the user what quiz they would like to play
question = input("What quiz would you like to play?: ").lower()

# If they say 'o', proceeds to quiz 1'
if question == "o" or question == "one":
    print("Displays quiz set one")

# If they say 't', proceeds to quiz 2'
elif question == "t" or question == "two":
    print("Display quiz set two")

# If they say 'x', exits program
elif question == "x":
    print("Thank you for playing")
# Otherwise - show error
else:
    print("Please answer 'o' or 't' or 'x' to exit")

print(f"You entered '{question}'")
