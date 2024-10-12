from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_network_sm_device_softwares200_response_inner import GetNetworkSmDeviceSoftwares200ResponseInner
from openapi_server import util


async def get_network_sm_device_softwares_2(request: web.Request, network_id, device_id) -> web.Response:
    """Get a list of softwares associated with a device

    Get a list of softwares associated with a device

    :param network_id: 
    :type network_id: str
    :param device_id: 
    :type device_id: str

    """
    return web.Response(status=200)


async def get_network_sm_user_softwares_2(request: web.Request, network_id, user_id) -> web.Response:
    """Get a list of softwares associated with a user

    Get a list of softwares associated with a user

    :param network_id: 
    :type network_id: str
    :param user_id: 
    :type user_id: str

    """
    return web.Response(status=200)
