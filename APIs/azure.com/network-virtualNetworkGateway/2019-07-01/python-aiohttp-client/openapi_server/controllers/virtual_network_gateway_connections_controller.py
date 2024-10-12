from typing import List, Dict
from aiohttp import web

from openapi_server.models.connection_reset_shared_key import ConnectionResetSharedKey
from openapi_server.models.connection_shared_key import ConnectionSharedKey
from openapi_server.models.virtual_network_gateway_connection import VirtualNetworkGatewayConnection
from openapi_server.models.virtual_network_gateway_connection_list_result import VirtualNetworkGatewayConnectionListResult
from openapi_server.models.virtual_network_gateway_connections_start_packet_capture_default_response import VirtualNetworkGatewayConnectionsStartPacketCaptureDefaultResponse
from openapi_server.models.virtual_network_gateway_connections_update_tags_request import VirtualNetworkGatewayConnectionsUpdateTagsRequest
from openapi_server.models.vpn_packet_capture_start_parameters import VpnPacketCaptureStartParameters
from openapi_server.models.vpn_packet_capture_stop_parameters import VpnPacketCaptureStopParameters
from openapi_server import util


async def virtual_network_gateway_connections_create_or_update(request: web.Request, resource_group_name, virtual_network_gateway_connection_name, api_version, subscription_id, parameters) -> web.Response:
    """virtual_network_gateway_connections_create_or_update

    Creates or updates a virtual network gateway connection in the specified resource group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param virtual_network_gateway_connection_name: The name of the virtual network gateway connection.
    :type virtual_network_gateway_connection_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to the create or update virtual network gateway connection operation.
    :type parameters: dict | bytes

    """
    parameters = VirtualNetworkGatewayConnection.from_dict(parameters)
    return web.Response(status=200)


async def virtual_network_gateway_connections_delete(request: web.Request, resource_group_name, virtual_network_gateway_connection_name, api_version, subscription_id) -> web.Response:
    """virtual_network_gateway_connections_delete

    Deletes the specified virtual network Gateway connection.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param virtual_network_gateway_connection_name: The name of the virtual network gateway connection.
    :type virtual_network_gateway_connection_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def virtual_network_gateway_connections_get(request: web.Request, resource_group_name, virtual_network_gateway_connection_name, api_version, subscription_id) -> web.Response:
    """virtual_network_gateway_connections_get

    Gets the specified virtual network gateway connection by resource group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param virtual_network_gateway_connection_name: The name of the virtual network gateway connection.
    :type virtual_network_gateway_connection_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def virtual_network_gateway_connections_get_shared_key(request: web.Request, resource_group_name, virtual_network_gateway_connection_name, api_version, subscription_id) -> web.Response:
    """virtual_network_gateway_connections_get_shared_key

    The Get VirtualNetworkGatewayConnectionSharedKey operation retrieves information about the specified virtual network gateway connection shared key through Network resource provider.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param virtual_network_gateway_connection_name: The virtual network gateway connection shared key name.
    :type virtual_network_gateway_connection_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def virtual_network_gateway_connections_list(request: web.Request, resource_group_name, api_version, subscription_id) -> web.Response:
    """virtual_network_gateway_connections_list

    The List VirtualNetworkGatewayConnections operation retrieves all the virtual network gateways connections created.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def virtual_network_gateway_connections_reset_shared_key(request: web.Request, resource_group_name, virtual_network_gateway_connection_name, api_version, subscription_id, parameters) -> web.Response:
    """virtual_network_gateway_connections_reset_shared_key

    The VirtualNetworkGatewayConnectionResetSharedKey operation resets the virtual network gateway connection shared key for passed virtual network gateway connection in the specified resource group through Network resource provider.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param virtual_network_gateway_connection_name: The virtual network gateway connection reset shared key Name.
    :type virtual_network_gateway_connection_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to the begin reset virtual network gateway connection shared key operation through network resource provider.
    :type parameters: dict | bytes

    """
    parameters = ConnectionResetSharedKey.from_dict(parameters)
    return web.Response(status=200)


async def virtual_network_gateway_connections_set_shared_key(request: web.Request, resource_group_name, virtual_network_gateway_connection_name, api_version, subscription_id, parameters) -> web.Response:
    """virtual_network_gateway_connections_set_shared_key

    The Put VirtualNetworkGatewayConnectionSharedKey operation sets the virtual network gateway connection shared key for passed virtual network gateway connection in the specified resource group through Network resource provider.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param virtual_network_gateway_connection_name: The virtual network gateway connection name.
    :type virtual_network_gateway_connection_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to the Begin Set Virtual Network Gateway connection Shared key operation throughNetwork resource provider.
    :type parameters: dict | bytes

    """
    parameters = ConnectionSharedKey.from_dict(parameters)
    return web.Response(status=200)


async def virtual_network_gateway_connections_start_packet_capture(request: web.Request, resource_group_name, virtual_network_gateway_connection_name, api_version, subscription_id, parameters=None) -> web.Response:
    """virtual_network_gateway_connections_start_packet_capture

    Starts packet capture on virtual network gateway connection in the specified resource group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param virtual_network_gateway_connection_name: The name of the virtual network gateway connection.
    :type virtual_network_gateway_connection_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Virtual network gateway packet capture parameters supplied to start packet capture on gateway connection.
    :type parameters: dict | bytes

    """
    parameters = VpnPacketCaptureStartParameters.from_dict(parameters)
    return web.Response(status=200)


async def virtual_network_gateway_connections_stop_packet_capture(request: web.Request, resource_group_name, virtual_network_gateway_connection_name, api_version, subscription_id, parameters) -> web.Response:
    """virtual_network_gateway_connections_stop_packet_capture

    Stops packet capture on virtual network gateway connection in the specified resource group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param virtual_network_gateway_connection_name: The name of the virtual network gateway Connection.
    :type virtual_network_gateway_connection_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Virtual network gateway packet capture parameters supplied to stop packet capture on gateway connection.
    :type parameters: dict | bytes

    """
    parameters = VpnPacketCaptureStopParameters.from_dict(parameters)
    return web.Response(status=200)


async def virtual_network_gateway_connections_update_tags(request: web.Request, resource_group_name, virtual_network_gateway_connection_name, api_version, subscription_id, parameters) -> web.Response:
    """virtual_network_gateway_connections_update_tags

    Updates a virtual network gateway connection tags.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param virtual_network_gateway_connection_name: The name of the virtual network gateway connection.
    :type virtual_network_gateway_connection_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to update virtual network gateway connection tags.
    :type parameters: dict | bytes

    """
    parameters = VirtualNetworkGatewayConnectionsUpdateTagsRequest.from_dict(parameters)
    return web.Response(status=200)
