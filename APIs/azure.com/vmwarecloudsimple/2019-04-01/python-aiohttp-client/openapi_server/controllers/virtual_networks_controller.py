from typing import List, Dict
from aiohttp import web

from openapi_server.models.csrp_error import CSRPError
from openapi_server.models.virtual_network import VirtualNetwork
from openapi_server.models.virtual_network_list_response import VirtualNetworkListResponse
from openapi_server import util


async def virtual_networks_get(request: web.Request, subscription_id, region_id, pc_name, virtual_network_name, api_version) -> web.Response:
    """Implements virtual network GET method

    Return virtual network by its name

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param region_id: The region Id (westus, eastus)
    :type region_id: str
    :param pc_name: The private cloud name
    :type pc_name: str
    :param virtual_network_name: virtual network id (vsphereId)
    :type virtual_network_name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def virtual_networks_list(request: web.Request, subscription_id, region_id, pc_name, api_version, resource_pool_name) -> web.Response:
    """Implements list available virtual networks within a subscription method

    Return list of virtual networks in location for private cloud

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param region_id: The region Id (westus, eastus)
    :type region_id: str
    :param pc_name: The private cloud name
    :type pc_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param resource_pool_name: Resource pool used to derive vSphere cluster which contains virtual networks
    :type resource_pool_name: str

    """
    return web.Response(status=200)
