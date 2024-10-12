from typing import List, Dict
from aiohttp import web

from openapi_server.models.access_denied import AccessDenied
from openapi_server.models.os_browsers import OsBrowsers
from openapi_server import util


async def os_browsers(request: web.Request, os=None) -> web.Response:
    """Fetch all available os-browser combinations.

    Fetch all os browsers combinations available on lambdatest platform.

    :param os: Fetch details for a particular OS
    :type os: str

    """
    return web.Response(status=200)
