from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.virtual_machine_extension import VirtualMachineExtension
from openapi_server.models.virtual_machine_extension_update import VirtualMachineExtensionUpdate
from openapi_server.models.virtual_machine_extensions_list_result import VirtualMachineExtensionsListResult
from openapi_server import util


async def virtual_machine_scale_set_vm_extensions_create_or_update(request: web.Request, resource_group_name, vm_scale_set_name, instance_id, vm_extension_name, api_version, subscription_id, extension_parameters) -> web.Response:
    """virtual_machine_scale_set_vm_extensions_create_or_update

    The operation to create or update the VMSS VM extension.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param vm_scale_set_name: The name of the VM scale set.
    :type vm_scale_set_name: str
    :param instance_id: The instance ID of the virtual machine.
    :type instance_id: str
    :param vm_extension_name: The name of the virtual machine extension.
    :type vm_extension_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param extension_parameters: Parameters supplied to the Create Virtual Machine Extension operation.
    :type extension_parameters: dict | bytes

    """
    extension_parameters = VirtualMachineExtension.from_dict(extension_parameters)
    return web.Response(status=200)


async def virtual_machine_scale_set_vm_extensions_delete(request: web.Request, resource_group_name, vm_scale_set_name, instance_id, vm_extension_name, api_version, subscription_id) -> web.Response:
    """virtual_machine_scale_set_vm_extensions_delete

    The operation to delete the VMSS VM extension.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param vm_scale_set_name: The name of the VM scale set.
    :type vm_scale_set_name: str
    :param instance_id: The instance ID of the virtual machine.
    :type instance_id: str
    :param vm_extension_name: The name of the virtual machine extension.
    :type vm_extension_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def virtual_machine_scale_set_vm_extensions_get(request: web.Request, resource_group_name, vm_scale_set_name, instance_id, vm_extension_name, api_version, subscription_id, expand=None) -> web.Response:
    """virtual_machine_scale_set_vm_extensions_get

    The operation to get the VMSS VM extension.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param vm_scale_set_name: The name of the VM scale set.
    :type vm_scale_set_name: str
    :param instance_id: The instance ID of the virtual machine.
    :type instance_id: str
    :param vm_extension_name: The name of the virtual machine extension.
    :type vm_extension_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param expand: The expand expression to apply on the operation.
    :type expand: str

    """
    return web.Response(status=200)


async def virtual_machine_scale_set_vm_extensions_list(request: web.Request, resource_group_name, vm_scale_set_name, instance_id, api_version, subscription_id, expand=None) -> web.Response:
    """virtual_machine_scale_set_vm_extensions_list

    The operation to get all extensions of an instance in Virtual Machine Scaleset.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param vm_scale_set_name: The name of the VM scale set.
    :type vm_scale_set_name: str
    :param instance_id: The instance ID of the virtual machine.
    :type instance_id: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param expand: The expand expression to apply on the operation.
    :type expand: str

    """
    return web.Response(status=200)


async def virtual_machine_scale_set_vm_extensions_update(request: web.Request, resource_group_name, vm_scale_set_name, instance_id, vm_extension_name, api_version, subscription_id, extension_parameters) -> web.Response:
    """virtual_machine_scale_set_vm_extensions_update

    The operation to update the VMSS VM extension.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param vm_scale_set_name: The name of the VM scale set.
    :type vm_scale_set_name: str
    :param instance_id: The instance ID of the virtual machine.
    :type instance_id: str
    :param vm_extension_name: The name of the virtual machine extension.
    :type vm_extension_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param extension_parameters: Parameters supplied to the Update Virtual Machine Extension operation.
    :type extension_parameters: dict | bytes

    """
    extension_parameters = VirtualMachineExtensionUpdate.from_dict(extension_parameters)
    return web.Response(status=200)
