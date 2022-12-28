import uvicorn
from Cores import Push_Notififcation
from fastapi import FastAPI
from Services import BackupInterface, TaskInterface

app = FastAPI(title="Varla-Connector")


TaskInterface(app, ["Tasks"])
BackupInterface(app, ["Backup"])
Push_Notififcation(app, ["Notification"])

if __name__ == "__main__":
    uvicorn.run("main:app", port=8002, reload=True)
