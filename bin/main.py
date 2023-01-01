import uvicorn
from conf import settings
from Cores import PushNotififcationInterface
from fastapi import FastAPI
from Services import BackupInterface, TaskInterface
from VarlaLib.Shell import varla_header

app = FastAPI(title="Varla-Connector")


TaskInterface(app, ["Tasks"])
BackupInterface(app, ["Backup"])
PushNotififcationInterface(app, ["Notification"])


if __name__ == "__main__":
    varla_header()
    uvicorn.run(
        "main:app",
        port=settings.GATEWAY_PORT,
        host=str(settings.GATEWAY_HOST),
    )
