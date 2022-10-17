from __future__ import annotations
from dataclasses import dataclass
from typing import  ClassVar, Optional
from threading import Lock, Thread
from time import sleep


@dataclass(init=False)
class Singleton:
    __instance: ClassVar[Optional[Singleton]]=None
    __lock: ClassVar[Lock]=Lock()
    __init_flag: ClassVar[bool]=False
    _num: int 

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            with cls.__lock as lock:
                if cls.__instance is None:
                    cls.__instance = super(Singleton, cls).__new__(cls)
        return cls.__instance

    def __init__(self, num: int):
        if self.__init_flag is False:
            with self.__lock as lock:
                if self.__init_flag is False:
                    self._num = num
                    self.__init_flag = True
        else:
            print('has been already initialized')


def create_singleton(num: int) -> None:
    Singleton(num)
    

if __name__=="__main__":
    threads = [Thread(target=create_singleton, args=(num,)) for num in range(100)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
