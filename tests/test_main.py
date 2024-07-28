"""
!Author: Ajay Shimpi, 27.07.2024, 22:00!
unittest example #1

NOTE:
1. make sure you have setup pytest environment correctly
2. make sure you have set interpretor for each module correctly
"""
from main import increment
from main import decrement

import main
import unittest

class TestIncreDecrement(unittest.TestCase):

    # instead of writing variable repeatatively in functions which have same init value
    # use setUp(self) method to use it
    # so that we can replace values at one place and use it over the class
    def setUp(self):
        self.x=10
    
    def test_increment(self):
        assert increment(self.x) == 11
    
    def test_decremet(self):
        #x=5
        assert decrement(self.x) == 9


"""
this is example of unittest with python cide
using class
unittest library
self, assert etc functionaliity
"""
# comment1: test class Test_TestIncrementDecrement is defined, inheriting from unittest.TestCase
# Inheriting from unittest.TestCase allows the class to use various testing methods provided by the unittest module
class Test_TestIncrementDecrement(unittest.TestCase):
    # comment2: checks if main.increment(3) returns 4. If it does, the test passes; otherwise, it fails
    def test_increment(self):
        self.assertEqual(main.increment(3), 4)

    # comment3: checks if main.decrement(3) does not return 4. 
    # If it returns any value other than 4, the test passes; otherwise, it fails
    def test_decrement(self):
        self.assertNotEqual(main.decrement(3),4)

    """
    #negative TC, which will failed because Hello from this TC will not match with actual string
    def test_firstFunctionEqual(self):
        self.assertEqual(main.firstFunction(), "Hello")
    """
    # comment4: checks if main.firstFunction() returns False. If it does, the test passes; otherwise, it fails. 
    # The string "Hello" is an optional message that will be displayed if the test fails.
    def test_firstFunctionFalse(self):
        self.assertFalse(main.firstFunction(), "Hello")
        

    def test_incrementTest(self):
        self.assertEqual(increment(5),6)

# comment5: unittest.main() discovers and runs all the test methods in the file
if __name__ == "__main__":
    unittest.main()