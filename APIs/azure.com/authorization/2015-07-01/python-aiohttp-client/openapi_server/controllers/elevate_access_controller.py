from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def elevate_access_post(request: web.Request, api_version) -> web.Response:
    """elevate_access_post

    Elevates access for a Global Administrator.

    :param api_version: The API version to use for this operation.
    :type api_version: str

    """
    return web.Response(status=200)
