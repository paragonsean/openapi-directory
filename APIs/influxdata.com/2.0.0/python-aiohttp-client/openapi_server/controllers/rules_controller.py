from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.flux_response import FluxResponse
from openapi_server import util


async def get_notification_rules_id_query(request: web.Request, rule_id, zap_trace_span=None) -> web.Response:
    """Retrieve a notification rule query

    

    :param rule_id: The notification rule ID.
    :type rule_id: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    return web.Response(status=200)
