from fastapi import FastAPI


from .interface import Push_Notififcation

def NotificationInterface(app:FastAPI, tags:list[str] = []):
    Push_Notififcation(app,tags)