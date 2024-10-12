from typing import List, Dict
from aiohttp import web

from openapi_server.models.subnet import Subnet
from openapi_server.models.subnet_list_result import SubnetListResult
from openapi_server import util


async def subnets_create_or_update(request: web.Request, resource_group_name, virtual_network_name, subnet_name, api_version, subscription_id, subnet_parameters) -> web.Response:
    """subnets_create_or_update

    The Put Subnet operation creates/updates a subnet in the specified virtual network

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param virtual_network_name: The name of the virtual network.
    :type virtual_network_name: str
    :param subnet_name: The name of the subnet.
    :type subnet_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param subnet_parameters: Parameters supplied to the create/update Subnet operation
    :type subnet_parameters: dict | bytes

    """
    subnet_parameters = Subnet.from_dict(subnet_parameters)
    return web.Response(status=200)


async def subnets_delete(request: web.Request, resource_group_name, virtual_network_name, subnet_name, api_version, subscription_id) -> web.Response:
    """subnets_delete

    The delete subnet operation deletes the specified subnet.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param virtual_network_name: The name of the virtual network.
    :type virtual_network_name: str
    :param subnet_name: The name of the subnet.
    :type subnet_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def subnets_get(request: web.Request, resource_group_name, virtual_network_name, subnet_name, api_version, subscription_id) -> web.Response:
    """subnets_get

    The Get subnet operation retrieves information about the specified subnet.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param virtual_network_name: The name of the virtual network.
    :type virtual_network_name: str
    :param subnet_name: The name of the subnet.
    :type subnet_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def subnets_list(request: web.Request, resource_group_name, virtual_network_name, api_version, subscription_id) -> web.Response:
    """subnets_list

    The List subnets operation retrieves all the subnets in a virtual network.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param virtual_network_name: The name of the virtual network.
    :type virtual_network_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)
