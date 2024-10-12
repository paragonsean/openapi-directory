from typing import List, Dict
from aiohttp import web

from openapi_server.models.network_interfaces_get_virtual_machine_scale_set_ip_configuration200_response import NetworkInterfacesGetVirtualMachineScaleSetIpConfiguration200Response
from openapi_server.models.network_interfaces_get_virtual_machine_scale_set_network_interface200_response import NetworkInterfacesGetVirtualMachineScaleSetNetworkInterface200Response
from openapi_server.models.network_interfaces_list_virtual_machine_scale_set_ip_configurations200_response import NetworkInterfacesListVirtualMachineScaleSetIpConfigurations200Response
from openapi_server.models.network_interfaces_list_virtual_machine_scale_set_network_interfaces200_response import NetworkInterfacesListVirtualMachineScaleSetNetworkInterfaces200Response
from openapi_server import util


async def network_interfaces_get_virtual_machine_scale_set_ip_configuration(request: web.Request, resource_group_name, virtual_machine_scale_set_name, virtualmachine_index, network_interface_name, ip_configuration_name, api_version, subscription_id, expand=None) -> web.Response:
    """network_interfaces_get_virtual_machine_scale_set_ip_configuration

    Get the specified network interface ip configuration in a virtual machine scale set.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param virtual_machine_scale_set_name: The name of the virtual machine scale set.
    :type virtual_machine_scale_set_name: str
    :param virtualmachine_index: The virtual machine index.
    :type virtualmachine_index: str
    :param network_interface_name: The name of the network interface.
    :type network_interface_name: str
    :param ip_configuration_name: The name of the ip configuration.
    :type ip_configuration_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param expand: Expands referenced resources.
    :type expand: str

    """
    return web.Response(status=200)


async def network_interfaces_get_virtual_machine_scale_set_network_interface(request: web.Request, resource_group_name, virtual_machine_scale_set_name, virtualmachine_index, network_interface_name, api_version, subscription_id, expand=None) -> web.Response:
    """network_interfaces_get_virtual_machine_scale_set_network_interface

    Get the specified network interface in a virtual machine scale set.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param virtual_machine_scale_set_name: The name of the virtual machine scale set.
    :type virtual_machine_scale_set_name: str
    :param virtualmachine_index: The virtual machine index.
    :type virtualmachine_index: str
    :param network_interface_name: The name of the network interface.
    :type network_interface_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param expand: Expands referenced resources.
    :type expand: str

    """
    return web.Response(status=200)


async def network_interfaces_list_virtual_machine_scale_set_ip_configurations(request: web.Request, resource_group_name, virtual_machine_scale_set_name, virtualmachine_index, network_interface_name, api_version, subscription_id, expand=None) -> web.Response:
    """network_interfaces_list_virtual_machine_scale_set_ip_configurations

    Get the specified network interface ip configuration in a virtual machine scale set.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param virtual_machine_scale_set_name: The name of the virtual machine scale set.
    :type virtual_machine_scale_set_name: str
    :param virtualmachine_index: The virtual machine index.
    :type virtualmachine_index: str
    :param network_interface_name: The name of the network interface.
    :type network_interface_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param expand: Expands referenced resources.
    :type expand: str

    """
    return web.Response(status=200)


async def network_interfaces_list_virtual_machine_scale_set_network_interfaces(request: web.Request, resource_group_name, virtual_machine_scale_set_name, api_version, subscription_id) -> web.Response:
    """network_interfaces_list_virtual_machine_scale_set_network_interfaces

    Gets all network interfaces in a virtual machine scale set.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param virtual_machine_scale_set_name: The name of the virtual machine scale set.
    :type virtual_machine_scale_set_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def network_interfaces_list_virtual_machine_scale_set_vm_network_interfaces(request: web.Request, resource_group_name, virtual_machine_scale_set_name, virtualmachine_index, api_version, subscription_id) -> web.Response:
    """network_interfaces_list_virtual_machine_scale_set_vm_network_interfaces

    Gets information about all network interfaces in a virtual machine in a virtual machine scale set.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param virtual_machine_scale_set_name: The name of the virtual machine scale set.
    :type virtual_machine_scale_set_name: str
    :param virtualmachine_index: The virtual machine index.
    :type virtualmachine_index: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)
