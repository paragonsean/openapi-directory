from typing import List, Dict
from aiohttp import web

from openapi_server.models.public_ip_addresses_get_virtual_machine_scale_set_public_ip_address200_response import PublicIPAddressesGetVirtualMachineScaleSetPublicIPAddress200Response
from openapi_server.models.public_ip_addresses_list_virtual_machine_scale_set_public_ip_addresses200_response import PublicIPAddressesListVirtualMachineScaleSetPublicIPAddresses200Response
from openapi_server import util


async def public_ip_addresses_get_virtual_machine_scale_set_public_ip_address(request: web.Request, resource_group_name, virtual_machine_scale_set_name, virtualmachine_index, network_interface_name, ip_configuration_name, public_ip_address_name, api_version, subscription_id, expand=None) -> web.Response:
    """public_ip_addresses_get_virtual_machine_scale_set_public_ip_address

    Get the specified public IP address in a virtual machine scale set.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param virtual_machine_scale_set_name: The name of the virtual machine scale set.
    :type virtual_machine_scale_set_name: str
    :param virtualmachine_index: The virtual machine index.
    :type virtualmachine_index: str
    :param network_interface_name: The name of the network interface.
    :type network_interface_name: str
    :param ip_configuration_name: The name of the IP configuration.
    :type ip_configuration_name: str
    :param public_ip_address_name: The name of the public IP Address.
    :type public_ip_address_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param expand: Expands referenced resources.
    :type expand: str

    """
    return web.Response(status=200)


async def public_ip_addresses_list_virtual_machine_scale_set_public_ip_addresses(request: web.Request, resource_group_name, virtual_machine_scale_set_name, api_version, subscription_id) -> web.Response:
    """public_ip_addresses_list_virtual_machine_scale_set_public_ip_addresses

    Gets information about all public IP addresses on a virtual machine scale set level.

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


async def public_ip_addresses_list_virtual_machine_scale_set_vm_public_ip_addresses(request: web.Request, resource_group_name, virtual_machine_scale_set_name, virtualmachine_index, network_interface_name, ip_configuration_name, api_version, subscription_id) -> web.Response:
    """public_ip_addresses_list_virtual_machine_scale_set_vm_public_ip_addresses

    Gets information about all public IP addresses in a virtual machine IP configuration in a virtual machine scale set.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param virtual_machine_scale_set_name: The name of the virtual machine scale set.
    :type virtual_machine_scale_set_name: str
    :param virtualmachine_index: The virtual machine index.
    :type virtualmachine_index: str
    :param network_interface_name: The network interface name.
    :type network_interface_name: str
    :param ip_configuration_name: The IP configuration name.
    :type ip_configuration_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)
