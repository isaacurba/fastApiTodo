from fastapiproject.repositories.in_memory_todo_repo import (InMemoryTodoRepo)
from fastapiproject.services.todo_service import TodoService

repository = InMemoryTodoRepo()
todo_service = TodoService(repository)