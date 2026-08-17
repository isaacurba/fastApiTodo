from fastapi import APIRouter, HTTPException

from fastapiproject.models.todo import Todo
from fastapiproject.services.todo_service import (TodoService, TodoNotFoundError)

router = APIRouter()

def create_todo_controller(service: TodoService):
    @router.post("/todos/", status_code=201)
    def create_todo(todo: Todo):
        return service.add(todo)

    @router.get("/todos/")
    def get_all_todos():
        return service.find_all()

    @router.get("/todos/{todo_id}")
    def get_todo(todo_id: int):
        try:
            return service.find_by_id(todo_id)
        except TodoNotFoundError:
            raise HTTPException(status_code=404, detail="Todo not found")

    @router.patch("/todos/{todo_id}")
    def update_todo(todo_id: int, todo: Todo):
        try:
            todo.id = todo_id
            return service.update(todo)
        except TodoNotFoundError:
            raise HTTPException(status_code=404, detail="Todo not found")

    @router.delete("/todos/{todo_id}")
    def delete_todo(todo_id: int):
        try:
            service.delete(todo_id)
        except TodoNotFoundError:
            raise HTTPException(status_code=404, detail="Tddo not found")


    return router

