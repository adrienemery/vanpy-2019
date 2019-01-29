from autobahn.asyncio.component import Component
from autobahn.asyncio.component import run
from autobahn.asyncio.wamp import ApplicationSession
import asyncio 
from c_serial_thread import bot

comp = Component(
    # transports="wss://vanpy-wamp.herokuapp.com/ws",
    transports="ws://localhost:8080/ws",
    realm="realm1",
)

@comp.on_join
async def joined(session, details):
    print("session ready")
    asyncio.create_task(update(session))

@comp.register('bot.move')
async def move(val):
    bot.move(val)

async def update(session):
    while True:
        session.publish('bot.update', {'distance': bot.distance})
        await asyncio.sleep(1)


if __name__ == "__main__":
    run([comp])