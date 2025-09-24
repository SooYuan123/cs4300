#sys module provides access to system-specific parameters and functions
#os module provides functions to interact with the operating system
import sys
import os
import pytest
import numpy as np

#__file__ is a built-in variable that stores the path to the current Python file
#os.path.dirname(__file__) gives the dir that contains the current file
#ex. if __file__ = '/home/student/cs4300/homework1/tests/test_task7.py' then os.path.dirname(__file__) = '/home/student/cs4300/homework1/tests'.
#os.path.join() combines folder paths in a safe way, regardless of operating system
sys.path.append(os.path.join(os.path.dirname(__file__),'../src'))

#so the path right now: /home/student/cs4300/homework1/src
#and can directly import task7

#note: have to do all of these because src/ and tests/ are siblings, and task7 and test_task7 are not in the same dir and cannot be imported directly
import task7

def test_calculate_stats_integer():
	lab_data = [23, 50, 80, 37, 66]
	results = task7.calculate_stats(lab_data)

	# Test return type
	assert isinstance(results, dict)

	# Test all required keys are present
	assert 'mean' in results
	assert 'median' in results
	assert 'std_dev' in results

	# Test values are correct
	expected_mean = np.mean(lab_data)
	expected_median = np.median(lab_data)
	expected_std = np.std(lab_data)

	assert results['mean'] == expected_mean
	assert results['median'] == expected_median
	assert results['std_dev'] == expected_std

def test_calculate_stats_float():

	float_data = [23.5, 50.2, 80.7, 37.1, 66.9]
	results = task7.calculate_stats(float_data)

	expected_mean = np.mean(float_data)
	expected_median = np.median(float_data)
	expected_std = np.std(float_data)

	assert results['mean'] == pytest.approx(expected_mean)
	assert results['median'] == pytest.approx(expected_median)
	assert results['std_dev'] == pytest.approx(expected_std)


