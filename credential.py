from credential import user

class user:
    '''
    Class that generates new instances of user
    '''
    
    def __init__(self,user_name,email,password):
                
        self.user_name = user_name
        self.email = email
        self.password = password