from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import Optional
import json
import os
from data_factory import DataFactory


@dataclass
class DataFile(DataFactory):

    def _write_new_data(self, data: dict) -> None:
        with open(self.src_name, 'w') as json_file:
            json.dump(data, json_file)

    def __init__(self, *args):
        super(DataFile, self).__init__(*args)
        if not self.src_name.endswith('.json'):
            raise Exception('must be a json file')
        if not os.path.exists(self.src_name):
            self._write_new_data({})
        
    def _get_data_from_file_decorator(func) -> str:
        def wrapper(self, *args, **kwargs):
            try:
                with open(self.src_name, 'r') as json_file:
                    data = json.load(json_file)
                kwargs['data'] = data
            except FileNotFoundError:
                kwargs['data'] = {}
            return func(self, *args, **kwargs)
        return wrapper

    @_get_data_from_file_decorator
    def get(self, key: str, data=None) -> str:
        try:
            val = data[key]
            return f'Value: {val}'
        except KeyError:
            return f'Key `{key}` not found!'

    @_get_data_from_file_decorator
    def set(self, key: str, val: str, data=None) -> str:
        if data.get(key) is None:
            data[key] = val
            self._write_new_data(data)
            return 'Data was written!'
        return f'Key `{key}` already exists with val {data[key]}'

    @_get_data_from_file_decorator
    def delete(self, key: str, data=None) -> str:
        try:
            del data[key]
            self._write_new_data(data)
            return f'Key `{key}` was deleted!'
        except KeyError:
            return f'Key `{key}` not found!'