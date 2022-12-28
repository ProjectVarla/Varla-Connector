from os import getenv

import uvicorn
from Cores import Push_Notififcation
from dotenv import load_dotenv
from fastapi import FastAPI
from Services import BackupInterface, TaskInterface

app = FastAPI(title="Varla-Connector")

PORT: int = int(getenv("GATEWAY_PORT"))

TaskInterface(app, ["Tasks"])
BackupInterface(app, ["Backup"])
Push_Notififcation(app, ["Notification"])

if __name__ == "__main__":
    uvicorn.run("main:app", port=PORT)
