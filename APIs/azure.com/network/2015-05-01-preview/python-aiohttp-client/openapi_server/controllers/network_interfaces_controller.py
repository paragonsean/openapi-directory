from typing import List, Dict
from aiohttp import web

from openapi_server.models.network_interface import NetworkInterface
from openapi_server.models.network_interface_list_result import NetworkInterfaceListResult
from openapi_server import util


async def network_interfaces_create_or_update(request: web.Request, resource_group_name, network_interface_name, api_version, subscription_id, parameters) -> web.Response:
    """network_interfaces_create_or_update

    The Put NetworkInterface operation creates/updates a networkInterface

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param network_interface_name: The name of the network interface.
    :type network_interface_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to the create/update NetworkInterface operation
    :type parameters: dict | bytes

    """
    parameters = NetworkInterface.from_dict(parameters)
    return web.Response(status=200)


async def network_interfaces_delete(request: web.Request, resource_group_name, network_interface_name, api_version, subscription_id) -> web.Response:
    """network_interfaces_delete

    The delete networkInterface operation deletes the specified networkInterface.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param network_interface_name: The name of the network interface.
    :type network_interface_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def network_interfaces_get(request: web.Request, resource_group_name, network_interface_name, api_version, subscription_id) -> web.Response:
    """network_interfaces_get

    The Get network interface operation retrieves information about the specified network interface.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param network_interface_name: The name of the network interface.
    :type network_interface_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def network_interfaces_get_virtual_machine_scale_set_network_interface(request: web.Request, resource_group_name, virtual_machine_scale_set_name, virtualmachine_index, network_interface_name, api_version, subscription_id) -> web.Response:
    """network_interfaces_get_virtual_machine_scale_set_network_interface

    The Get network interface operation retrieves information about the specified network interface in a virtual machine scale set.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param virtual_machine_scale_set_name: The name of the virtual machine scale set.
    :type virtual_machine_scale_set_name: str
    :param virtualmachine_index: The virtual machine index.
    :type virtualmachine_index: str
    :param network_interface_name: The name of the network interface.
    :type network_interface_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def network_interfaces_list(request: web.Request, resource_group_name, api_version, subscription_id) -> web.Response:
    """network_interfaces_list

    The List networkInterfaces operation retrieves all the networkInterfaces in a resource group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def network_interfaces_list_all(request: web.Request, api_version, subscription_id) -> web.Response:
    """network_interfaces_list_all

    The List networkInterfaces operation retrieves all the networkInterfaces in a subscription.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def network_interfaces_list_virtual_machine_scale_set_network_interfaces(request: web.Request, resource_group_name, virtual_machine_scale_set_name, api_version, subscription_id) -> web.Response:
    """network_interfaces_list_virtual_machine_scale_set_network_interfaces

    The list network interface operation retrieves information about all network interfaces in a virtual machine scale set.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param virtual_machine_scale_set_name: The name of the virtual machine scale set.
    :type virtual_machine_scale_set_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def network_interfaces_list_virtual_machine_scale_set_vm_network_interfaces(request: web.Request, resource_group_name, virtual_machine_scale_set_name, virtualmachine_index, api_version, subscription_id) -> web.Response:
    """network_interfaces_list_virtual_machine_scale_set_vm_network_interfaces

    The list network interface operation retrieves information about all network interfaces in a virtual machine from a virtual machine scale set.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param virtual_machine_scale_set_name: The name of the virtual machine scale set.
    :type virtual_machine_scale_set_name: str
    :param virtualmachine_index: The virtual machine index.
    :type virtualmachine_index: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)
