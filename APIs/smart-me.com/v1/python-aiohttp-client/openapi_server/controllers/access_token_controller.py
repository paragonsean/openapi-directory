from typing import List, Dict
from aiohttp import web

from openapi_server.models.access_token_to_put import AccessTokenToPut
from openapi_server import util


async def access_token_put(request: web.Request, body) -> web.Response:
    """Creates a Access Token to write on a Card (e.g. NFC)

    Creates a Access Token to write on a Card (e.g. NFC)

    :param body: 
    :type body: dict | bytes

    """
    body = AccessTokenToPut.from_dict(body)
    return web.Response(status=200)
