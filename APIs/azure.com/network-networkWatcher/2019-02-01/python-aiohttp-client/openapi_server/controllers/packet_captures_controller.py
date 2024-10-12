from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.packet_capture import PacketCapture
from openapi_server.models.packet_capture_list_result import PacketCaptureListResult
from openapi_server.models.packet_capture_query_status_result import PacketCaptureQueryStatusResult
from openapi_server.models.packet_capture_result import PacketCaptureResult
from openapi_server import util


async def packet_captures_create(request: web.Request, resource_group_name, network_watcher_name, packet_capture_name, api_version, subscription_id, parameters) -> web.Response:
    """packet_captures_create

    Create and start a packet capture on the specified VM.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param network_watcher_name: The name of the network watcher.
    :type network_watcher_name: str
    :param packet_capture_name: The name of the packet capture session.
    :type packet_capture_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters that define the create packet capture operation.
    :type parameters: dict | bytes

    """
    parameters = PacketCapture.from_dict(parameters)
    return web.Response(status=200)


async def packet_captures_delete(request: web.Request, resource_group_name, network_watcher_name, packet_capture_name, api_version, subscription_id) -> web.Response:
    """packet_captures_delete

    Deletes the specified packet capture session.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param network_watcher_name: The name of the network watcher.
    :type network_watcher_name: str
    :param packet_capture_name: The name of the packet capture session.
    :type packet_capture_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def packet_captures_get(request: web.Request, resource_group_name, network_watcher_name, packet_capture_name, api_version, subscription_id) -> web.Response:
    """packet_captures_get

    Gets a packet capture session by name.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param network_watcher_name: The name of the network watcher.
    :type network_watcher_name: str
    :param packet_capture_name: The name of the packet capture session.
    :type packet_capture_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def packet_captures_get_status(request: web.Request, resource_group_name, network_watcher_name, packet_capture_name, api_version, subscription_id) -> web.Response:
    """packet_captures_get_status

    Query the status of a running packet capture session.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param network_watcher_name: The name of the Network Watcher resource.
    :type network_watcher_name: str
    :param packet_capture_name: The name given to the packet capture session.
    :type packet_capture_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def packet_captures_list(request: web.Request, resource_group_name, network_watcher_name, api_version, subscription_id) -> web.Response:
    """packet_captures_list

    Lists all packet capture sessions within the specified resource group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param network_watcher_name: The name of the Network Watcher resource.
    :type network_watcher_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def packet_captures_stop(request: web.Request, resource_group_name, network_watcher_name, packet_capture_name, api_version, subscription_id) -> web.Response:
    """packet_captures_stop

    Stops a specified packet capture session.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param network_watcher_name: The name of the network watcher.
    :type network_watcher_name: str
    :param packet_capture_name: The name of the packet capture session.
    :type packet_capture_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)
