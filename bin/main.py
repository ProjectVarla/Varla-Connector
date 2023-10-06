from dataclasses import dataclass
from typing import List
import uvicorn
from Infrastructure.Orchestrator import OrchestratorInterface
from conf import settings
from Cores import PushNotififcationInterface
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from Services import BackupInterface, TaskInterface
from VarlaLib.Decorations import header
from websocket import create_connection

from starlette.websockets import WebSocket, WebSocketState

app = FastAPI(title="Varla-Connector")


TaskInterface(app, ["Tasks"])
BackupInterface(app, ["Backup"])
PushNotififcationInterface(app, ["Notification"])
OrchestratorInterface(app, ["Orchestrator"])


@dataclass
class Socket:
    websocket: WebSocket
    acknowledged: bool
    id: int


class Notifier:
    def __init__(self):
        self.connections: dict[str, List[Socket]] = {}
        self.generator = self.get_notification_generator()

    async def get_notification_generator(self):
        while True:
            message, channel_name = yield
            await self._notify(channel_name=channel_name, message=message)

    async def push(self, channel_name: str, message: str):
        await self.generator.asend((message, channel_name))
        print(self.connections)

    async def subscribe(self, channel_name: str, socket: Socket):
        await socket.websocket.accept()

        if channel_name not in self.connections:
            self.connections[channel_name] = []

        self.connections[channel_name].append(socket)

    def remove(self, channel_name: str, socket: Socket):
        self.connections[channel_name].remove(socket)

    async def close_all(self):
        for channel in self.connections:
            while len(self.connections[channel]) > 0:
                socket = self.connections[channel].pop()
                await self.close(socket)

    async def close(self, socket: Socket):
        await socket.websocket.close()

    async def _notify(self, channel_name: str, message: str):
        living_connections = []
        while (
            channel_name in self.connections and len(self.connections[channel_name]) > 0
        ):
            socket = self.connections[channel_name].pop()

            if socket.acknowledged:
                # socket.acknowledged = False
                await socket.websocket.send_text(message)
                living_connections.append(socket)
            else:
                self.close(socket)

        self.connections[channel_name] = living_connections


notifier = Notifier()


@app.websocket("/bind/{channel_name}")
async def deco_socket(websocket: WebSocket, channel_name: str, url: str = ""):
    socket = Socket(websocket=websocket, acknowledged=True, id=1)

    await notifier.subscribe(channel_name=channel_name, socket=socket)
    print(websocket)

    try:
        ws = create_connection(f"ws://localhost:8500/bind/{channel_name}")
        await socket.websocket.send_text(f"Connected!")
        socket.acknowledged = True
        while True:
            # print("socket", data, socket.id)
            core = ws.recv()
            print("core:", core)

            await websocket.send_text(f"core: {core}")
            client = await socket.websocket.receive()
            print("client:", client)

            if client["type"] == "websocket.disconnect":
                print(socket.websocket, "bye")
                ws.close()
                notifier.remove(channel_name=channel_name, socket=socket.websocket)
                return
            elif client["text"] == "alive":
                print("here")
                ws.send("alive")
                socket.acknowledged = True
                print("here 2")

    except WebSocketDisconnect:
        notifier.remove(channel_name=channel_name, websocket=socket.websocket)

    # generate ID
    # Assoiciate ID to websocket
    # send Notification core ID to connect
    # accept client socket after notification core establishes connection
    # Listen to any of the client sockets and send to Notifcation core
    # listen to any of the notification core socket and send to client
    # if any of the sockets closes it closes the other one too

    pass


# @app.websocket("/bind/{channel_name}")
# async def bind(websocket: WebSocket, channel_name: str):
#     deco_socket(websocket=websocket, channel_name=channel_name, url="")
#     pass


if __name__ == "__main__":
    header()
    uvicorn.run(
        "main:app",
        port=settings.GATEWAY_PORT,
        host=str(settings.GATEWAY_HOST),
    )
