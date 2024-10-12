from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_status import APIStatus
from openapi_server import util


async def get_status(request: web.Request, if_none_match=None) -> web.Response:
    """get_status

    Returns API status, and TBA status information.

    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)
