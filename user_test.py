
import pyperclip #importing pyperclip
from user import user # importing user class
from credential import user # import credential class
  

def test_copy_name(self):  
    '''
    Test to confirm that we are copying the name from a found user
    ''' 
    self.new_user.save_user()
    user.copy_name("Juliet")
    user.copy_password("Igotthis1*")

    self.assertEqual(self.new_user.name,pyperclip.paste()) 





import unittest #importing the unitest module
from user import user #importing user class

class Testuser(unittest.TestCase):

    # '''
    # Test class that defines test cases for the user class behaviours.

    # Args:
    #     unittest.TestCase: class that helps in creating test cases
    # '''  

    # def setUp(self):    
    #     '''
    #     Set up method to run before each test cases.
    #     '''
    #     self.new_user = user("Juliet","Igotthis*") #create contact object

    # def test_init(self):
    #     '''
    #     test_init test case to test if the object is initialized properly
    #     '''

    #     self.assertEqual(self.new_user.user_name,"Juliet")  
    #     self.assertEqual(self.new_user.password,"Igotthis1*")
    #     self.assertEqual(self.new_user.email,"juliet@gmail.com") 

    def test_save_user(self):
        '''
        test_save_user test case test if the user object is saved
        ''' 
        self.new_user.save_user()
        self.assertEqual(len(user.user_list),1)  

if __name__ == '__main__':
    unittest.main()