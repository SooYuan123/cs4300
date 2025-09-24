#function for calculating prices after discount
def calculate_discount(price, discount):
	try:
		price_float = float(price)	#converting numbers to floats so it works for both int and float)
		discount_float = float(discount)
	except (TypeError, ValueError):
		raise TypeError("Price and discount must be numeric values.")

	#price can be float but cannot be negative
	if price_float < 0:
		raise ValueError("Price cannot be negative.")

	#discount cannot be negative as well
	if discount_float < 0:
		raise ValueError("Discount cannot be negative.")

	#calculate the amount of discount first then the final price after discount
	final_discount_amt = (discount_float / 100) * price_float
	final_price = price_float - final_discount_amt

	#return final price with 2 decimals only
	return round(final_price, 2)


if __name__=="__main__":
	try:
		price = input("Enter the price: ")
		discount = input("Enter the percentage of the discount: ")
		total = calculate_discount(price, discount)
		print(f"Your total after discount: {total}")
	except ValueError:
		print("Invalid input.")
