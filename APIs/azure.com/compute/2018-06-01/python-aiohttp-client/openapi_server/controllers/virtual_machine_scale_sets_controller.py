from typing import List, Dict
from aiohttp import web

from openapi_server.models.recovery_walk_response import RecoveryWalkResponse
from openapi_server.models.virtual_machine_scale_set import VirtualMachineScaleSet
from openapi_server.models.virtual_machine_scale_set_instance_view import VirtualMachineScaleSetInstanceView
from openapi_server.models.virtual_machine_scale_set_list_os_upgrade_history import VirtualMachineScaleSetListOSUpgradeHistory
from openapi_server.models.virtual_machine_scale_set_list_result import VirtualMachineScaleSetListResult
from openapi_server.models.virtual_machine_scale_set_list_skus_result import VirtualMachineScaleSetListSkusResult
from openapi_server.models.virtual_machine_scale_set_list_with_link_result import VirtualMachineScaleSetListWithLinkResult
from openapi_server.models.virtual_machine_scale_set_reimage_parameters import VirtualMachineScaleSetReimageParameters
from openapi_server.models.virtual_machine_scale_set_update import VirtualMachineScaleSetUpdate
from openapi_server.models.virtual_machine_scale_set_vm_instance_ids import VirtualMachineScaleSetVMInstanceIDs
from openapi_server.models.virtual_machine_scale_set_vm_instance_required_ids import VirtualMachineScaleSetVMInstanceRequiredIDs
from openapi_server import util


async def virtual_machine_scale_sets_create_or_update(request: web.Request, resource_group_name, vm_scale_set_name, api_version, subscription_id, parameters) -> web.Response:
    """virtual_machine_scale_sets_create_or_update

    Create or update a VM scale set.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param vm_scale_set_name: The name of the VM scale set to create or update.
    :type vm_scale_set_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: The scale set object.
    :type parameters: dict | bytes

    """
    parameters = VirtualMachineScaleSet.from_dict(parameters)
    return web.Response(status=200)


async def virtual_machine_scale_sets_deallocate(request: web.Request, resource_group_name, vm_scale_set_name, api_version, subscription_id, vm_instance_ids=None) -> web.Response:
    """virtual_machine_scale_sets_deallocate

    Deallocates specific virtual machines in a VM scale set. Shuts down the virtual machines and releases the compute resources. You are not billed for the compute resources that this virtual machine scale set deallocates.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param vm_scale_set_name: The name of the VM scale set.
    :type vm_scale_set_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param vm_instance_ids: A list of virtual machine instance IDs from the VM scale set.
    :type vm_instance_ids: dict | bytes

    """
    vm_instance_ids = VirtualMachineScaleSetVMInstanceIDs.from_dict(vm_instance_ids)
    return web.Response(status=200)


async def virtual_machine_scale_sets_delete(request: web.Request, resource_group_name, vm_scale_set_name, api_version, subscription_id) -> web.Response:
    """virtual_machine_scale_sets_delete

    Deletes a VM scale set.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param vm_scale_set_name: The name of the VM scale set.
    :type vm_scale_set_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def virtual_machine_scale_sets_delete_instances(request: web.Request, resource_group_name, vm_scale_set_name, api_version, subscription_id, vm_instance_ids) -> web.Response:
    """virtual_machine_scale_sets_delete_instances

    Deletes virtual machines in a VM scale set.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param vm_scale_set_name: The name of the VM scale set.
    :type vm_scale_set_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param vm_instance_ids: A list of virtual machine instance IDs from the VM scale set.
    :type vm_instance_ids: dict | bytes

    """
    vm_instance_ids = VirtualMachineScaleSetVMInstanceRequiredIDs.from_dict(vm_instance_ids)
    return web.Response(status=200)


async def virtual_machine_scale_sets_force_recovery_service_fabric_platform_update_domain_walk(request: web.Request, resource_group_name, vm_scale_set_name, api_version, subscription_id, platform_update_domain) -> web.Response:
    """virtual_machine_scale_sets_force_recovery_service_fabric_platform_update_domain_walk

    Manual platform update domain walk to update virtual machines in a service fabric virtual machine scale set.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param vm_scale_set_name: The name of the VM scale set.
    :type vm_scale_set_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param platform_update_domain: The platform update domain for which a manual recovery walk is requested
    :type platform_update_domain: int

    """
    return web.Response(status=200)


async def virtual_machine_scale_sets_get(request: web.Request, resource_group_name, vm_scale_set_name, api_version, subscription_id) -> web.Response:
    """virtual_machine_scale_sets_get

    Display information about a virtual machine scale set.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param vm_scale_set_name: The name of the VM scale set.
    :type vm_scale_set_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def virtual_machine_scale_sets_get_instance_view(request: web.Request, resource_group_name, vm_scale_set_name, api_version, subscription_id) -> web.Response:
    """virtual_machine_scale_sets_get_instance_view

    Gets the status of a VM scale set instance.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param vm_scale_set_name: The name of the VM scale set.
    :type vm_scale_set_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def virtual_machine_scale_sets_get_os_upgrade_history(request: web.Request, resource_group_name, vm_scale_set_name, api_version, subscription_id) -> web.Response:
    """virtual_machine_scale_sets_get_os_upgrade_history

    Gets list of OS upgrades on a VM scale set instance.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param vm_scale_set_name: The name of the VM scale set.
    :type vm_scale_set_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def virtual_machine_scale_sets_list(request: web.Request, resource_group_name, api_version, subscription_id) -> web.Response:
    """virtual_machine_scale_sets_list

    Gets a list of all VM scale sets under a resource group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def virtual_machine_scale_sets_list_all(request: web.Request, api_version, subscription_id) -> web.Response:
    """virtual_machine_scale_sets_list_all

    Gets a list of all VM Scale Sets in the subscription, regardless of the associated resource group. Use nextLink property in the response to get the next page of VM Scale Sets. Do this till nextLink is null to fetch all the VM Scale Sets.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def virtual_machine_scale_sets_list_skus(request: web.Request, resource_group_name, vm_scale_set_name, api_version, subscription_id) -> web.Response:
    """virtual_machine_scale_sets_list_skus

    Gets a list of SKUs available for your VM scale set, including the minimum and maximum VM instances allowed for each SKU.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param vm_scale_set_name: The name of the VM scale set.
    :type vm_scale_set_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def virtual_machine_scale_sets_perform_maintenance(request: web.Request, resource_group_name, vm_scale_set_name, api_version, subscription_id, vm_instance_ids=None) -> web.Response:
    """virtual_machine_scale_sets_perform_maintenance

    Perform maintenance on one or more virtual machines in a VM scale set. Operation on instances which are not eligible for perform maintenance will be failed. Please refer to best practices for more details: https://docs.microsoft.com/en-us/azure/virtual-machine-scale-sets/virtual-machine-scale-sets-maintenance-notifications

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param vm_scale_set_name: The name of the VM scale set.
    :type vm_scale_set_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param vm_instance_ids: A list of virtual machine instance IDs from the VM scale set.
    :type vm_instance_ids: dict | bytes

    """
    vm_instance_ids = VirtualMachineScaleSetVMInstanceIDs.from_dict(vm_instance_ids)
    return web.Response(status=200)


async def virtual_machine_scale_sets_power_off(request: web.Request, resource_group_name, vm_scale_set_name, api_version, subscription_id, vm_instance_ids=None) -> web.Response:
    """virtual_machine_scale_sets_power_off

    Power off (stop) one or more virtual machines in a VM scale set. Note that resources are still attached and you are getting charged for the resources. Instead, use deallocate to release resources and avoid charges.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param vm_scale_set_name: The name of the VM scale set.
    :type vm_scale_set_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param vm_instance_ids: A list of virtual machine instance IDs from the VM scale set.
    :type vm_instance_ids: dict | bytes

    """
    vm_instance_ids = VirtualMachineScaleSetVMInstanceIDs.from_dict(vm_instance_ids)
    return web.Response(status=200)


async def virtual_machine_scale_sets_redeploy(request: web.Request, resource_group_name, vm_scale_set_name, api_version, subscription_id, vm_instance_ids=None) -> web.Response:
    """virtual_machine_scale_sets_redeploy

    Shuts down all the virtual machines in the virtual machine scale set, moves them to a new node, and powers them back on.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param vm_scale_set_name: The name of the VM scale set.
    :type vm_scale_set_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param vm_instance_ids: A list of virtual machine instance IDs from the VM scale set.
    :type vm_instance_ids: dict | bytes

    """
    vm_instance_ids = VirtualMachineScaleSetVMInstanceIDs.from_dict(vm_instance_ids)
    return web.Response(status=200)


async def virtual_machine_scale_sets_reimage(request: web.Request, resource_group_name, vm_scale_set_name, api_version, subscription_id, vm_scale_set_reimage_input=None) -> web.Response:
    """virtual_machine_scale_sets_reimage

    Reimages (upgrade the operating system) one or more virtual machines in a VM scale set which don&#39;t have a ephemeral OS disk, for virtual machines who have a ephemeral OS disk the virtual machine is reset to initial state.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param vm_scale_set_name: The name of the VM scale set.
    :type vm_scale_set_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param vm_scale_set_reimage_input: Parameters for Reimaging VM ScaleSet.
    :type vm_scale_set_reimage_input: dict | bytes

    """
    vm_scale_set_reimage_input = VirtualMachineScaleSetReimageParameters.from_dict(vm_scale_set_reimage_input)
    return web.Response(status=200)


async def virtual_machine_scale_sets_reimage_all(request: web.Request, resource_group_name, vm_scale_set_name, api_version, subscription_id, vm_instance_ids=None) -> web.Response:
    """virtual_machine_scale_sets_reimage_all

    Reimages all the disks ( including data disks ) in the virtual machines in a VM scale set. This operation is only supported for managed disks.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param vm_scale_set_name: The name of the VM scale set.
    :type vm_scale_set_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param vm_instance_ids: A list of virtual machine instance IDs from the VM scale set.
    :type vm_instance_ids: dict | bytes

    """
    vm_instance_ids = VirtualMachineScaleSetVMInstanceIDs.from_dict(vm_instance_ids)
    return web.Response(status=200)


async def virtual_machine_scale_sets_restart(request: web.Request, resource_group_name, vm_scale_set_name, api_version, subscription_id, vm_instance_ids=None) -> web.Response:
    """virtual_machine_scale_sets_restart

    Restarts one or more virtual machines in a VM scale set.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param vm_scale_set_name: The name of the VM scale set.
    :type vm_scale_set_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param vm_instance_ids: A list of virtual machine instance IDs from the VM scale set.
    :type vm_instance_ids: dict | bytes

    """
    vm_instance_ids = VirtualMachineScaleSetVMInstanceIDs.from_dict(vm_instance_ids)
    return web.Response(status=200)


async def virtual_machine_scale_sets_start(request: web.Request, resource_group_name, vm_scale_set_name, api_version, subscription_id, vm_instance_ids=None) -> web.Response:
    """virtual_machine_scale_sets_start

    Starts one or more virtual machines in a VM scale set.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param vm_scale_set_name: The name of the VM scale set.
    :type vm_scale_set_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param vm_instance_ids: A list of virtual machine instance IDs from the VM scale set.
    :type vm_instance_ids: dict | bytes

    """
    vm_instance_ids = VirtualMachineScaleSetVMInstanceIDs.from_dict(vm_instance_ids)
    return web.Response(status=200)


async def virtual_machine_scale_sets_update(request: web.Request, resource_group_name, vm_scale_set_name, api_version, subscription_id, parameters) -> web.Response:
    """virtual_machine_scale_sets_update

    Update a VM scale set.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param vm_scale_set_name: The name of the VM scale set to create or update.
    :type vm_scale_set_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: The scale set object.
    :type parameters: dict | bytes

    """
    parameters = VirtualMachineScaleSetUpdate.from_dict(parameters)
    return web.Response(status=200)


async def virtual_machine_scale_sets_update_instances(request: web.Request, resource_group_name, vm_scale_set_name, api_version, subscription_id, vm_instance_ids) -> web.Response:
    """virtual_machine_scale_sets_update_instances

    Upgrades one or more virtual machines to the latest SKU set in the VM scale set model.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param vm_scale_set_name: The name of the VM scale set.
    :type vm_scale_set_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param vm_instance_ids: A list of virtual machine instance IDs from the VM scale set.
    :type vm_instance_ids: dict | bytes

    """
    vm_instance_ids = VirtualMachineScaleSetVMInstanceRequiredIDs.from_dict(vm_instance_ids)
    return web.Response(status=200)
