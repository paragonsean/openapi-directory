from typing import List, Dict
from aiohttp import web

from openapi_server.models.update_network_traffic_analysis_request import UpdateNetworkTrafficAnalysisRequest
from openapi_server import util


async def get_network_traffic_analysis_1(request: web.Request, network_id) -> web.Response:
    """Return the traffic analysis settings for a network

    Return the traffic analysis settings for a network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def update_network_traffic_analysis_1(request: web.Request, network_id, body=None) -> web.Response:
    """Update the traffic analysis settings for a network

    Update the traffic analysis settings for a network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkTrafficAnalysisRequest.from_dict(body)
    return web.Response(status=200)
