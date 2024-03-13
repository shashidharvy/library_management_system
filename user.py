import logging

from models import LibraryDatabase

logger = logging.getLogger(__name__)


class User:
    def __init__(self, username, user_id):
        self.username = username
        self.user_id = user_id

    def __str__(self):
        return f"User (username={self.username}, user_id={self.user_id})"


class UserManagement(LibraryDatabase):
    def add_user(self, user):
        """
        This function adds a user to the database.
        :param user: user object from User class to add to database
        :return:
        """
        try:
            self.add_user_info(user)
            logger.info(f"{user} added to database")
        except Exception as e:
            logger.error(e)
            print(e)

    def list_users(self):
        """
        This function list the users in the database
        :return: list of usernames
        """
        try:
            self.list_user_info()
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
            self.update_user_info(user)
            logger.info(f"updated {user}")
        except Exception as e:
            print(e)

    def delete_user(self, user_id):
        """
        This function deletes a user from the database by its userid
        :param user_id:
        :return:
        """
        try:
            self.delete_user_info(user_id)
            logger.info(f"deleted {user_id}")
        except Exception as e:
            logger.error(e)
            print(e)
