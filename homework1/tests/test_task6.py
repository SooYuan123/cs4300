#sys module provides access to system-specific parameters and functions
#os module provides functions to interact with the operating system
import sys
import os
import pytest

#__file__ is a built-in variable that stores the path to the current Python file
#os.path.dirname(__file__) gives the dir that contains the current file
#ex. if __file__ = '/home/student/cs4300/homework1/tests/test_task6.py' then os.path.dirname(__file__) = '/home/student/cs4300/homework1/tests'.
#os.path.join() combines folder paths in a safe way, regardless of operating system
sys.path.append(os.path.join(os.path.dirname(__file__),'../src'))

#so the path right now: /home/student/cs4300/homework1/src
#and can directly import task6

#note: have to do all of these because src/ and tests/ are siblings, and task6 and test_task6 are not in the same dir and cannot be imported directly
import task6

#function to test if word count is correct
def test_word_count():
	filename = "../task6_read_me.txt"
	assert task6.count_words_in_file(filename) == 104

#function to check for invalid files
def test_file_not_found():
	with pytest.raises(FileNotFoundError):
		task6.count_words_in_file("invalid_file.txt")

#parametrized test
@pytest.mark.parametrize("content, expected_word_count", [
	("", 0),			#empty
	("Hello", 1),
	("Hello World", 2),
	("Hello     World", 2),		#multiple spaces
	("Hello\nWorld", 2),		#newline
	("Hello, World!", 2),		#With punctuation
	("  Hello  World  ", 2),	#leading/trailing spaces
	("Tab\tseparated\twords", 3),	#tab
	("One    two    three", 3), 	#multiple spaces between words
])

#function to check the parametrized test
def test_word_count_various_inpus(tmp_path, content, expected_word_count):
	#create a temporary file with the context
	test_file = tmp_path / "temp.txt"
	test_file.write_text(content)

	assert task6.count_words_in_file(test_file) == expected_word_count
