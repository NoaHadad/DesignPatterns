
from data_factory import DataFactory
from data_file import DataFile
from db import DataBase


class DataInstance:

    OPTIONS = {'file': DataFile, 'db': DataBase}

    @staticmethod
    def get_instance(data_src: str, src_name: str) -> DataFactory:
        try:
            return DataInstance.OPTIONS[data_src](src_name)
        except KeyError:
            raise Exception('Data source does not exist. Select `file` or `db`.')


class Menu:

    def _select_data_src(self) -> None:
        flag_keep_trying = True
        while flag_keep_trying:
            data_src = input('Please select data source: ')
            src_name = input('Please select source name: ')
            try:
                self._data_instance = DataInstance.get_instance(data_src, src_name)
                flag_keep_trying = False
            except Exception as e:
                print(e)

    def operation_decorator(func):
        def wrapper(self, *args, **kwargs) -> None:
            key = input('\nPlease enter a key: ')
            print(func(self, key))
        return wrapper

    @operation_decorator
    def _get(self, key=None) -> str:
        return self._data_instance.get(key)

    @operation_decorator
    def _set(self, key=None) -> str:
        val = input('Please enter a value: ')
        return self._data_instance.set(key, val)

    @operation_decorator
    def _delete(self, key=None) -> str:
        return self._data_instance.delete(key)

    def _stop(self):
        self._run_flag = 0

    def _select_operation(self) -> None:
        operations = {'1': self._select_data_src, 
                      '2': self._get,
                      '3': self._set,
                      '4': self._delete,
                      '5': self._stop
                     }
        selected = input("\nPlease select operation: \n1)Change data src \n2)Get data \n3)Set data \n4)Delete data \n5)Stop \nYour selection: ")
        operations[selected]()

    def run(self) -> None:
        self._run_flag = 1
        self._select_data_src()
        while self._run_flag:
            self._select_operation()


if __name__=='__main__':

    Menu().run()
        

