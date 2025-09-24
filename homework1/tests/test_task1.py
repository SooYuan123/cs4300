#sys module provides access to system-specific parameters and functions
#os module provides functions to interact with the operating system
import sys
import os

#__file__ is a built-in variable that stores the path to the current Python file
#os.path.dirname(_file__) gives the dir that contains the current file
#ex. if __file__ = '/home/student/cs4300/homework1/tests/test_task1.py' then os.path.dirname(__file__) = '/home/student/cs4300/homework1/tests'.
#os.path.join() combines folder paths in a safe way, regardless of operating system
sys.path.append(os.path.join(os.path.dirname(__file__),'../src'))

#so the path right now: /home/student/cs4300/homework1/src
#and can directly import task1

#note: have to do all of these because src/ and tests/ are siblings, and task1 and test_task1 are not in the same dir and cannot be imported directly

import task1

#function to return a string
def test_hello_world():
	assert task1.hello_world() == "Hello, World!"
