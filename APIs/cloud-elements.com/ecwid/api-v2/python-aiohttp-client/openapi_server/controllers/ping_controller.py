from typing import List, Dict
from aiohttp import web

from openapi_server.models.pong import Pong
from openapi_server import util


async def get_ping(request: web.Request, authorization) -> web.Response:
    """Ping the Element to confirm that the Hub Element has a heartbeat.  If the Element does not have a heartbeat, an error message will be returned.

    

    :param authorization: The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39;
    :type authorization: str

    """
    return web.Response(status=200)
