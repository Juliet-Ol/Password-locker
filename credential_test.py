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

if __name__ == '__main__':
    unittest.main()         