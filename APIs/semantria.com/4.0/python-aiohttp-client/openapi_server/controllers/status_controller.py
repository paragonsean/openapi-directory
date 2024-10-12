from typing import List, Dict
from aiohttp import web

from openapi_server.models.status import Status
from openapi_server import util


async def get_status(request: web.Request, content_type) -> web.Response:
    """Retrieve API status

    This method retrieves API status information such as the app version, current API version, supported languages and encodings, the overall service status, etc.

    :param content_type: 
    :type content_type: str

    """
    return web.Response(status=200)
