from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_realtime(request: web.Request, sec_websocket_protocol) -> web.Response:
    """get_realtime

    Use to request a Websockets handshake

    :param sec_websocket_protocol: The JWT token to use for auth
    :type sec_websocket_protocol: str

    """
    return web.Response(status=200)
