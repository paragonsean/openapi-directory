from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server import util


async def post_signin(request: web.Request, zap_trace_span=None) -> web.Response:
    """Exchange basic auth credentials for session

    

    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    return web.Response(status=200)


async def post_signout(request: web.Request, zap_trace_span=None) -> web.Response:
    """Expire the current session

    

    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    return web.Response(status=200)
