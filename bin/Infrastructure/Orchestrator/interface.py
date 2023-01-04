from conf import settings
from fastapi import FastAPI, Request, Response, status
from Infrastructure.Gateway import route
from Models import ServicesFilter


def OrchestratorInfrastructureInterface(app: FastAPI, tags: list[str] = []):
    @route(
        path="/up/{server_name}",
        request_method=app.post,
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
        path="/up",
        request_method=app.post,
        payload_key="services_filter",
        status_code=status.HTTP_200_OK,
        service_url=settings.ORCHESTRATOR_INFRASTRUCTURE_URL,
        authentication_required=False,
        post_processing_func=None,
        tags=tags,
    )
    async def orchestrator_up_list(
        services_filter: ServicesFilter, request: Request, response: Response
    ):
        pass

    @route(
        path="/down/{server_name}",
        request_method=app.post,
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
        path="/down",
        request_method=app.post,
        payload_key="services_filter",
        status_code=status.HTTP_200_OK,
        service_url=settings.ORCHESTRATOR_INFRASTRUCTURE_URL,
        authentication_required=False,
        post_processing_func=None,
        tags=tags,
    )
    async def orchestrator_down_list(
        services_filter: ServicesFilter, request: Request, response: Response
    ):
        pass

    @route(
        path="/restart/{server_name}",
        request_method=app.post,
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
        path="/restart",
        request_method=app.post,
        payload_key="services_filter",
        status_code=status.HTTP_200_OK,
        service_url=settings.ORCHESTRATOR_INFRASTRUCTURE_URL,
        authentication_required=False,
        post_processing_func=None,
        tags=tags,
    )
    async def orchestrator_restart_list(
        services_filter: ServicesFilter, request: Request, response: Response
    ):
        pass

    @route(
        path="/status/{server_name}",
        request_method=app.post,
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

    @route(
        path="/status",
        request_method=app.post,
        payload_key="services_filter",
        status_code=status.HTTP_200_OK,
        service_url=settings.ORCHESTRATOR_INFRASTRUCTURE_URL,
        authentication_required=False,
        post_processing_func=None,
        tags=tags,
    )
    async def orchestrator_status_list(
        services_filter: ServicesFilter, request: Request, response: Response
    ):
        pass

    @route(
        path="/list",
        request_method=app.post,
        payload_key=None,
        status_code=status.HTTP_200_OK,
        service_url=settings.ORCHESTRATOR_INFRASTRUCTURE_URL,
        authentication_required=False,
        post_processing_func=None,
        tags=tags,
    )
    async def orchestrator_list(request: Request, response: Response):
        pass
