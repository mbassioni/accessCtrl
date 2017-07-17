from functools import wraps; 
import logging; 

logging.basicConfig(filename="aaa.log", level=logging.DEBUG, mode='w'); 

def authentication(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        if self.is_authenticated:
            print "User is authenticated, let'em in" 
            return func(self, _authenticated=True, *args, **kwargs)
        else:
            print "User is not authenticated to access this resource" 
            #Log this event
            logging.debug("Unauthorized access detected, please take an action")
            '''
            #TODO: Redirect to 403 - Forbidden. 
            With the option to ask for permissions
            '''
            
            return func(self, _authenticated=False, *args, **kwargs)
    return wrapper


def authorization(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        if self.is_authenticated:
            print "User is authenticated, let'em in" 
            return func(self, _authorized=True, *args, **kwargs)
        else:
            print "User is not authorized to access this resource" 
            #Log this event
            logging.debug("Unauthorized access detected, please take an action")
            '''
                TODO: Redirect to 404 - Not found. 
            '''
            return func(self, _authorized=False, *args, **kwargs)
    return wrapper