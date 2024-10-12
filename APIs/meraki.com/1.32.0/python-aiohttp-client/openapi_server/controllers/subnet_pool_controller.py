from typing import List, Dict
from aiohttp import web

from openapi_server.models.update_network_cellular_gateway_subnet_pool_request import UpdateNetworkCellularGatewaySubnetPoolRequest
from openapi_server import util


async def get_network_cellular_gateway_subnet_pool_1(request: web.Request, network_id) -> web.Response:
    """Return the subnet pool and mask configured for MGs in the network.

    Return the subnet pool and mask configured for MGs in the network.

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def update_network_cellular_gateway_subnet_pool_1(request: web.Request, network_id, body=None) -> web.Response:
    """Update the subnet pool and mask configuration for MGs in the network.

    Update the subnet pool and mask configuration for MGs in the network.

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkCellularGatewaySubnetPoolRequest.from_dict(body)
    return web.Response(status=200)
