from typing import List, Dict
from aiohttp import web

from openapi_server.models.pong_response import PongResponse
from openapi_server import util


async def get_ping(request: web.Request, ) -> web.Response:
    """get_ping

    Returns a ping. In case you need a health check in your system. Cannot be called /ping as AWS is using this route for their health check. This webservice doesn&#39;t have CORS enable, as it&#39;s supposed to be call server to server and not from a webpage ( it won&#39;t work over the tester)


    """
    return web.Response(status=200)
