# Ask the user what quiz they would like to play
question = input("What quiz would you like to play? :")

# If they say 'o', proceeds to quiz 1'
if question == "o":
    print("Question set 1")

# If they say 't', proceeds to quiz 2'
elif question == "t":
    print("Question set 2")
# If they say 'x', exits program
elif question == "x":
    print("Goodbye")

# Otherwise - show error
else:
    print("Please answer 'o' or 't' or 'x' to exit")
