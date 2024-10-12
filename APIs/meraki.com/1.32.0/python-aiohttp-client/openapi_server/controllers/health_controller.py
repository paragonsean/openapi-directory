from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_network_health_alerts200_response_inner import GetNetworkHealthAlerts200ResponseInner
from openapi_server import util


async def get_network_health_alerts_1(request: web.Request, network_id) -> web.Response:
    """Return all global alerts on this network

    Return all global alerts on this network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)
