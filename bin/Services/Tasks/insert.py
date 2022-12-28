from fastapi import FastAPI, Request, Response, status
from Infrastructure.Gateway import route, settings
from Models import Task, Todo


def TaskInsertInterface(app: FastAPI, tags: list[str] = []):
    @route(
        path="/api/tasks/insert/task",
        request_method=app.post,
        payload_key="task",
        status_code=status.HTTP_200_OK,
        service_url=settings.TASKS_SERVICE_URL,
        authentication_required=False,
        post_processing_func=None,
        tags=tags,
    )
    async def create_task(task: Task.Base, request: Request, response: Response):
        pass

    @route(
        path="/api/tasks/insert/todo/{task_id}",
        request_method=app.post,
        payload_key="todo",
        status_code=status.HTTP_200_OK,
        service_url=settings.TASKS_SERVICE_URL,
        authentication_required=False,
        post_processing_func=None,
        tags=tags,
    )
    async def create_todo(
        task_id: int, todo: Todo.Base, request: Request, response: Response
    ):
        pass
