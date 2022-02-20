class credential:
    '''
    Class that generates new instances of credential
    '''

    credential_list = [] #empty list
    
    def __init__(self,user_name,email,password):
                
        self.user_name = user_name
        self.email = email
        self.password = password


    # def save_credential(self):
    #     '''
    #     save_user method saves user objects in user list
    #     '''

    #     credential.save_credential.append(self)   