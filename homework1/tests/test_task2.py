#sys module provides access to system-specific parameters and functions
#os module provides functions to interact with the operating system
import sys
import os

#__file__ is a built-in variable that stores the path to the current Python file
#os.path.dirname(_file__) gives the dir that contains the current file
#ex. if __file__ = '/home/student/cs4300/homework1/tests/test_task2.py' then os.path.dirname(__file__) = '/home/student/cs4300/homework1/tests'.
#os.path.join() combines folder paths in a safe way, regardless of operating system
sys.path.append(os.path.join(os.path.dirname(__file__),'../src'))

#so the path right now: /home/student/cs4300/homework1/src
#and can directly import task2

#note: have to do all of these because src/ and tests/ are siblings, and task2 and test_task2 are not in the same dir and cannot be imported directly

import task2

#function for checking if the data is an int and if it is equal to the num it supposed to be
def test_integer_type():
	sum, product = task2.integer_type()

	assert isinstance(sum, int)
	assert isinstance(product, int)
	assert sum == 70
	assert product == 696

#function for checking if the data is a float and if it is equal to the num it supposed to be
def test_float_type():
	total, multiple = task2.float_type()

	assert isinstance(total, float)
	assert isinstance(multiple, float)
	assert total == 93.25
	assert multiple == 274.24

#function for checking if the data is a string and if it is the same as the string it supposed to be
def test_string_type():
	sentence = task2.string_type()

	assert isinstance(sentence, str)
	assert sentence == "Hello World and HW1"

#funtion for checking if the data is a boolean and if it is equal to the state it supposed to be
def test_boolean_type():
	and_result, or_result = task2.boolean_type()

	assert isinstance(and_result, bool)
	assert isinstance(or_result, bool)
	assert and_result == False
	assert or_result == True
