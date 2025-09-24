#sys module provides access to system-specific parameters and functions
#os module provides functions to interact with the operating system
import sys
import os

#__file__ is a built-in variable that stores the path to the current Python file
#os.path.dirname(_file__) gives the dir that contains the current file
#ex. if __file__ = '/home/student/cs4300/homework1/tests/test_task3.py' then os.path.dirname(__file__) = '/home/student/cs4300/homework1/tests'.
#os.path.join() combines folder paths in a safe way, regardless of operating system
sys.path.append(os.path.join(os.path.dirname(__file__),'../src'))

#so the path right now: /home/student/cs4300/homework1/src
#and can directly import task3

#note: have to do all of these because src/ and tests/ are siblings, and task3 and test_task3 are not in the same dir and cannot be imported directly
import task3


#these 3 functions are for checking sign of different numbers (positive, negative, and zero)
def test_check_sign_positive():
	assert task3.check_sign(0.001) == "positive"
	assert task3.check_sign(3.14) == "positive"
	assert task3.check_sign(23) == "positive"

def test_check_sign_negative():
	assert task3.check_sign(-8.92) == "negative"
	assert task3.check_sign(-7) == "negative"

def test_check_sign_zero():
	assert task3.check_sign(0) == "zero"



#function to test if it is a prime number
def test_is_prime():

	#some known prime numbers
	assert task3.is_prime(2) == True
	assert task3.is_prime(3) == True
	assert task3.is_prime(5) == True
	assert task3.is_prime(7) == True

	#some known composite numbers
	assert task3.is_prime(4) == False
	assert task3.is_prime(6) == False
	assert task3.is_prime(8) == False
	assert task3.is_prime(9) == False

	#some edge cases
	assert task3.is_prime(0) == False
	assert task3.is_prime(1) == False
	assert task3.is_prime(-5) == False

#function to check if the first 10 primes are the correct primes
def test_first_ten_prime_output(capsys):
	task3.first_ten_prime()

	#capture or grab the printed text
	captured = capsys.readouterr()
	output = captured.out

	#check if it has 10 lines of outputs
	lines = output.strip().split('\n')
	assert len(lines) == 10

	#convert output to integers
	primes = [int(line.strip()) for line in lines]

	#verify the first 10 primes
	correct_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
	assert primes == correct_primes

#function to check the sum from 1 to 100
def test_sum_1_to_100():
	assert task3.sum_1_to_100() == 5050
