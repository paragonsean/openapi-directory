from typing import List, Dict
from aiohttp import web

from openapi_server.models.virtual_machine_scale_set_extension import VirtualMachineScaleSetExtension
from openapi_server.models.virtual_machine_scale_set_extension_list_result import VirtualMachineScaleSetExtensionListResult
from openapi_server.models.virtual_machine_scale_set_extension_update import VirtualMachineScaleSetExtensionUpdate
from openapi_server import util


async def virtual_machine_scale_set_extensions_create_or_update(request: web.Request, resource_group_name, vm_scale_set_name, vmss_extension_name, api_version, subscription_id, extension_parameters) -> web.Response:
    """virtual_machine_scale_set_extensions_create_or_update

    The operation to create or update an extension.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param vm_scale_set_name: The name of the VM scale set where the extension should be create or updated.
    :type vm_scale_set_name: str
    :param vmss_extension_name: The name of the VM scale set extension.
    :type vmss_extension_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param extension_parameters: Parameters supplied to the Create VM scale set Extension operation.
    :type extension_parameters: dict | bytes

    """
    extension_parameters = VirtualMachineScaleSetExtension.from_dict(extension_parameters)
    return web.Response(status=200)


async def virtual_machine_scale_set_extensions_delete(request: web.Request, resource_group_name, vm_scale_set_name, vmss_extension_name, api_version, subscription_id) -> web.Response:
    """virtual_machine_scale_set_extensions_delete

    The operation to delete the extension.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param vm_scale_set_name: The name of the VM scale set where the extension should be deleted.
    :type vm_scale_set_name: str
    :param vmss_extension_name: The name of the VM scale set extension.
    :type vmss_extension_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def virtual_machine_scale_set_extensions_get(request: web.Request, resource_group_name, vm_scale_set_name, vmss_extension_name, api_version, subscription_id, expand=None) -> web.Response:
    """virtual_machine_scale_set_extensions_get

    The operation to get the extension.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param vm_scale_set_name: The name of the VM scale set containing the extension.
    :type vm_scale_set_name: str
    :param vmss_extension_name: The name of the VM scale set extension.
    :type vmss_extension_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param expand: The expand expression to apply on the operation.
    :type expand: str

    """
    return web.Response(status=200)


async def virtual_machine_scale_set_extensions_list(request: web.Request, resource_group_name, vm_scale_set_name, api_version, subscription_id) -> web.Response:
    """virtual_machine_scale_set_extensions_list

    Gets a list of all extensions in a VM scale set.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param vm_scale_set_name: The name of the VM scale set containing the extension.
    :type vm_scale_set_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def virtual_machine_scale_set_extensions_update(request: web.Request, resource_group_name, vm_scale_set_name, vmss_extension_name, api_version, subscription_id, extension_parameters) -> web.Response:
    """virtual_machine_scale_set_extensions_update

    The operation to update an extension.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param vm_scale_set_name: The name of the VM scale set where the extension should be updated.
    :type vm_scale_set_name: str
    :param vmss_extension_name: The name of the VM scale set extension.
    :type vmss_extension_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param extension_parameters: Parameters supplied to the Update VM scale set Extension operation.
    :type extension_parameters: dict | bytes

    """
    extension_parameters = VirtualMachineScaleSetExtensionUpdate.from_dict(extension_parameters)
    return web.Response(status=200)
