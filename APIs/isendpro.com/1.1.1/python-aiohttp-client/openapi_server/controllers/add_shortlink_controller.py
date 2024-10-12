from typing import List, Dict
from aiohttp import web

from openapi_server.models.erreur import Erreur
from openapi_server.models.shortlink_request import ShortlinkRequest
from openapi_server.models.shortlink_response import ShortlinkResponse
from openapi_server import util


async def add_shortlink(request: web.Request, body) -> web.Response:
    """add a shortlink

    add a shortlink

    :param body: add sub account request
    :type body: dict | bytes

    """
    body = ShortlinkRequest.from_dict(body)
    return web.Response(status=200)
