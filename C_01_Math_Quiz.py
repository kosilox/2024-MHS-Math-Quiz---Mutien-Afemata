import random

# checks user answer and compares to real answer
def ans_compare(user, ans):
    # if the user and the answer is the same, it's a win
    if user == ans:
        quiz_result = "win"
    # if not the same, then it's a loss
    else:
        quiz_result = "lose"
    return quiz_result


def string_checker(question, valid_ans=('yes', 'no')):

    error = (f"Please enter a valid option from the following list: {valid_ans}")

    while True:

        # Get user response and make sure it's lowercase
        user_response = input(question).lower()

        for i in valid_ans:
            # check if the user response is a word in the list
            if i == user_response:
                return i

            # check if the user response is the same as
            # the first letter of an item in the list
            elif user_response == i[0]:
                return i

        # print error if user does not enter something that is valid
        print(error)
        print()


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


def instructions():
    print('''

**** Instructions ****

To begin, choose how many questions you would like and 
then choose any of the operations which will be set to your question:

 [addition, subtraction, multiplication, division]
 
You can press <enter> for a mix of all of these. 
Press <xxx> to exit the quiz at anytime.

Your goal is to try to guess as many correct as possible,
This is to test your arithmetic math knowledge!

Good luck.


    ''')


# main routine starts here
# initialise game variables

operations = ["addition", "subtraction", "multiplication", "division", "everything"]
quiz_history = []

questions_answered = 0
incorrect_guesses = 0
quiz_feedback = ""
mode = "regular"

# quiz begins here
print("Welcome to the MHS Arithmetic Math Quiz!")
print()

want_instructions = string_checker("Do you want instructions?")

if want_instructions == "yes":
    instructions()
    pass

# asks how many questions user wants
num_questions = int_check("How many questions would you like? "
                          "(Press <enter> for infinite mode) ",
                          low=1, exit_code="")
if num_questions == "":
    mode = "infinite"
    num_questions = 5

# ask the choice of operations
# user wants to solve for each question
operation_mode = string_checker("\nChoose the operation: "
                               "(type 'e' for all operations) ",
                                operations)

# if user inputs <enter> then pass straight into quiz loop
if operation_mode == "everything":
    pass

print(operation_mode)
# quiz loop starts here
while questions_answered < num_questions:

    # question headings (based on mode)
    if mode == "infinite":
        rounds_heading = f"\n Question {questions_answered + 1} (Infinite mode)"
    else:
        rounds_heading = f"\n Question {questions_answered + 1} of {num_questions}"

    print(rounds_heading)
    print()

    # initialize variables
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = 0
    user_input = ""
    feedback = ""

    # mixed_operations acts as a 2nd operation mode if
    # user wants all operation in their questions
    mixed_operations = ""

    if operation_mode == "everything":
        # chooses a random operation from the operation list
        # except for 'everything'
        mixed_operations = random.choice(operations[:4])

    if operation_mode == "addition" or mixed_operations == "addition":
        c = (a * a) + (b * b)
        feedback = f"{a * a} + {b * b} = ?"

    if operation_mode == "subtraction" or mixed_operations == "subtraction":
        c = (a * a) - (b * b)
        feedback = f"{a * a} - {b * b} = ?"

    if operation_mode == "multiplication" or mixed_operations == "multiplication":
        c = (a * b)
        feedback = f"{a} * {b} = ?"

    if operation_mode == "division" or mixed_operations == "division":
        c = (a * b) / a
        feedback = f"{a * b} / {a} = ?"

    # FOR TESTING PURPOSES
    print(f"answer = {c}")

    # shows user the question
    print(feedback)

    # get user answer
    user_input = int_check("Solve: ", exit_code="xxx")

    # if user choice is the exit code, break the loop
    if user_input == "xxx":
        break

    result = ans_compare(user_input, c)

    # adjust game lost / game won counters and add results to game history
    if result == "win":
        quiz_feedback = "You guessed it correct!"
    if result == "lose":
        incorrect_guesses += 1
        quiz_feedback = f"Wrong, the answer is {c}"

    # set up question feedback and output it to user
    # add it to the game history list (include the question number)
    question_feedback = f"User: {user_input} | Question: {feedback} \nAnswer: {c} | Result: {quiz_feedback}\n"
    history_item = f"Question: {questions_answered + 1} - {question_feedback}"

    print(question_feedback)
    quiz_history.append(history_item)

    questions_answered += 1

    # if users are in infinite mode, increase number of rounds!
    if mode == "infinite":
        num_questions += 1

# quiz loops ends here

if questions_answered > 0:
    # game history / statistics area

    # calculate statistics
    correct_guesses = questions_answered - incorrect_guesses
    percent_won = correct_guesses / questions_answered * 100
    percent_loss = incorrect_guesses / questions_answered * 100


    print("📈📈📈Game Statistics📈📈📈")
    print(f"Wrong Guesses: {percent_loss:.2f} |\t"
          f"Correct Guesses: {percent_won:.2f}\t")

    # ask user if they want to see their game history and output it if requested.
    see_history = string_checker("\nDo you want to see your quiz history? ")
    if see_history == "yes":
        for item in quiz_history:
            print(f"\n{item}\n")

    print()
    print("Thanks for playing.")
else:
    # if user didn't answer any questions
    print("oops, you chickened out")
