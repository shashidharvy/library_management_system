from storage import Storage


class LibraryDatabase:
    def __init__(self):
        # self.file_format = file_format
        self._storage = Storage()
        # if self.file_format.endswith('.json'):
        self._checkout_info = self._storage.from_json('checkout_storage') \
            if self._storage.from_json('checkout_storage') \
            else {}
        self._user_info = self._storage.from_json('user_storage') \
            if self._storage.from_json('user_storage') \
            else {}
        self._inventory_info = self._storage.from_json('inventory_storage') \
            if self._storage.from_json('inventory_storage') \
            else {}

    def book_checkout(self, userid, isbn):
        """
        this function checkout the book for the given userid if it is available else raise the ValueError
        :param userid:
        :param isbn:
        :return:
        """
        print(self._checkout_info)
        availability_status = self._checkout_info.get(isbn)
        if not availability_status:
            raise ValueError(f"Specified {isbn} is not available")
        if availability_status and availability_status['checked_out']:
            raise ValueError(f"Specified {isbn} is already checkedout")
        self._checkout_info[isbn] = {
            'user_id': userid,
            'checked_out': True
        }
        self._storage.to_json(self._checkout_info, 'checkout_storage')
        print(f"Checked out {isbn}")

    def book_checkin(self, userid, isbn):
        """
        this function checkin the book for the given userid
        :param userid:
        :param isbn:
        :return:
        """
        availability_status = self._checkout_info.get(isbn)
        if availability_status and (not availability_status['checked_out'] or availability_status['user_id'] != userid):
            raise ValueError(f"Specified {isbn} is either not checkedout or provided userid is wrong")
        self._checkout_info[isbn] = {
            'user_id': None,
            'checked_out': False
        }
        self._storage.to_json(self._checkout_info, 'checkout_storage')
        print(f"Checked in {isbn}")

    def checkout_availability(self, isbn):
        """
        This function checks the availability of a book
        :param isbn:
        :return:
        """
        availability = self._checkout_info.get(isbn)
        if not availability:
            raise ValueError(f"Specified {isbn} is not available")
        print("available" if not availability['checked_out'] else "not available")

    def add_to_inventory(self, book):
        """
        This function adds a book to the inventory
        :param book: book object from the Book class to add to the inventory
        :return:
        """
        if self._inventory_info.get(book.isbn):
            raise ValueError(f"Book with isbn {book.isbn} already exists")
        self._inventory_info[book.isbn] = {"title": book.title, "author": book.author}
        self._storage.to_json(self._inventory_info, 'inventory_storage')
        self._checkout_info[book.isbn] = {'user_id': None, 'checked_out': False}
        self._storage.to_json(self._checkout_info, 'checkout_storage')
        print(f"Added {book}")

    def list_inventory(self):
        """
        This function returns a list of the books in the inventory
        :return: list of books
        """
        if self._inventory_info:
            print({isbn: book for isbn, book in self._inventory_info.items()})
        else:
            print("No books in inventory")

    def delete_from_inventory(self, isbn):
        """
        This function deletes a book from the inventory
        :return: list of books
        """
        if not self._inventory_info.get(isbn):
            raise ValueError(f"Book with isbn {isbn} does not exist")
        self._inventory_info.pop(isbn)
        self._storage.to_json(self._inventory_info, 'inventory_storage')
        print(f"Removed book with {isbn}")

    def update_inventory(self, book):
        """
        This function updates a book in the inventory
        :param book: book object from the Book class to update the inventory
        :return:
        """
        if not self._inventory_info.get(book.isbn):
            raise ValueError(f"Book with isbn {book.isbn} does not exist")
        self._inventory_info[book.isbn] = {"title": book.title, "author": book.author}
        self._storage.to_json(self._inventory_info, 'inventory_storage')
        print(f"Updated {book}")

    def add_user_info(self, user):
        """
        This function adds a user to the database.
        :param user: user object from User class to add to database
        :return:
        """
        if self._user_info.get(user.user_id):
            raise ValueError(f"User already exists for {user.user_id}")
        self._user_info[user.user_id] = user.username
        self._storage.to_json(self._user_info, 'user_storage')
        print(f'Added {user}')

    def list_user_info(self):
        """
        This function list the users in the database
        :return: list of usernames
        """
        if self._user_info:
            print({user_id: username for user_id, username in self._user_info.items()})
        else:
            print('No users in database')

    def update_user_info(self, user):
        """
        This function updates a user in the database by its userid
        :param user: user object from User class to add to database
        :return:
        """
        if not self._user_info.get(user.user_id):
            raise ValueError(f"User does not exists for {user.user_id}")
        self._user_info[user.user_id] = user.username
        self._storage.to_json(self._user_info, 'user_storage')
        print(f'Updated {user}')

    def delete_user_info(self, user_id):
        """
        this function deletes a user from the database by its userid
        :param user_id:
        :return:
        """
        if not self._user_info.get(user_id):
            raise ValueError(f"User does not exist for {user_id}")
        self._user_info.pop(user_id)
        self._storage.to_json(self._user_info, 'user_storage')
        print(f'Deleted {user_id}')
