class Booklist():
	def __init__(self):
		self.books =[]
		''' INITIALIZE THE BOOKS ATTRIBUTE'''
	

	def add(self, title, author):
		book = {}
		book['title'] = title
		book['author'] = author
		self.books.append(book)
		''' line 7 creating an empty dictionary 
		line 9- 11  assigning key/value pairs inside the dictionaries
		appending the boook dictionary to the attribute in line 4
		'''

	

	def count_books(self):
		return len(self.books)

		
	def remove_title(self, title):
		for book in self.books:
			if book['title'] == title:
				self.books.remove(book)

	def display_titles(self):
		title = []
		for book in self.books:
			title.append(book['title'])
		
	def display_ti	
		print(sorted(title))
