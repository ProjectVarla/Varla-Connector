from fastapi import FastAPI, Request, Response, status
from Infrastructure.Gateway import route, settings
from Models import Task, Todo


def TaskUpdateInterface(app: FastAPI, tags: list[str] = []):
    @route(
        path="/api/tasks/update/task/{task_id}",
        request_method=app.put,
        payload_key="task",
        status_code=status.HTTP_200_OK,
        service_url=settings.TASKS_SERVICE_URL,
        authentication_required=False,
        post_processing_func=None,
        tags=tags,
    )
    async def modify_task(
        task_id: int, task: Task.Edit, request: Request, response: Response
    ):
        pass

    @route(
        path="/api/tasks/update/todo/{todo_id}",
        request_method=app.put,
        payload_key="todo",
        status_code=status.HTTP_200_OK,
        service_url=settings.TASKS_SERVICE_URL,
        authentication_required=False,
        post_processing_func=None,
        tags=tags
        # tags = ["tasks"]
    )
    async def modify_todo(
        todo_id: int, todo: Todo.Edit, request: Request, response: Response
    ):
        pass
