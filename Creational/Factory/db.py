from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import Optional
import sqlite3
from data_factory import DataFactory


@dataclass
class DataBase(DataFactory):

    def __init__(self, *args):
        super(DataBase, self).__init__(*args)
        self.conn = sqlite3.connect(self.src_name) 
        self.c = self.conn.cursor()
        self.c.execute(
            '''
            CREATE TABLE IF NOT EXISTS keyvals
            ([key] TEXT PRIMARY KEY, [value] TEXT)
            '''
        )
        self.conn.commit()

    def get(self, key: str, data=None) -> str:
        data = self.c.execute(f'SELECT key, value FROM keyvals WHERE key = "{key}"'
        ).fetchone()
        if data:
            return f'Value: {data[1]}'
        return f'Key `{key}` not found!'

    def set(self, key: str, val: str) -> str:
        try:
            self.c.execute(f'INSERT INTO keyvals (key, value) VALUES ("{key}", "{val}")')
        except sqlite3.IntegrityError:
            return f'Key `{key}` already exists'
        self.conn.commit()
        return 'Data was written'

    def delete(self, key: str) -> str:
        self.c.execute(f'DELETE FROM keyvals WHERE key = "{key}"')
        self.conn.commit()
        return f'Key `{key}` is not in the db anymore'