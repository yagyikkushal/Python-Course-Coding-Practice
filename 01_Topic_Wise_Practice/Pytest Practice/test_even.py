# Write a function that checks if a number is even.
# Then write pytest cases for inputs like `2`, `3`, `0`, and `-6`.

def check_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

def test_even():
    assert check_even(2) == True
    assert check_even(3) == False
    assert check_even(0) == True
    assert check_even(-6) == True

'''

Notes: Zero is even and negative numbers can also be odd or even.

'''