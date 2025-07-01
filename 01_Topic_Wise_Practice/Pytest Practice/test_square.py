# Write a function that returns the square of a number.
# Then write a pytest to check if it works correctly for inputs like `2`, `3`, and `-4`.

def square_of_number(number):
    return number*number

def test_square_of_number():
    assert square_of_number(2)==4
    assert square_of_number(3)==9
    assert square_of_number(-4)==16

'''
Notes: 

1) Give descriptive name of functions recommended by ChatGPT.
2) Always save .py file name with "test_". As "_" is also important along with test.
3) Best practice is to save the file name of python file using "_" don't give spaces 
   between two words as it can cause error in importing, command line execution, and 
   automation tools.
   
'''