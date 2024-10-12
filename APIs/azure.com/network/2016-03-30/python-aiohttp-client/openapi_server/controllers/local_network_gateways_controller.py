from typing import List, Dict
from aiohttp import web

from openapi_server.models.local_network_gateway import LocalNetworkGateway
from openapi_server.models.local_network_gateway_list_result import LocalNetworkGatewayListResult
from openapi_server import util


async def local_network_gateways_create_or_update(request: web.Request, resource_group_name, local_network_gateway_name, api_version, subscription_id, parameters) -> web.Response:
    """local_network_gateways_create_or_update

    The Put LocalNetworkGateway operation creates/updates a local network gateway in the specified resource group through Network resource provider.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param local_network_gateway_name: The name of the local network gateway.
    :type local_network_gateway_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to the Begin Create or update Local Network Gateway operation through Network resource provider.
    :type parameters: dict | bytes

    """
    parameters = LocalNetworkGateway.from_dict(parameters)
    return web.Response(status=200)


async def local_network_gateways_delete(request: web.Request, resource_group_name, local_network_gateway_name, api_version, subscription_id) -> web.Response:
    """local_network_gateways_delete

    The Delete LocalNetworkGateway operation deletes the specified local network Gateway through Network resource provider.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param local_network_gateway_name: The name of the local network gateway.
    :type local_network_gateway_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def local_network_gateways_get(request: web.Request, resource_group_name, local_network_gateway_name, api_version, subscription_id) -> web.Response:
    """local_network_gateways_get

    The Get LocalNetworkGateway operation retrieves information about the specified local network gateway through Network resource provider.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param local_network_gateway_name: The name of the local network gateway.
    :type local_network_gateway_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def local_network_gateways_list(request: web.Request, resource_group_name, api_version, subscription_id) -> web.Response:
    """local_network_gateways_list

    The List LocalNetworkGateways operation retrieves all the local network gateways stored.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)
