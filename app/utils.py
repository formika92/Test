import asyncio

from app.locks import with_lock
from settings import TIMEOUT


@with_lock
async def work() -> None:
    await asyncio.sleep(TIMEOUT)
