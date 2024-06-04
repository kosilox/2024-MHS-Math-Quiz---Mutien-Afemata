def yes_no(question):
    while True:
        response = input(question).lower()
        # checks user response, question
        # repeats if users don't enter yes / no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Invalid, Please input only y/n")
while True:
    instructions = yes_no("Do you want to read the instructions? ")
    if instructions == "yes":
        print("\nUSER INPUT: YES\n")
        pass
    if instructions == "no":
        print("\nUSER INPUT: NO\n")
        pass
    if instructions == ValueError:
        print("\nUSER INPUT: INVALID\n")
        pass