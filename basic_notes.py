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
