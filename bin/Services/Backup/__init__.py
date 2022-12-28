from fastapi import FastAPI
from .interface import Backups_Trigger


def BackupInterface(app: FastAPI, tags: list[str] = []):
    Backups_Trigger(app, tags)
