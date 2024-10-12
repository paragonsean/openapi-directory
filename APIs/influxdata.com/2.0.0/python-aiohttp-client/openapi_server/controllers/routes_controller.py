from typing import List, Dict
from aiohttp import web

from openapi_server.models.routes import Routes
from openapi_server import util


async def get_routes(request: web.Request, zap_trace_span=None) -> web.Response:
    """List all top level routes

    

    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    return web.Response(status=200)
