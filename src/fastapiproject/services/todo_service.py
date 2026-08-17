from fastapiproject.models.todo import Todo
from fastapiproject.repositories.todo_repo import TodoRepo

class TodoNotFoundError:
    pass

class TodoService:

    def __init__(self, repo: TodoRepo):
        self.repo = repo
        self.todos = []
        self.next_id = 1

    def add(self, todo: Todo) -> Todo:
        todo.id = self.next_id
        self.next_id += 1
        self.todos.append(todo)
        return todo

    def find_by_id(self, todo_id: int) -> Todo | None:
        for todo in self.todos:
            if todo.id == todo_id: return todo
        return None

    def find_all(self) -> list[Todo]:
        return self.todos

    def update(self, todo: Todo) -> Todo:
        for index, existing_todo in enumerate(self.todos):
            if existing_todo.id == todo.id:
                self.todos[index] = todo
                return todo
        return None

    def delete(self, todo_id: int) -> None:
        for todo in self.todos:
            if todo.id == todo_id:
                self.todos.remove(todo)
                return
