from fastapi import FastAPI


from .interface import OrchestratorInfrastructureInterface


def OrchestratorInterface(app: FastAPI, tags: list[str] = []):
    OrchestratorInfrastructureInterface(app, tags)
