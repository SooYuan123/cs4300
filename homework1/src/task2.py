#function for int operations
def integer_type():
	a = 58
	b = 12
	int_sum = a + b
	int_mul = a * b

	return int_sum, int_mul

#function for float operations
def float_type():
	c = 3.04
	d = 90.21
	float_sum = c + d
	float_mul = round(c * d, 2)

	return float_sum, float_mul

#function for string operations
def string_type():
	first = "Hello"
	second = "World"
	third = "and"
	fourth = "HW1"
	full_string = first + " " + second + " " + third + " " + fourth

	return full_string

#function for bool operations
def boolean_type():
	t = True
	f = False
	bool_and = t and f
	bool_or = t or f

	return bool_and, bool_or


if __name__=="__main__":
	print("\n Integer:")
	print(integer_type())
	print("\n Float:")
	print(float_type())
	print("\n String:")
	print(string_type())
	print("\n Boolean:")
	print(boolean_type())
