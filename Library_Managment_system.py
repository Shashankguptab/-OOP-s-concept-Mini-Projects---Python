"""
Library Management System

Class: Book (title, author, ISBN, availability).

Class: Library to store a list of books, borrow and return methods.

Demonstrates composition and encapsulation
"""


class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        for book in self.books:
            status = "Available" if book.available else "not available"
            print(f"{book.title} by {book.author} ({status})")

    def borrow_books(self, isbn):
        for book in self.books:
            if book.isbn == isbn and book.available:
                book.available = False
                print(f"You borrowed {book.title}")
                return
        print("Book not available")

    def return_books(self, isbn):
        for book in self.books:
            if book.isbn == isbn and not book.available:
                book.available = True
                print(f"You returned {book.title}")
                return
        print("You have not returned the book ")


lib = Library()
book1 = Book("Python Basics", "Rajkumar", "101")
book2 = Book("Java Basics", "Ambresh", "102")

lib.add_book(book1)
lib.add_book(book2)

lib.display_books()
lib.borrow_books("101")
lib.return_books("101")
lib.borrow_books("102")
lib.display_books()
