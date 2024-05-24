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

To begin, choose the type of mathematical questions and 
you'll get a choice to customise default game parameters 
(where we give you 10 questions to solve relating to the choice
you made), or you pick the questions after each is solved.

Your goal is to try to guess as many correct as possible,
this is to test your math knowledge!

Good luck.


    ''')
print("Welcome to the MHS Math Quiz!")
print()

while True:
    want_instructions = yes_no("Do you want to read the instructions?")


    # checks if users enter yes or no
    if want_instructions == "yes":
        instructions()
        pass
    else:
        print("program continues")


