#function to check sign of a number
def check_sign(num):
	if num > 0:
		return "positive"
	elif num < 0:
		return "negative"
	else:
		return "zero"

#function to check if a number is a prime number
def is_prime(n):
	if n <= 1:
		return False

	for i in range(2, n):
		if n % i == 0:
			return False
	return True

#function to find the first 10 prime numbers
def first_ten_prime():
	count = 0	#to store the counts
	number = 2	#to store the number to be checked for prime 

	while count < 10:
		if is_prime(number):
			print(number)
			count += 1
		number += 1

#function to sum 1 to 100
def sum_1_to_100():
	current_num = 1	#the current number
	sum = 0		#the current total

	while current_num <= 100:
		sum += current_num
		current_num += 1

	return sum

if __name__=="__main__":
	num_x = 0

	print("Check Sign:")
	print({num_x}," is ",check_sign(num_x))
	print("\nFirst 10 prime numbers:")
	first_ten_prime()
	print("\nSum from 1 to 100:")
	print(sum_1_to_100())
