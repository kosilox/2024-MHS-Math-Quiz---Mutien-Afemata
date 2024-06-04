# check that users have entered a valid
# option based on a list

# basic string checker for arithmetic mode / stats
def string_checker(user_response, valid_ans):
    while True:

        # Get user response and make sure it's lowercase
        user_response = user_response.lower()

        for item in valid_ans:
            # iterate through valid responses and return
            # full word if response is first letter of the item
            # or the full item
            if user_response == item[0] or item == user_response:
                return item

        return "invalid"

# automated testing is below in the form (test_case, expected_value)
to_test = [

    ('Addition', 'addition'),
    ('SUBTRACTION', 'subtraction'),
    ('division', 'division'),
    ('A', 'addition'),
    ('S', 'subtraction'),
    ('XXX', 'xxx'),
    ('M', 'multiplication'),
    ('random', 'invalid'),

]

# run tests!
for item in to_test:
    # retrieve text case and expected value
    case = item[0]
    expected = item[1]

    # get actual value (ie: test ticket function)
    actual = string_checker(case, ["addition", "subtraction", "multiplication", "division", "xxx"])

    # compare actual and expected and output pass / fail
    if actual == expected:
        print(f"✔️ Passed! Case: {case}, expected: {expected}, received: {actual}")
    else:
        print(f"❌ Failed! Case: {case}, expected: {expected}, received: {actual}")
