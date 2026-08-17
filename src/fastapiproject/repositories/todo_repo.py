from abc import ABC, abstractmethod

from fastapiproject.models.todo import Todo

class TodoRepo(ABC):

    @abstractmethod
    def add(self, todo: Todo) -> Todo:
        pass

    @abstractmethod
    def find_by_id(self, todo_id: int) -> Todo:
        pass

    @abstractmethod
    def find_all(self) -> list[Todo]:
        pass

    @abstractmethod
    def update(self, todo: Todo) -> Todo:
        pass

    @abstractmethod
    def delete(self, todo_id: int) -> None:
        pass