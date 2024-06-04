# check that users have entered a valid
# option based on a list

# basic string checker for arithmetic mode
def string_checker(question, valid_ans=('yes', 'no')):

    error = f"Please enter a valid option from the following list: {valid_ans}"

    while True:

        # Get user response and make sure it's lowercase
        user_response = input(question).lower()

        for item in valid_ans:
            if item == user_response:
                return item
            # iterate through valid responses and return
            # full word if response is first letter of the item
            # or the full item
            elif user_response == item[0]:
                return item

        # print error if user does not enter something that is valid
        print(error)
        print()


# main routine goes here

operations = ["addition", "subtraction", "multiplication", "division", ""]

want_instructions = string_checker("Do you want to see the instructions?")

print("You chose ", want_instructions)

user_choice = string_checker("choose:" , operations)
print("You chose: ", user_choice)