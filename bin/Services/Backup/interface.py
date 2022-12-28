from fastapi import FastAPI, Request, Response, status
from Infrastructure.Gateway import route, settings


def Backups_Trigger(app: FastAPI, tags: list[str] = []):
    @route(
        path="/FileManager/backup/trigger/{backup_name}",
        request_method=app.post,
        payload_key=None,
        status_code=status.HTTP_200_OK,
        service_url=settings.BACKUP_SERVICE_URL,
        authentication_required=False,
        post_processing_func=None,
        tags=tags,
    )
    async def trigger_backup(backup_name: str, request: Request, response: Response):
        pass

    @route(
        path="/FileManager/backup/trigger_all",
        request_method=app.post,
        payload_key=None,
        status_code=status.HTTP_200_OK,
        service_url=settings.BACKUP_SERVICE_URL,
        authentication_required=False,
        post_processing_func=None,
        tags=tags,
    )
    async def trigger_all_backups(request: Request, response: Response):
        pass
