from fastapi import FastAPI

from .delete import TaskDeleteInterface
from .insert import TaskInsertInterface
from .retrieve import TaskRetrieveInterface
from .update import TaskUpdateInterface


def TaskInterface(app: FastAPI, tags: list[str] = []):
    TaskRetrieveInterface(app, tags)
    TaskInsertInterface(app, tags)
    TaskUpdateInterface(app, tags)
    TaskDeleteInterface(app, tags)
