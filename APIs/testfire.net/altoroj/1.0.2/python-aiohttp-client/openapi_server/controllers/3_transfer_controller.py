from typing import List, Dict
from aiohttp import web

from openapi_server.models.transfer import Transfer
from openapi_server import util


async def trasnfer(request: web.Request, authorization, body) -> web.Response:
    """trasnfer

    Transfer money between two accounts

    :param authorization: Authorization token (provided upon successful login)
    :type authorization: str
    :param body: Transfer details including ammount, sender and receiver
    :type body: dict | bytes

    """
    body = Transfer.from_dict(body)
    return web.Response(status=200)
