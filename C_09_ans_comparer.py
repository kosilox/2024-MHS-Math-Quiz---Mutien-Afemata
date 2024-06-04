# check that users have entered a valid
# option based on a list

def ans_compare(user, ans):
    # if the user and the answer is the same, it's a win
    if user == ans:
        quiz_result = "win"
    # if not the same, then it's a loss
    else:
        quiz_result = "lose"
    return quiz_result



# automated testing is below in the form (test_case, expected_value)
to_test = [

    ('7', '8', 'lose'),
    ('8', '8', 'win'),

]

# run tests!
for item in to_test:
    # retrieve text case and expected value
    user = item[0]
    comp = item[1]
    expected = item[2]

    # get actual value (ie: test ticket function)
    actual = ans_compare(user, comp)
    # compare actual and expected and output pass / fail
    if actual == expected:
        print(f"✔️ Passed! Case: {user}, expected: {comp}, received: {actual}")
    else:
        print(f"❌ Failed! Case: {user}, expected: {comp}, received: {actual}")