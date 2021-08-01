# traceback - where the error is happening , stack traces - bottom of lines - main error

#IdexError: list index out of range
#KeyError: 'release' - use key incorrectly 
#AttributeError: 'list' object has no attribute 'intersection'
#NotImplementedError - user define error
#RuntimeError - base class error
#SyntaxError - wrong syntax 
#IndentationError - TabError --> do not mix match tab spaces
#NameError
#TypeError - unsupported operand type for +: 'int' and 'str'
#ValueError - int('20.5')
#ImportError - 
#DeprecationWarning 
#Docstring

def count_from_zero_to_n(n):
    if n < 0:
        raise ValueError('Input should be a non-negative integer')
    for x in range(0, n+1):
        print(x)
        
        
class MyCustomError(TypeError):
  def __init__(self, message, code):
    super().__init__(f'Error code {code}: {message}' )
    self.code = code
  
raise MyCustomError ('Ouch! an error happened.' ) 


# - define a UncountableError that takes in wrong_value as the only argument
# - the UncountableError should inherit ValueError
# - the UncountableError should indicate an error message like this:
#    'Invalid value for n, WRONG_VALUE. n must be greater than 0.'
#    where WRONG_VALUE should be replaced by the given value in the argument
# define your UncountableError here:

class UncountableError(ValueError):
  def __init__(self, wrong_value):
    super().__init__(f'Invalid value for n, {wrong_value}. n must be greater than 0.')


# do not change anything in the count_from_zero_to_n() function
# you may expect your UncountableError work in the following way
def count_from_zero_to_n(n):
    if n < 1:
        raise UncountableError(n)
    for x in range(0, n + 1):
        print(x)
        
        
# Ban and Dan problem for try except else and finally use
# note that if exception happens than else statement will not run, finally block will always run. 
# in the special case below, the answer for two inputs 4 and 'dan' is 16.0 and error, the reason is finally block will run regardless of except block returning value to the function, and the value returned from finally get prioritized and hence error happens in case two.

def power_of_two():
    user_input = input('Please enter a number: ')
    try:
        n = float(user_input)
    except ValueError:
        print('Your input was invalid. Using default value 0')
        return 0
    finally:
        n_square = n ** 2
        return n_square
        
def power_of_two():
    user_input = input('Please enter a number: ')
    try:
        n = float(user_input)
        n_square = n ** 2
        return n_square
    except ValueError:
        print('Your input was invalid. Using default value 0')
        return 0

print(power_of_two())

#simple test for git commit
# git commit -m  " this is a comment"
        
