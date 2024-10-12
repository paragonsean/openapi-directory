from typing import List, Dict
from aiohttp import web

from openapi_server.models.update_network_switch_stp_request import UpdateNetworkSwitchStpRequest
from openapi_server import util


async def get_network_switch_stp_1(request: web.Request, network_id) -> web.Response:
    """Returns STP settings

    Returns STP settings

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def update_network_switch_stp_1(request: web.Request, network_id, body=None) -> web.Response:
    """Updates STP settings

    Updates STP settings

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkSwitchStpRequest.from_dict(body)
    return web.Response(status=200)
