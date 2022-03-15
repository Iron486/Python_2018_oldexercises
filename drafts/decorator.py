
from functools import wraps
def test_function(fun_parameter):
    @wraps(fun_parameter)
    def wrapper(*args,**kwargs):
        return fun_parameter(*args,**kwargs)
    return wrapper
@test_function
def decorator(parameter1):
    return parameter1
print(decorator('Qualcosa a caso'))   


        
