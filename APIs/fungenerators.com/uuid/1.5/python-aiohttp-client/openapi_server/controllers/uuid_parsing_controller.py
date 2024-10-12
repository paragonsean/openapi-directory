from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def uuid_post(request: web.Request, uuidstr) -> web.Response:
    """uuid_post

    Parse a UUID string and return its version and check whether it is valid.

    :param uuidstr: UUID String to parse
    :type uuidstr: str

    """
    return web.Response(status=200)
