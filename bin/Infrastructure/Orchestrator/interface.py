from fastapi import FastAPI, Request, Response, status
from Infrastructure.Gateway import route
from conf import settings


def OrchestratorInfrastructureInterface(app: FastAPI, tags: list[str] = []):
    @route(
        path="/up/{server_name}",
        request_method=app.get,
        payload_key=None,
        status_code=status.HTTP_200_OK,
        service_url=settings.ORCHESTRATOR_INFRASTRUCTURE_URL,
        authentication_required=False,
        post_processing_func=None,
        tags=tags,
    )
    async def orchestrator_up(server_name: str, request: Request, response: Response):
        pass

    @route(
        path="/down/{server_name}",
        request_method=app.get,
        payload_key=None,
        status_code=status.HTTP_200_OK,
        service_url=settings.ORCHESTRATOR_INFRASTRUCTURE_URL,
        authentication_required=False,
        post_processing_func=None,
        tags=tags,
    )
    async def orchestrator_down(server_name: str, request: Request, response: Response):
        pass

    @route(
        path="/restart/{server_name}",
        request_method=app.get,
        payload_key=None,
        status_code=status.HTTP_200_OK,
        service_url=settings.ORCHESTRATOR_INFRASTRUCTURE_URL,
        authentication_required=False,
        post_processing_func=None,
        tags=tags,
    )
    async def orchestrator_restart(
        server_name: str, request: Request, response: Response
    ):
        pass

    @route(
        path="/status/{server_name}",
        request_method=app.get,
        payload_key=None,
        status_code=status.HTTP_200_OK,
        service_url=settings.ORCHESTRATOR_INFRASTRUCTURE_URL,
        authentication_required=False,
        post_processing_func=None,
        tags=tags,
    )
    async def orchestrator_status(
        server_name: str, request: Request, response: Response
    ):
        pass
