from autobahn.asyncio.component import Component
from autobahn.asyncio.component import run
from autobahn.asyncio.wamp import ApplicationSession
import asyncio 

comp = Component(
    transports="ws://localhost:8080/ws",
    realm="realm1",
)

@comp.on_join
async def joined(session, details):
    print("session ready")
    asyncio.create_task(update(session))

async def update(session):
    while True:
        session.publish('publish', 1)
        print('test')
        await asyncio.sleep(1)


if __name__ == "__main__":
    run([comp])
    