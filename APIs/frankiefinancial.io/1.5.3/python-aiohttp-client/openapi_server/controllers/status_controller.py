from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_object import ErrorObject
from openapi_server.models.puppy_object import PuppyObject
from openapi_server import util


async def status_check(request: web.Request, asking_nicely=None) -> web.Response:
    """Service Status

    Simple check to see if the service is running smoothly.

    :param asking_nicely: If set to true, the request is being made politely. 
    :type asking_nicely: bool

    """
    return web.Response(status=200)
