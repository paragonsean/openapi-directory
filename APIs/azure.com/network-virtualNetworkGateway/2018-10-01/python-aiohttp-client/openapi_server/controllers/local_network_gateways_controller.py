from typing import List, Dict
from aiohttp import web

from openapi_server.models.local_network_gateway import LocalNetworkGateway
from openapi_server.models.local_network_gateway_list_result import LocalNetworkGatewayListResult
from openapi_server.models.virtual_network_gateway_connections_update_tags_request import VirtualNetworkGatewayConnectionsUpdateTagsRequest
from openapi_server import util


async def local_network_gateways_create_or_update(request: web.Request, resource_group_name, local_network_gateway_name, api_version, subscription_id, parameters) -> web.Response:
    """local_network_gateways_create_or_update

    Creates or updates a local network gateway in the specified resource group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param local_network_gateway_name: The name of the local network gateway.
    :type local_network_gateway_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to the create or update local network gateway operation.
    :type parameters: dict | bytes

    """
    parameters = LocalNetworkGateway.from_dict(parameters)
    return web.Response(status=200)


async def local_network_gateways_delete(request: web.Request, resource_group_name, local_network_gateway_name, api_version, subscription_id) -> web.Response:
    """local_network_gateways_delete

    Deletes the specified local network gateway.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param local_network_gateway_name: The name of the local network gateway.
    :type local_network_gateway_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def local_network_gateways_get(request: web.Request, resource_group_name, local_network_gateway_name, api_version, subscription_id) -> web.Response:
    """local_network_gateways_get

    Gets the specified local network gateway in a resource group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param local_network_gateway_name: The name of the local network gateway.
    :type local_network_gateway_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def local_network_gateways_list(request: web.Request, resource_group_name, api_version, subscription_id) -> web.Response:
    """local_network_gateways_list

    Gets all the local network gateways in a resource group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def local_network_gateways_update_tags(request: web.Request, resource_group_name, local_network_gateway_name, api_version, subscription_id, parameters) -> web.Response:
    """local_network_gateways_update_tags

    Updates a local network gateway tags.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param local_network_gateway_name: The name of the local network gateway.
    :type local_network_gateway_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to update local network gateway tags.
    :type parameters: dict | bytes

    """
    parameters = VirtualNetworkGatewayConnectionsUpdateTagsRequest.from_dict(parameters)
    return web.Response(status=200)
