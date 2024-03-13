import logging

from models import LibraryDatabase

logger = logging.getLogger(__name__)


class CheckinManagement(LibraryDatabase):
    def ckeck_out(self, checkin_details):
        """
        This function checks out a book based on availability
        :param checkin_details:
        :return:
        """
        user_id, isbn = checkin_details
        try:
            self.book_checkout(user_id, isbn)
            logger.info(f"User {user_id} checked out book {isbn}")
        except Exception as e:
            logger.error(e)
            print(e)

    def ckeck_in(self, checkin_details):
        """
        This function checks the book back into the inventory
        :param checkin_details:
        :return:
        """
        user_id, isbn = checkin_details
        try:
            self.book_checkin(user_id, isbn)
            logger.info(f"User {user_id} checked in book {isbn}")
        except Exception as e:
            logger.error(e)
            print(e)

    def check_availability(self, isbn):
        """
        This function checks the availability of a book
        :param isbn:
        :return:
        """
        try:
            return self.checkout_availability(isbn)
        except Exception as e:
            logger.error(e)
            print(e)
