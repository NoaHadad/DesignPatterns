from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import Optional
import json


@dataclass
class DataFactory(ABC):

    src_name: str

    @abstractmethod
    def get(self, key: str, *args, **kwargs) -> str:
        """return corresponding value from the db or key doesn't exist"""
        pass

    @abstractmethod
    def set(self, key: str, value: str, *args, **kwargs) -> str:
        """setting data to the db if key is not already exist.
           otherwise, returns key already exist"""
        pass

    @abstractmethod
    def delete(self, key: str, *args, **kwargs) -> str:
        """deleting key and corresponding val"""
        pass