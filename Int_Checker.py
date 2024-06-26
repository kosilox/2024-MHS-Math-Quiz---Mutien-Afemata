import random

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



secret_number = random.randint(1, 180)

num_questions = int_check("How many questions would you like to solve? ",
                          low=1, exit_code="")
if num_questions == "":
    mode = "infinite"
    num_questions = 5
    print(f"{mode} mode activated")

print("program continues")