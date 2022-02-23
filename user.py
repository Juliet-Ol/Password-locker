class user:
    '''
    Class that generates new instances of user
    '''

    user_list = [] #empty list

    def __init__(self,user_name,password,email):
                
        self.user_name = user_name
        self.password = password
        self.email = email


    user_list = [] # empty list
    #Init method up here
    def save_user(self):
        '''
        save_user method saves user objects in user list
        '''

        user.user_list.append(self)
    

