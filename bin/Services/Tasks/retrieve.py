from fastapi import FastAPI, Request, Response, status
from Infrastructure.Gateway import route, settings
from Models import Task, Todo


def TaskRetrieveInterface(app: FastAPI, tags: list[str] = []):
    @route(
        path="/api/tasks/get/tasks",
        request_method=app.post,
        payload_key="filter",
        status_code=status.HTTP_200_OK,
        service_url=settings.TASKS_SERVICE_URL,
        authentication_required=False,
        post_processing_func=None,
        tags=tags,
    )
    async def get_tasks(filter: Task.Filter, request: Request, response: Response):
        pass

    @route(
        path="/api/tasks/get/todos",
        request_method=app.post,
        payload_key="filter",
        status_code=status.HTTP_200_OK,
        service_url=settings.TASKS_SERVICE_URL,
        authentication_required=False,
        post_processing_func=None,
        tags=tags,
    )
    async def get_todos(filter: Todo.Filter, request: Request, response: Response):
        pass
