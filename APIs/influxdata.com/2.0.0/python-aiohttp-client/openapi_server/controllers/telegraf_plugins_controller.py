from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.telegraf_plugins import TelegrafPlugins
from openapi_server import util


async def get_telegraf_plugins(request: web.Request, zap_trace_span=None, type=None) -> web.Response:
    """List all Telegraf plugins

    

    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str
    :param type: The type of plugin desired.
    :type type: str

    """
    return web.Response(status=200)
