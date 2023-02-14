from asyncio import Lock
from functools import wraps

_locks = {}


def with_lock(f):
    # for lock in different instances requires an intermediary,
    # for ex. Redis
    @wraps(f)
    async def wrapper(*args, **kwargs):
        lock_name = "{module}.{name}".format(module=f.__module__, name=f.__name__)
        lock = _locks.setdefault(lock_name, Lock())
        async with lock:
            return await f(*args, **kwargs)

    return wrapper