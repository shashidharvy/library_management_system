from models import LibraryDatabase


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
        self.add_user_info(user)

    def list_users(self):
        """
        This function list the users in the database
        :return: list of usernames
        """
        self.list_user_info()

    def update_user(self, user):
        """
        This function updates a user in the database by its userid
        :param user:
        :return:
        """
        return self.update_user_info(user)

    def delete_user(self, user_id):
        """
        This function deletes a user from the database by its userid
        :param user_id:
        :return:
        """
        self.delete_user_info(user_id)
