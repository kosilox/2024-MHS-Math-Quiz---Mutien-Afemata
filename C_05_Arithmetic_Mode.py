
# checks what arithmetic mode
# user wants to solve
# gives the arithmetic modes they want to do
modes = [

("addition"),
("subtraction"),
("multiplication"),
("division"),

]

def arithmetic_mode(question, modes, exit_code=None):
    print(modes)
    error = (f"Please choose a mode of question from this list: \n{modes}\n")

    while True:
        response = input(question).lower()
        if response == exit_code:
            return response

        # iterate through valid responses and return
        # full word if response is first letter/s of item
        # or the full item
        for item in modes:
            if response == item[:0] or response == item:
                return item
        # if response is not in the list, output an error
        # and ask question again (because the code loops).
        print(error)

question_mode = arithmetic_mode("\nChoose the mode of question you solve: ",
                                modes = [("addition"),("subtraction"),
                                         ("multiplication"),("division")],
                                exit_code="xxx")