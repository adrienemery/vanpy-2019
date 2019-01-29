from autobahn.asyncio.component import Component
from autobahn.asyncio.component import run
from autobahn.asyncio.wamp import ApplicationSession
import asyncio 

comp = Component(
    # transports="wss://vanpy-wamp.herokuapp.com/ws",
    transports="ws://localhost:8080/ws",
    realm="realm1",
)

@comp.on_join
async def joined(session, details):
    print("session ready")

@comp.subscribe('bot.update')
async def handle(data):
    print(data)
    

if __name__ == "__main__":
    run([comp])
    