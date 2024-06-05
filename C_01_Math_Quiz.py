import random

# checks user answer and compares to real answer
def ans_compare(user, ans):
    # if the user and the answer is the same, it's correct
    if user == ans:
        quiz_result = "correct"
    # if not the same, then it's incorrect
    else:
        quiz_result = "incorrect"
    return quiz_result


# checks if user input is a valid answer
def string_checker(question, valid_ans=('yes', 'no')):

    error = f"Please enter a valid option from the following list: {valid_ans}"

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
    # integer (ie: questions )
    elif low is not None and high is None:
        error = (f"Please enter an integer that is "
                 f"more than / equal to {low}")
    else:
        error = "\nPlease enter an integer\n"

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
 
You can type "everything" or "e" for a mix of all of these.
(you can also type the first letter of operations to choose them).
 
Press <xxx> to exit the quiz at anytime.

Your goal is to try to guess as many correct as possible,
This is to test your arithmetic math knowledge!

Good luck.


    ''')


# main routine starts here
# initialise question variables

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

# ask what operations user wants to solve for each question
operation_mode = string_checker("\nChoose the operation: "
                               "(type 'e' for all operations) ",
                                operations)

# if user inputs 'e' or 'everything' then pass straight into quiz loop
if operation_mode == "everything":
    pass

print("you have chosen", operation_mode)

# quiz loop starts here
while questions_answered < num_questions:

    # question headings (based on mode)
    if mode == "infinite":
        questions_heading = f"\n Question {questions_answered + 1} (Infinite mode)"
    else:
        questions_heading = f"\n Question {questions_answered + 1} of {num_questions}"

    print(questions_heading)
    print()

    # initialize variables
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = 0
    user_input = ""
    quiz_question = ""

    # mixed_operations acts as a 2nd operation mode if
    # user wants all operation in their questions
    mixed_operations = ""

    if operation_mode == "everything":
        # chooses a random operation from the operation list
        # except for 'everything'
        mixed_operations = random.choice(operations[:4])

    if operation_mode == "addition" or mixed_operations == "addition":
        c = (a * a) + (b * b)
        quiz_question = f"{a * a} + {b * b} = ?"

    if operation_mode == "subtraction" or mixed_operations == "subtraction":
        c = (a * a) - (b * b)
        quiz_question = f"{a * a} - {b * b} = ?"

    if operation_mode == "multiplication" or mixed_operations == "multiplication":
        c = (a * b)
        quiz_question = f"{a} * {b} = ?"

    if operation_mode == "division" or mixed_operations == "division":
        c = (a * b) / a
        quiz_question = f"{a * b} / {a} = ?"

    # FOR TESTING PURPOSES
    print(f"answer = {c}")

    # shows user the question
    print(quiz_question)

    # get user answer
    user_input = int_check("Solve: ", exit_code="xxx")

    # if user choice is the exit code, break the loop
    if user_input == "xxx":
        break

    result = ans_compare(user_input, c)

    # adjust question incorrect / question correct counters
    # and add results to quiz history

    if result == "correct":
        quiz_feedback = "You guessed it correct!"
    if result == "incorrect":
        incorrect_guesses += 1
        quiz_feedback = f"Wrong, the answer is {c}"

    # set up question result and output it to user
    # add it to the question history list (include the question number)
    question_result = f"User: {user_input} | Question: {quiz_question} \nAnswer: {c} | Result: {quiz_feedback}\n"
    history_item = f"Question: {questions_answered + 1} - {question_result}"

    print(question_result)
    quiz_history.append(history_item)

    questions_answered += 1

    # if users are in infinite mode, increase number of questions!
    if mode == "infinite":
        num_questions += 1

# quiz loops ends here

if questions_answered > 0:
    # quiz history / statistics area
    # calculate statistics
    correct_guesses = questions_answered - incorrect_guesses
    percent_correct = correct_guesses / questions_answered * 100
    percent_incorrect = incorrect_guesses / questions_answered * 100

    print("📈📈📈Game Statistics📈📈📈")
    print(f"Wrong Guesses: {percent_incorrect:.2f}% |\t"
          f"Correct Guesses: {percent_correct:.2f}%\t")

    # ask user if they want to see their quiz history and output it if requested.
    see_history = string_checker("\nDo you want to see your quiz history? ")
    if see_history == "yes":
        for item in quiz_history:
            print(f"\n{item}\n")
    print()
    print("Thanks for playing.")
else:
    # if user didn't answer any questions
    print("oops, you chickened out")
