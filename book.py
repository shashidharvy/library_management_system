import logging

from models import Models

logger = logging.getLogger(__name__)


class Books(Models):
    def add_book(self, book):
        """
        This function adds a book to the inventory
        :param book: book object from the Book class to add to the inventory
        :return:
        """
        try:
            self.create(storage_key='books', input_data=book)
            checkout_details = {
                'isbn': book['isbn'],
                'user_id': None,
                'checked_out': False
            }
            self.create(storage_key='checkouts', input_data=checkout_details)
            logger.info(f"Added {book}")
            print(f"{book} Book Added")
        except Exception as e:
            logger.error(e)
            print(e)

    def list_books(self):
        """
        This function returns a list of the books in the inventory
        :return: list of books
        """
        try:
            self.list_data(storage_key='books')
        except Exception as e:
            print(e)

    def delete_book(self, isbn):
        """
        This function deletes a book from the inventory
        :param isbn:
        :return: list of books
        """
        try:
            self.delete(storage_key='books', delete_keyword=isbn)
            self.delete(storage_key='checkouts', delete_keyword=isbn)
            print(f"Removed book with {isbn}")
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
            self.update(storage_key='books', update_data=book)
            print(f"Updated {book}")
            logger.info(f"Updated {book}")
        except Exception as e:
            logger.error(e)
            print(e)
