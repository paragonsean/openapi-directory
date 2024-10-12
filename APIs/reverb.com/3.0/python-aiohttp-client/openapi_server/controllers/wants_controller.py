from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def wants_get(request: web.Request, ) -> web.Response:
    """A list of wanted items by the user

    A list of wanted items by the user


    """
    return web.Response(status=200)


async def wants_id_delete(request: web.Request, id) -> web.Response:
    """Unmark an item wanted.

    Unmark an item wanted.

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def wants_id_put(request: web.Request, id) -> web.Response:
    """Mark an item wanted. Returns 200 on success or 422 on failure.

    Mark an item wanted. Returns 200 on success or 422 on failure.

    :param id: 
    :type id: str

    """
    return web.Response(status=200)
