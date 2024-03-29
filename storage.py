import json
import os
from pathlib import Path


class Storage:
    def __init__(self):
        self._storage_paths = {
            'users':
                {
                    'json_path': os.path.join(Path.cwd(), 'users.json'),
                    'csv_path': 'user_csv.csv',
                },
            'books':
                {
                    'json_path': os.path.join(Path.cwd(), 'books.json'),
                    'csv_path': 'inventory_csv.csv',
                },
            'checkouts':
                {
                    'json_path': os.path.join(Path.cwd(), 'checkouts.json'),
                    'csv_path': 'checkout_csv.csv',
                },
        }

    def to_json(self, json_obj, storage_key):
        with open(self._storage_paths[storage_key]['json_path'], 'w') as fp:
            json.dump(json_obj, fp)

    @staticmethod
    def to_csv():
        """ TODO
        for csv based storage
        """
        pass

    def from_json(self, storage_key):
        source_path = self._storage_paths[storage_key]['json_path']
        if os.path.exists(source_path):
            with open(self._storage_paths[storage_key]['json_path'], 'r') as fp:
                json_data = json.load(fp)
            return json_data

    @staticmethod
    def from_csv():
        """ TODO
        for csv based storage
        """
        pass
