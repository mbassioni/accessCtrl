from functools import wraps; 
import logging; 

logging.basicConfig(filename="aaa.log", level=logging.DEBUG, mode='w'); 

def authenticated(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        if self.is_authenticated:
            print "User is authenticated, let'em in" 
            return func(self, check_passed=True, *args, **kwargs)
        else:
            print "User is not authenticated to access this resource" 
            #Log this event
            logging.debug("Unauthorized access detected, please take an action")
            return func(self, check_passed=False, *args, **kwargs)
    return wrapper