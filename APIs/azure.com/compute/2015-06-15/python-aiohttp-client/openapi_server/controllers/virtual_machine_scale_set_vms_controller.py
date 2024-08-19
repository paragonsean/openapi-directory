from typing import List, Dict
from aiohttp import web

from openapi_server.models.operation_status_response import OperationStatusResponse
from openapi_server.models.virtual_machine_scale_set_vm import VirtualMachineScaleSetVM
from openapi_server.models.virtual_machine_scale_set_vm_instance_view import VirtualMachineScaleSetVMInstanceView
from openapi_server.models.virtual_machine_scale_set_vm_list_result import VirtualMachineScaleSetVMListResult
from openapi_server import util


async def virtual_machine_scale_set_vms_deallocate(request: web.Request, resource_group_name, vm_scale_set_name, instance_id, api_version, subscription_id) -> web.Response:
    """virtual_machine_scale_set_vms_deallocate

    Deallocates a specific virtual machine in a VM scale set. Shuts down the virtual machine and releases the compute resources it uses. You are not billed for the compute resources of this virtual machine once it is deallocated.

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

    """
    return web.Response(status=200)


async def virtual_machine_scale_set_vms_delete(request: web.Request, resource_group_name, vm_scale_set_name, instance_id, api_version, subscription_id) -> web.Response:
    """virtual_machine_scale_set_vms_delete

    Deletes a virtual machine from a VM scale set.

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

    """
    return web.Response(status=200)


async def virtual_machine_scale_set_vms_get(request: web.Request, resource_group_name, vm_scale_set_name, instance_id, api_version, subscription_id) -> web.Response:
    """virtual_machine_scale_set_vms_get

    Gets a virtual machine from a VM scale set.

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

    """
    return web.Response(status=200)


async def virtual_machine_scale_set_vms_get_instance_view(request: web.Request, resource_group_name, vm_scale_set_name, instance_id, api_version, subscription_id) -> web.Response:
    """virtual_machine_scale_set_vms_get_instance_view

    Gets the status of a virtual machine from a VM scale set.

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

    """
    return web.Response(status=200)


async def virtual_machine_scale_set_vms_list(request: web.Request, resource_group_name, virtual_machine_scale_set_name, api_version, subscription_id, filter=None, select=None, expand=None) -> web.Response:
    """virtual_machine_scale_set_vms_list

    Gets a list of all virtual machines in a VM scale sets.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param virtual_machine_scale_set_name: The name of the VM scale set.
    :type virtual_machine_scale_set_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param filter: The filter to apply to the operation.
    :type filter: str
    :param select: The list parameters.
    :type select: str
    :param expand: The expand expression to apply to the operation.
    :type expand: str

    """
    return web.Response(status=200)


async def virtual_machine_scale_set_vms_power_off(request: web.Request, resource_group_name, vm_scale_set_name, instance_id, api_version, subscription_id) -> web.Response:
    """virtual_machine_scale_set_vms_power_off

    Power off (stop) a virtual machine in a VM scale set. Note that resources are still attached and you are getting charged for the resources. Instead, use deallocate to release resources and avoid charges.

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

    """
    return web.Response(status=200)


async def virtual_machine_scale_set_vms_reimage(request: web.Request, resource_group_name, vm_scale_set_name, instance_id, api_version, subscription_id) -> web.Response:
    """virtual_machine_scale_set_vms_reimage

    Reimages (upgrade the operating system) a specific virtual machine in a VM scale set.

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

    """
    return web.Response(status=200)


async def virtual_machine_scale_set_vms_restart(request: web.Request, resource_group_name, vm_scale_set_name, instance_id, api_version, subscription_id) -> web.Response:
    """virtual_machine_scale_set_vms_restart

    Restarts a virtual machine in a VM scale set.

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

    """
    return web.Response(status=200)


async def virtual_machine_scale_set_vms_start(request: web.Request, resource_group_name, vm_scale_set_name, instance_id, api_version, subscription_id) -> web.Response:
    """virtual_machine_scale_set_vms_start

    Starts a virtual machine in a VM scale set.

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

    """
    return web.Response(status=200)
