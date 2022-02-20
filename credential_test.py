import pyperclip #importing pyperclip

def test_copy_name(self):  
    '''
    Test to confirm that we are copying the name from a found credential
    ''' 
    self.new_credential.save_credential()
    credential.copy_name("Juliet")
    credential.copy_password("Ihavethis*")

    self.assertEqual(self.new_user.name,pyperclip.paste())   




import unittest #importing the unitest module
from credential import credential # import credential class


class Testcredential(unittest.TestCase):

    '''
    Test class that defines test cases for the credential class behaviours.

    Args:
        unittest.TestCase: class that helps in creating test cases
    '''  

    def setUp(self):    
        '''
        Set up method to run before each test cases.
        '''
        self.new_credential = credential("Juliet","juliet@gmail.com","Ihavethis*") #create credential object

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credential.user_name,"Juliet")  
        self.assertEqual(self.new_credential.password,"Ihavethis*")
        self.assertEqual(self.new_credential.email,"juliet@gmail.com") 

    def test_save_credential(self):
        '''
        test_save_credential test case test if the credential object is saved
        ''' 
        self.new_user.save_user()
        self.assertEqual(len(credential.credential_list),1)  

    def test_delete_credential(self):
        '''
        test_delete_user to test if credential can be deleted
        '''
        self.new_user.delete_user()#Deleting a user
        self.assertEqual(len(credential.credential_list),1)


    def test_save_multiple_credential(self):
            '''
            test_save_multiple_credential to check if we can save multiple credentials
            objects to our credential_list
            '''
            self.new_credential.save_credential()
            test_credential = credential("Test","user","metoo1","test@user.com") # new contact
            test_credential.save_credential()
            self.assertEqual(len(credential.credential_list),2)


    @classmethod
    def find_by_email(cls,email):
        '''
        Method that takes in an email and returns a credential matching that user.

        Args:
            email: email to search for
        Returns :
            user of person matching the email.
        '''

        for credential in cls.credential_list:
            if credential.email == email:
                return credential     

if __name__ == '__main__':
    unittest.main()         