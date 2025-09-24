#function to create a dictionary of book list
def book_list():
	books = [
		{"title": "Harry Potter", "author": "J.K. Rowling"},
		{"title": "The Lord of the Rings", "author": "J.R.R. Tolkein"},
		{"title": "The Return of the Condor Heroes", "author": "Jin Yong"},
		{"title": "Pride and Prejudice", "author": "Jane Austen"},
		{"title": "Romance of the Three Kingdoms", "author": "Luo Guanzhong"},
	]
	return books

#function to find and print the first three books in the list
def first_three_books(booklist):
	three_books = booklist[:3]
	print("First three books:")
	for i, book in enumerate(three_books, 1):
		print(f"{i}. '{book['title']}' by {book['author']}")
	return three_books

#function to create a student database dictionary
def student_database():
	students = {
		"Amy White": "S25001",
		"David Brown": "S25002",
		"Gavin Johnson": "S25003",
		"Trinity Wilson": "S25004"
	}
	return students

#function to print out the student database
def print_student_database(data):
	print("Student Database:")
	for name, student_id in data.items():
		print(f"  {name}: {student_id}")
	return data


if __name__=="__main__":
	#displaying booklist
	booklist = book_list()
	first_three_books(booklist)

	print("\n")

	#displaying student database
	students_data = student_database()
	print_student_database(students_data)
