#function to count words in a file, first read a file then count words in it
def count_words_in_file(filename):
	try:
		#read the file
		with open(filename, "r", encoding="utf-8") as file:
			text = file.read()
			words = text.split()	#words are separated by column
			return len(words)	#how many words
	except FileNotFoundError:
		raise FileNotFoundError(f"File {filename} not found.")



if __name__=="__main__":
	filename = "../task6_read_me.txt"	#task6_read_me.txt is saved under homework1/

	word_count = count_words_in_file(filename)
	print(f"There are {word_count} words in the file 'task6_read_me.txt'.")
