import logging

from models import Models

logger = logging.getLogger(__name__)


class CheckinManager(Models):
    def ckeckout(self, checkout_details):
        """
        This function checks out a book based on availability
        :param checkout_details:
        :return:
        """
        try:
            information_found = self.search(storage_key='checkouts', search_keyword=checkout_details['isbn'])
            user_found = self.search(storage_key='users', search_keyword=checkout_details['user_id'])
            if not information_found or not user_found:
                raise ValueError(f"Specified isbn or userid is not available")
            if information_found and information_found['checked_out']:
                raise ValueError(f"Specified {checkout_details['isbn']} is already checkedout")
            checkout_details['checked_out'] = True
            self.update(storage_key='checkouts', update_data=checkout_details)
            print(f"Checked out {checkout_details['isbn']}")
            logger.info(f"User {checkout_details['user_id']} checked out book {checkout_details['isbn']}")
        except Exception as e:
            logger.error(e)
            print(e)

    def ckeckin(self, checkin_details):
        """
        This function checks out a book based on availability
        :param checkin_details:
        :return:
        """
        try:
            information_found = self.search(storage_key='checkouts', search_keyword=checkin_details['isbn'])
            if not information_found:
                raise ValueError(f"Specified {checkin_details['isbn']} is not available")
            if information_found and not information_found['checked_out']:
                raise ValueError(f"Specified {checkin_details['isbn']} is not checkedout")
            checkin_details['checked_out'] = False
            self.update(storage_key='checkouts', update_data=checkin_details)
            print(f"Checked in {checkin_details['isbn']}")
            logger.info(f"User {checkin_details['user_id']} checked in the book {checkin_details['isbn']}")
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
            information_found = self.search(storage_key='checkouts', search_keyword=isbn)
            if information_found and not information_found['checked_out']:
                print(f"book with {isbn} is available for checkout")
            else:
                raise ValueError(f"Book with {isbn} is not available")
        except Exception as e:
            logger.error(e)
            print(e)
