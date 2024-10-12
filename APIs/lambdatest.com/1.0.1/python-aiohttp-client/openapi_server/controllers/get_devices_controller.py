from typing import List, Dict
from aiohttp import web

from openapi_server.models.access_denied import AccessDenied
from openapi_server.models.os_devices import OsDevices
from openapi_server import util


async def devices(request: web.Request, os=None) -> web.Response:
    """Fetch all available device combinations.

    Fetch all os devices combinations available on lambdatest platform.

    :param os: Fetch details for a particular OS
    :type os: str

    """
    return web.Response(status=200)
