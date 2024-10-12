from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.health_check import HealthCheck
from openapi_server import util


async def get_health(request: web.Request, zap_trace_span=None) -> web.Response:
    """Get the health of an instance

    

    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    return web.Response(status=200)
