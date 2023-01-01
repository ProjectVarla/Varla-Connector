from fastapi import FastAPI


from .interface import PushNotififcationInterface


def NotificationInterface(app: FastAPI, tags: list[str] = []):
    PushNotififcationInterface(app, tags)
