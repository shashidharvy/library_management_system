import logging

from book import Books
from check import CheckinManager
from user import Users

logging.basicConfig(
    filename='library_events.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(name)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)


class Inputs:
    def __init__(self):
        self._input_prompts = {
            1: {
                "title": "Enter title: ",
                "author": "Enter author: ",
                "isbn": "Enter ISBN: "
            },
            2: {
                "name": "Enter user name: ",
                "user_id": "Enter user ID: "
            },
            3: {
                "user_id": "Enter user ID: ",
                "isbn": "Enter ISBN of the book to checkout: "
            }
        }

        self.prompt_map = {
            1: {
                'job': 'ADD BOOK',
                'method': self.get_book,
                'action': Books().add_book
            },
            2: {
                'job': 'LIST BOOK',
                'method': Books().list_books,
                'action': None
            },
            3: {
                'job': 'UPDATE BOOK',
                'method': self.get_book,
                'action': Books().update_book
            },
            4: {
                'job': 'DELETE BOOK',
                'method': self.get_isbn,
                'action': Books().delete_book
            },
            5: {
                'job': 'ADD USER',
                'method': self.get_user,
                'action': Users().add_user
            },
            6: {
                'job': 'LIST USER',
                'method': Users().list_users,
                'action': None
            },
            7: {
                'job': 'UPDATE USER',
                'method': self.get_user,
                'action': Users().update_user
            },
            8: {
                'job': 'DELETE USER',
                'method': self.get_user_id,
                'action': Users().delete_user
            },
            9: {
                'job': 'CHECKOUT BOOK',
                'method': self.get_chckout_info,
                'action': CheckinManager().ckeckout
            },
            10: {
                'job': 'CHECKIN BOOK',
                'method': self.get_chckout_info,
                'action': CheckinManager().ckeckin
            },
            11: {
                'job': 'CHECKOUT AVAILABLE',
                'method': self.get_isbn,
                'action': CheckinManager().check_availability
            },
            12: {
                'job': 'EXIT',
                'method': None
            }
        }

    def get_book(self):
        while True:
            title = input(self._input_prompts[1]["title"])
            author = input(self._input_prompts[1]["author"])
            isbn = input(self._input_prompts[1]["isbn"])
            if len(title) == 0:
                print("Please pass valid title")
                continue
            if len(author) == 0:
                print("Please pass valid author")
                continue
            if len(isbn) != 13:
                print("Please pass valid ISBN of length 13")
                continue
            break

        return {'isbn': isbn, 'title': title, 'author': author}

    def get_user(self):
        while True:
            username = input(self._input_prompts[2]["name"])
            user_id = input(self._input_prompts[2]["user_id"])
            if len(username) == 0:
                print("Please pass valid username")
                continue
            if len(user_id) == 0:
                print("Please pass valid user ID")
                continue
            break
        return {'username': username, 'user_id': user_id}

    @staticmethod
    def get_user_id():
        while True:
            user_id = input("Enter user ID: ")
            if len(user_id) == 0:
                print("Please pass valid user ID")
                continue
            break
        return user_id

    @staticmethod
    def get_isbn():
        while True:
            isbn = input("Enter ISBN: ")
            if len(isbn) != 13:
                print("Please pass valid ISBN of length 13")
                continue
            break
        return isbn

    def get_chckout_info(self):
        while True:
            user_id = input(self._input_prompts[3]["user_id"])
            isbn = input(self._input_prompts[3]["isbn"])
            if len(user_id) == 0:
                print("Please pass valid user ID")
                continue
            if len(isbn) != 13:
                print("Please pass valid ISBN of length 13")
                continue
            break
        return {'user_id': user_id, 'isbn': isbn}

    def get_users_choice(self):
        print("\nLibrary Management System")
        for key, value in self.prompt_map.items():
            print(f"{key}. {value['job']}")

        while True:
            try:
                choice = int(input("Enter your choice: "))
            except ValueError:
                print("Please pass integer value in specified options.")
                continue
            if choice in self.prompt_map:
                return choice
            else:
                print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    while True:
        inputs = Inputs()
        user_input = inputs.get_users_choice()
        if inputs.prompt_map[user_input]['method'] is not None:
            input_details = inputs.prompt_map[user_input]['method']()
            if inputs.prompt_map[user_input]['action']:
                inputs.prompt_map[user_input]['action'](input_details)
        else:
            break
