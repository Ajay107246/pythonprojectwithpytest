"""
!Author: Ajay Shimpi, 27.07.2024, 22:00!
unittest example #1

NOTE:
1. make sure you have setup pytest environment correctly
2. make sure you have set interpretor for each module correctly
3. run on terminal with debug logs
py -m pytest -s
"""
from main import increment
from main import decrement
from main import len_url

import main
import unittest
from unittest.mock import patch



"""
this is example of unittest with python code
using class
unittest library
self, assert etc functionaliity
"""
class TestIncreDecrement(unittest.TestCase):

    # instead of writing variable repeatatively in functions which have same init value
    # use setUp(self) method to use it
    # so that we can replace values at one place and use it over the class
    def setUp(self):
        print("\nSETUP called...!")
        self.x=10

    def tearDown(self):
        #return super().tearDown()
        print("TEAR-DOWN called...!")
        
    def test_increment(self):
        print("test_increment called...!")
        assert increment(self.x) == 11
    
    def test_decremet(self):
        print("test_decrement called...!")
        #x=5
        assert decrement(self.x) == 9
    
    # use patch and its decorator to patch the len_url function
    # patch function takes arg as string, path to object to mock
    # here, it is get_url
    # decorator patch creates a special fake object - magicMock(), 
    # passes the reference to it into decorated function i.e. to definition below
    @patch('main.get_url')
    def test_len_url_google(self, mock_get_url):
        # get_url return a string and further len_url use it to calculate its length
        print("\ntest_len_url_google(self, mock_get_url) called...!")
        mock_get_url.return_value = 'return'
        self.assertEqual(len_url(), 6)



# comment1: test class Test_TestIncrementDecrement is defined, inheriting from unittest.TestCase
# Inheriting from unittest.TestCase allows the class to use various testing methods provided by the unittest module
class Test_TestIncrementDecrement(unittest.TestCase):
    # comment2: checks if main.increment(3) returns 4. If it does, the test passes; otherwise, it fails
    def test_increment(self):
        print("\nmain.increment(3) called...!")
        self.assertEqual(main.increment(3), 4)

    # comment3: checks if main.decrement(3) does not return 4. 
    # If it returns any value other than 4, the test passes; otherwise, it fails
    def test_decrement(self):
        print("\nmain.decrement(3) called...!")
        self.assertNotEqual(main.decrement(3),4)

    """
    #negative TC, which will failed because Hello from this TC will not match with actual string
    def test_firstFunctionEqual(self):
        self.assertNotEqual(main.firstFunction(), "Hello")
    """
    # comment4: checks if main.firstFunction() returns False. If it does, the test passes; otherwise, it fails. 
    # The string "Hello" is an optional message that will be displayed if the test fails.
    def test_firstFunctionFalse(self):
        print("\ntest_firstFunctionFals() called...!")
        self.assertFalse(main.firstFunction(), "Hello")
    
    """def test_firstFunctionTrue(self):
        self.assertEqual(main.firstFunction(), "Hello, This is my first python program in VS code!")
    """

# comment5: unittest.main() discovers and runs all the test methods in the file
if __name__ == "__main__":
    unittest.main()