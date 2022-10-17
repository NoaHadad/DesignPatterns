from dataclasses import dataclass, field
import os
import time
from abc import ABC, abstractmethod

@dataclass
class Command(ABC):

    @abstractmethod
    def execute(self) -> None:
        """executes the command"""
        pass

    @abstractmethod
    def undo(self) -> None:
        """undo the command"""
        pass


@dataclass
class ChangeFileNameCommand(Command):
    """Class for creating change file name command"""
    _from_file: str
    _to_file: str

    def execute(self) -> None:
        os.rename(self._from_file, self._to_file)

    def undo(self) -> None:
        os.rename(self._to_file, self._from_file)

    
@dataclass
class History:
    """Class for executing the incoming commands"""
    _logs: list = field(init=False, default_factory=(lambda: []))

    def execute(self, command: ChangeFileNameCommand) -> None:
        self._logs.append(command)
        command.execute()

    def undo(self) -> None:
        command = self._logs.pop()
        command.undo()


if __name__=="__main__":
    history = History()

    print('craeting x.json')
    open('x.json', 'a').close()
    time.sleep(5)

    print('command1 - changing to y.json')
    command = ChangeFileNameCommand('x.json', 'y.json')
    history.execute(command)
    time.sleep(5)

    print('command2 - returnning to x.json')
    history.undo()
    time.sleep(5)

    print('removing file')
    os.remove('x.json')
