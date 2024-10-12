from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def lock_thing(request: web.Request, thing, lock, key) -> web.Response:
    """Reserve and lock a thing.

    

    :param thing: A unique name of a thing.
    :type thing: str
    :param lock: A valid dweet.io lock.
    :type lock: str
    :param key: A valid dweet.io master key.
    :type key: str

    """
    return web.Response(status=200)


async def remove_lock(request: web.Request, lock, key) -> web.Response:
    """Remove a lock from thing.

    

    :param lock: A valid dweet.io lock.
    :type lock: str
    :param key: A valid dweet.io master key.
    :type key: str

    """
    return web.Response(status=200)


async def unlock_thing(request: web.Request, thing, key) -> web.Response:
    """Unlock a thing.

    

    :param thing: A unique name of a thing.
    :type thing: str
    :param key: A valid dweet.io master key.
    :type key: str

    """
    return web.Response(status=200)
