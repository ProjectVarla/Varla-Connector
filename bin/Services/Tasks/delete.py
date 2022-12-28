from fastapi import FastAPI, Request, Response, status
from Infrastructure.Gateway import route, settings


def TaskDeleteInterface(app: FastAPI, tags: list[str] = []):
    @route(
        path="/api/tasks/delete/task/{task_id}",
        request_method=app.delete,
        payload_key="filter",
        status_code=status.HTTP_200_OK,
        service_url=settings.TASKS_SERVICE_URL,
        authentication_required=False,
        post_processing_func=None,
        tags=tags,
    )
    async def delete_task(task_id: int, request: Request, response: Response):
        pass

    @route(
        path="/api/tasks/delete/todo/{todo_id}",
        request_method=app.delete,
        payload_key="filter",
        status_code=status.HTTP_200_OK,
        service_url=settings.TASKS_SERVICE_URL,
        authentication_required=False,
        post_processing_func=None,
        tags=tags,
    )
    async def delete_todo(todo_id: int, request: Request, response: Response):
        pass
