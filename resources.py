from acl import authenticated; 

class Resource(object):
    
    @property
    def id(self):
        return self._id_value; 
    @id.setter 
    def id(self, value=None):
        if isinstance(id, (int, long)):
            self._id_value = long(value); 
            
    @property
    def is_authenticated(self):
        return self._is_authenticated_value; 
    @is_authenticated.setter
    def is_authenticated(self, value=False):
        self._is_authenticated_value = value; 
        
    def __init__(self, id=None):
        self.is_authenticated = False; 
        if not isinstance(id, type(None)):
            self.id = long(id); 
            
    @authenticated
    def access(self, username=None, password=None, check_passed=False):
        print check_passed; 
        