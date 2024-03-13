from library_management_system.models import LibraryDatabase


class Book:
    def __init__(self, isbn, title, author):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        return f"Book (title={self.title}, author={self.author}, isbn={self.isbn})"


class BookManagement(LibraryDatabase):
    def add_book(self, book):
        """
        This function adds a book to the inventory
        :param book: book object from the Book class to add to the inventory
        :return:
        """
        self.add_to_inventory(book)

    def list_books(self):
        """
        This function returns a list of the books in the inventory
        :return: list of books
        """
        self.list_inventory()

    def delete_book(self, isbn):
        """
        This function deletes a book from the inventory
        :param isbn:
        :return: list of books
        """
        self.delete_from_inventory(isbn)

    def update_book(self, book):
        """
        This function updates a book in the inventory
        :param book: book object from the Book class to update the inventory
        :return:
        """
        self.update_inventory(book)
