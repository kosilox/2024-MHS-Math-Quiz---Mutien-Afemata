import random
import math
# checks if input is a valid integer
def int_check(question, low=None, high=None, exit_code=None):

    # if any integer is allowed...
    if low is None and high is None:
        error = "\nPlease enter an integer\n"

    # if the number needs to be more than an
    # integer (ie: rounds / ' high number '
    elif low is not None and high is None:
        error = (f"Please enter an integer that is "
                 f"more than / equal to {low}")

    # if the number needs to between low & high
    else:
        error = (f"Please enter an integer that "
                 f"is between {low} and {high} (inclusive)")

    while True:
        response = input(question).lower()

        # check for infinite mode / exit code
        if response == exit_code:
            return response

        try:
            response = int(response)
            # Check the integer is not too low...
            if low is not None and response < low:
                print(error)

            # check response is more than the low number
            elif high is not None and response > high:
                print(error)

            # if response is valid, return it
            else:
                return response

        except ValueError:
            print(error)

# checks if users enter yes or no
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
            print("Please enter yes / no")

def instructions():
    print('''

**** Instructions ****

To begin, choose the amount of questions you're willing to solve
and then choose from the following math modes:
Addition, Subtraction, Multiplication or Division.

Your goal is to try to guess as many correct as possible,
this is to test your arithmetic math knowledge!

Good luck.


    ''')

# initialise game variables
user_scores = []
game_history = []

user_exit = ""
feedback = ""
mode = "regular"
questions_ans = 0


print("Welcome to the MHS Math Quiz!")
print()

want_instructions = yes_no("Do you want instructions?")

if want_instructions == "yes":
    instructions()
    pass

num_questions = int_check("Number of questions? ",
                          low=1, exit_code="")
if num_questions == "":
    mode = "infinite"
    num_questions = 5
    print(f"{mode} mode activated")


# game loop starts here
while questions_ans < num_questions:

    # Rounds headings (based on mode)
    if mode == "infinite":
        rounds_heading = f"\n Question {questions_ans + 1} (Infinite mode)"
    else:
        rounds_heading = f"\n Question {questions_ans + 1} of {num_questions}"

    print(rounds_heading)
    print()

    # get user choice
    user_choice = input("Choose: ")

    # if user choice is the exit code, break the loop
    if user_choice == "xxx":
        break

    questions_ans += 1

    # if users are in infinite mode, increase number of rounds!
    if mode == "infinite":
        num_questions += 1


