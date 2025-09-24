#sys module provides access to system-specific parameters and functions
#os module provides functions to interact with the operating system
import sys
import os
import pytest

#__file__ is a built-in variable that stores the path to the current Python file
#os.path.dirname(__file__) gives the dir that contains the current file
#ex. if __file__ = '/home/student/cs4300/homework1/tests/test_task5.py' then os.path.dirname(__file__) = '/home/student/cs4300/homework1/tests'.
#os.path.join() combines folder paths in a safe way, regardless of operating system
sys.path.append(os.path.join(os.path.dirname(__file__),'../src'))

#so the path right now: /home/student/cs4300/homework1/src
#and can directly import task5

#note: have to do all of these because src/ and tests/ are siblings, and task5 and test_task5 are not in the same dir and cannot be imported directly
import task5


#function to check if book list has the correct structure with "title" and "author"
def test_book_list_structure():
	books = task5.book_list()
	assert isinstance(books, list)	#check if it is a list
	assert all(isinstance(book, dict) for book in  books)
	assert "title" in books[0]
	assert "author" in books [0]

#function to check if the first three books are correct
def test_first_three_books(capsys):
	books = task5.book_list()
	first_three = task5.first_three_books(books)

	#check if it is three books
	assert len(first_three) == 3

	#check if they have the correct titles
	expected_titles = ["Harry Potter", "The Lord of the Rings", "The Return of the Condor Heroes"]
	for i, book in enumerate(first_three):
		assert book["title"] == expected_titles[i]

#function to check if student database has the correct structure
def test_student_database_structure():
	students = task5.student_database()
	assert isinstance(students, dict)

	expected_students = {
	"Amy White": "S25001",
	"David Brown": "S25002",
	"Gavin Johnson": "S25003",
	"Trinity Wilson": "S25004"
	}

	#check if they have the correct student name and id
	for i, (name, student_id) in enumerate(expected_students.items(), 1):
		assert name in students
		assert students[name] == student_id
