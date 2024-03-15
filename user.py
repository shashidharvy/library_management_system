import logging

from models import Models

logger = logging.getLogger(__name__)


class Users(Models):
    def add_user(self, user):
        """
        This function adds a user to the database.
        :param user: user object from User class to add to database
        :return:
        """
        try:
            self.create(storage_key='users', input_data=user)
            logger.info(f"{user} added to database")
            print(f"{user} added")
        except Exception as e:
            logger.error(e)
            print(e)

    def list_users(self):
        """
        This function list the users in the database
        :return: list of usernames
        """
        try:
            self.list_data(storage_key='users')
        except Exception as e:
            logger.error(e)
            print(e)

    def update_user(self, user):
        """
        This function updates a user in the database by its userid
        :param user:
        :return:
        """
        try:
            self.update(storage_key='users', update_data=user)
            logger.info(f"updated {user}")
            print(f"updated {user}")
        except Exception as e:
            print(e)

    def delete_user(self, user_id):
        """
        This function deletes a user from the database by its userid
        :param user_id:
        :return:
        """
        try:
            self.delete(storage_key='users', delete_keyword=user_id)
            logger.info(f"deleted {user_id}")
            print(f"deleted {user_id}")
        except Exception as e:
            logger.error(e)
            print(e)
