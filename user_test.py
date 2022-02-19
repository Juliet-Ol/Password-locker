import unittest #importing the unitest module
from user import user #importing user class

class Testuser(unittest.TestCase):

    '''
    Test class that defines test cases for the contact class behaviours.

    Args:
        unittest.TestCase: class that helps in creating test cases
    '''  

    def setUp(self):    
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = user("Juliet","Igotthis*") #create contact object

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.user_name,"Juliet")  
        self.assertEqual(self.new_user.password,"Igotthis*") 

if __name__ == '__main__':
    unittest.main()