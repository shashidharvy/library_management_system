from models import LibraryDatabase


class CheckinManagement(LibraryDatabase):
    def ckeck_out(self, checkin_details):
        """
        This function checks out a book based on availability
        :param checkin_details:
        :return:
        """
        user_id, isbn = checkin_details
        self.book_checkout(user_id, isbn)

    def ckeck_in(self, checkin_details):
        """
        This function checks the book back into the inventory
        :param checkin_details:
        :return:
        """
        user_id, isbn = checkin_details
        self.book_checkin(user_id, isbn)

    def check_availability(self, isbn):
        """
        This function checks the availability of a book
        :param isbn:
        :return:
        """
        return self.checkout_availability(isbn)


