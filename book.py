import logging

from models import LibraryDatabase

logger = logging.getLogger(__name__)


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
        try:
            self.add_to_inventory(book)
            logger.info(f"Added {book}")
        except Exception as e:
            logger.error(e)
            print(e)

    def list_books(self):
        """
        This function returns a list of the books in the inventory
        :return: list of books
        """
        try:
            self.list_inventory()
        except Exception as e:
            print(e)

    def delete_book(self, isbn):
        """
        This function deletes a book from the inventory
        :param isbn:
        :return: list of books
        """
        try:
            self.delete_from_inventory(isbn)
            logger.info(f"Removed book with {isbn}")
        except Exception as e:
            logger.error(e)
            print(e)

    def update_book(self, book):
        """
        This function updates a book in the inventory
        :param book: book object from the Book class to update the inventory
        :return:
        """
        try:
            self.update_inventory(book)
            logger.info(f"Updated {book}")
        except Exception as e:
            logger.error(e)
            print(e)
