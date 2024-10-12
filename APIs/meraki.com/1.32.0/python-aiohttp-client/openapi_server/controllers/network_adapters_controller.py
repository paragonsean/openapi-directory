from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_network_sm_device_network_adapters200_response_inner import GetNetworkSmDeviceNetworkAdapters200ResponseInner
from openapi_server import util


async def get_network_sm_device_network_adapters_2(request: web.Request, network_id, device_id) -> web.Response:
    """List the network adapters of a device

    List the network adapters of a device

    :param network_id: 
    :type network_id: str
    :param device_id: 
    :type device_id: str

    """
    return web.Response(status=200)
