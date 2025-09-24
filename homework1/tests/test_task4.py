#sys module provides access to system-specific parameters and functions
#os module provides functions to interact with the operating system
#use pytest to do parameterized tests
import sys
import os
import pytest

#__file__ is a built-in variable that stores the path to the current Python file
#os.path.dirname(__file__) gives the dir that contains the current file
#ex. if __file__ = '/home/student/cs4300/homework1/tests/test_task4.py' then os.path.dirname(__file__) = '/home/student/cs4300/homework1/tests'.
#os.path.join() combines folder paths in a safe way, regardless of operating system
sys.path.append(os.path.join(os.path.dirname(__file__),'../src'))

#so the path right now: /home/student/cs4300/homework1/src
#and can directly import task4

#note: have to do all of these because src/ and tests/ are siblings, and task4 and test_task4 are not in the same dir and cannot be imported directly
import task4

@pytest.mark.parametrize("price, discount, expected", [

	#testing integer inputs with some discount, free, and no discount
	(150, 50, 75),
	(46, 12, 40.48),
	(70, 100, 0),
	(30, 0, 30),

	#testing float inputs with some discount, free, and no discount
	(150.0, 33.33, 100.00),
	(100, 12.12, 87.88),
	(20.25, 100, 0),
	(78.78, 0, 78.78),

	#testing with string inputs
	(100, "10", 90),
	("100", 10, 90),
	("100", "10", 90),
])


#function to check if the final price is calculated correctly
def test_calculate_discount(price, discount, expected):
	result = task4.calculate_discount(price, discount)
	assert result == expected
	
