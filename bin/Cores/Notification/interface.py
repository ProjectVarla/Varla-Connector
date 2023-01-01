from fastapi import FastAPI, Request, Response, status
from Infrastructure.Gateway import route, settings
from Models.Cores import NotificationMessage


def PushNotififcationInterface(app: FastAPI, tags: list[str] = []):
    @route(
        path="/push/{channel_name}/{message}",
        request_method=app.get,
        payload_key=None,
        status_code=status.HTTP_200_OK,
        service_url=settings.NOTIFICATION_CORE_URL,
        authentication_required=False,
        post_processing_func=None,
        tags=tags,
    )
    async def push_notification(
        channel_name: str, message: str, request: Request, response: Response
    ):
        pass

    @route(
        path="/push",
        request_method=app.post,
        payload_key="message",
        status_code=status.HTTP_200_OK,
        service_url=settings.NOTIFICATION_CORE_URL,
        authentication_required=False,
        post_processing_func=None,
        tags=tags,
    )
    async def push_notification_post(
        message: NotificationMessage, request: Request, response: Response
    ):
        pass
