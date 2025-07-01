# Write a function to check if a string is a palindrome (reads the same forward and backward).
# Then write pytest cases for inputs like "madam", "racecar", "hello", and "" (empty string).

import pytest

temp1 = str() #This is how empty strings are initiated.
temp2 = str()

def check_palindrome(string_value, temp1 = temp1, temp2 = temp2): #postitional argument and default positional arguments.
    for i, j in zip(string_value, string_value[::-1]): #zip can be used for every iterable for taking value one by one from both.
        temp1 += i       #This is how strings are appended letter by letter into a word.
        temp2 += j

    if not temp1:       #This is how empty strings are dealt.
        raise ValueError("Empty String is not Allowed.")
    elif temp1 == temp2:
        return True
    else:
        return False

def test_check_palindrome():
    assert check_palindrome(string_value="madam") == True
    assert check_palindrome(string_value="racecar") == True
    assert check_palindrome(string_value="hello") == False
    with pytest.raises(ValueError):
        check_palindrome(string_value="")