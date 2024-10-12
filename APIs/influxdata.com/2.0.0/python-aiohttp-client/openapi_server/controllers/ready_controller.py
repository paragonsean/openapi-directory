from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.ready import Ready
from openapi_server import util


async def get_ready(request: web.Request, zap_trace_span=None) -> web.Response:
    """Get the readiness of an instance at startup

    

    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    return web.Response(status=200)
