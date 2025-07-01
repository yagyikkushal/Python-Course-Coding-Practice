# Write a function that returns the factorial of a number.
# Then write pytest cases for inputs like 0, 1, 5, and -3 (handle invalid input).

import pytest

'''
Notes:

1️⃣ 'res = 1' is used because multiplying with '0' always gives '0'.
2️⃣ Setting a "default value" (like 'res=1') makes the argument "optional" when calling the function.
    If provided, it overrides the default.
 
'''

def factorial(n, res=0):
    if n == 0:
        return 1
    elif n < 0:
        raise ValueError("Negative numbers not allowed") # This is how we raise error.
    else:
        for _ in range(1,n+1):
            res *= _
    return res

def test_factorial():
    assert factorial(5) == 120
    assert factorial(0) == 1
    assert factorial(1) == 1

    with pytest.raises(ValueError): # This is how we handle error in pytest. Keep the syntax in mind if possible.
        factorial(-3)               # Assert and == is not required here. Keep the syntax in mind.