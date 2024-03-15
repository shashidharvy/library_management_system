from storage import Storage


class Models:
    def __init__(self):
        # self.file_format = file_format
        self._storage = Storage()
        # if self.file_format.endswith('.json'):
        self._storage_manager = {
            'checkouts':
                self._storage.from_json('checkouts')
                if self._storage.from_json('checkouts')
                else [],
            'users':
                self._storage.from_json('users')
                if self._storage.from_json('users')
                else [],
            'books':
                self._storage.from_json('books')
                if self._storage.from_json('books')
                else []

        }
        self._validation_keys = ['isbn', 'user_id']

    def search(self, storage_key, search_keyword):
        """
        this function searches for specified search keyword in selected storage
        :param storage_key:
        :param search_keyword:
        :return: json information of searched keyword
        """
        if isinstance(search_keyword, list):
            search_keyword = search_keyword
        elif isinstance(search_keyword, dict):
            search_keyword = search_keyword.values()
        elif isinstance(search_keyword, str):
            search_keyword = [search_keyword]
        else:
            raise ValueError(f"Specified {search_keyword} is not available")
        storage_info = self._storage_manager[storage_key]
        for json in storage_info:
            for key, value in json.items():
                if value in search_keyword:
                    return json

    def update(self, storage_key, update_data):
        information_found = self.search(storage_key, update_data)
        if information_found:
            update_index = self._storage_manager[storage_key].index(information_found)
            self._storage_manager[storage_key][update_index] = update_data
            self._storage.to_json(self._storage_manager[storage_key], storage_key)
        else:
            raise ValueError(f"Specified {update_data} is not available")

    def create(self, storage_key, input_data):
        information_found = self.search(storage_key, input_data)
        if not information_found:
            self._storage_manager[storage_key].append(input_data)
            self._storage.to_json(self._storage_manager[storage_key], storage_key)
        elif information_found and self.validate(information_found, input_data):
            self._storage_manager[storage_key].append(input_data)
            self._storage.to_json(self._storage_manager[storage_key], storage_key)
        else:
            raise ValueError(f"Specified {input_data} already exists")

    def delete(self, storage_key, delete_keyword):
        information_found = self.search(storage_key, delete_keyword)
        if information_found:
            delete_index = self._storage_manager[storage_key].index(information_found)
            self._storage_manager[storage_key].pop(delete_index)
            self._storage.to_json(self._storage_manager[storage_key], storage_key)
        else:
            raise ValueError(f"Specified {delete_keyword} does not exist")

    def list_data(self, storage_key):
        print(self._storage_manager[storage_key])

    def validate(self, input_information, validation_information):
        for key in self._validation_keys:
            if not validation_information.get(key):
                continue
            elif input_information.get(key) != validation_information.get(key):
                return True
            break
