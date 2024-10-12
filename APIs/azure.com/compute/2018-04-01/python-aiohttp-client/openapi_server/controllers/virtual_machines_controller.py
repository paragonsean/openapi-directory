from typing import List, Dict
from aiohttp import web

from openapi_server.models.virtual_machine import VirtualMachine
from openapi_server.models.virtual_machine_capture_parameters import VirtualMachineCaptureParameters
from openapi_server.models.virtual_machine_capture_result import VirtualMachineCaptureResult
from openapi_server.models.virtual_machine_instance_view import VirtualMachineInstanceView
from openapi_server.models.virtual_machine_list_result import VirtualMachineListResult
from openapi_server.models.virtual_machine_size_list_result import VirtualMachineSizeListResult
from openapi_server.models.virtual_machine_update import VirtualMachineUpdate
from openapi_server import util


async def virtual_machines_capture(request: web.Request, resource_group_name, vm_name, api_version, subscription_id, parameters) -> web.Response:
    """virtual_machines_capture

    Captures the VM by copying virtual hard disks of the VM and outputs a template that can be used to create similar VMs.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param vm_name: The name of the virtual machine.
    :type vm_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to the Capture Virtual Machine operation.
    :type parameters: dict | bytes

    """
    parameters = VirtualMachineCaptureParameters.from_dict(parameters)
    return web.Response(status=200)


async def virtual_machines_convert_to_managed_disks(request: web.Request, resource_group_name, vm_name, api_version, subscription_id) -> web.Response:
    """virtual_machines_convert_to_managed_disks

    Converts virtual machine disks from blob-based to managed disks. Virtual machine must be stop-deallocated before invoking this operation.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param vm_name: The name of the virtual machine.
    :type vm_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def virtual_machines_create_or_update(request: web.Request, resource_group_name, vm_name, api_version, subscription_id, parameters) -> web.Response:
    """virtual_machines_create_or_update

    The operation to create or update a virtual machine.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param vm_name: The name of the virtual machine.
    :type vm_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to the Create Virtual Machine operation.
    :type parameters: dict | bytes

    """
    parameters = VirtualMachine.from_dict(parameters)
    return web.Response(status=200)


async def virtual_machines_deallocate(request: web.Request, resource_group_name, vm_name, api_version, subscription_id) -> web.Response:
    """virtual_machines_deallocate

    Shuts down the virtual machine and releases the compute resources. You are not billed for the compute resources that this virtual machine uses.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param vm_name: The name of the virtual machine.
    :type vm_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def virtual_machines_delete(request: web.Request, resource_group_name, vm_name, api_version, subscription_id) -> web.Response:
    """virtual_machines_delete

    The operation to delete a virtual machine.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param vm_name: The name of the virtual machine.
    :type vm_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def virtual_machines_generalize(request: web.Request, resource_group_name, vm_name, api_version, subscription_id) -> web.Response:
    """virtual_machines_generalize

    Sets the state of the virtual machine to generalized.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param vm_name: The name of the virtual machine.
    :type vm_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def virtual_machines_get(request: web.Request, resource_group_name, vm_name, api_version, subscription_id, expand=None) -> web.Response:
    """virtual_machines_get

    Retrieves information about the model view or the instance view of a virtual machine.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param vm_name: The name of the virtual machine.
    :type vm_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param expand: The expand expression to apply on the operation.
    :type expand: str

    """
    return web.Response(status=200)


async def virtual_machines_instance_view(request: web.Request, resource_group_name, vm_name, api_version, subscription_id) -> web.Response:
    """virtual_machines_instance_view

    Retrieves information about the run-time state of a virtual machine.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param vm_name: The name of the virtual machine.
    :type vm_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def virtual_machines_list(request: web.Request, resource_group_name, api_version, subscription_id) -> web.Response:
    """virtual_machines_list

    Lists all of the virtual machines in the specified resource group. Use the nextLink property in the response to get the next page of virtual machines.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def virtual_machines_list_all(request: web.Request, api_version, subscription_id) -> web.Response:
    """virtual_machines_list_all

    Lists all of the virtual machines in the specified subscription. Use the nextLink property in the response to get the next page of virtual machines.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def virtual_machines_list_available_sizes(request: web.Request, resource_group_name, vm_name, api_version, subscription_id) -> web.Response:
    """virtual_machines_list_available_sizes

    Lists all available virtual machine sizes to which the specified virtual machine can be resized.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param vm_name: The name of the virtual machine.
    :type vm_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def virtual_machines_list_by_location(request: web.Request, location, api_version, subscription_id) -> web.Response:
    """virtual_machines_list_by_location

    Gets all the virtual machines under the specified subscription for the specified location.

    :param location: The location for which virtual machines under the subscription are queried.
    :type location: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def virtual_machines_perform_maintenance(request: web.Request, resource_group_name, vm_name, api_version, subscription_id) -> web.Response:
    """virtual_machines_perform_maintenance

    The operation to perform maintenance on a virtual machine.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param vm_name: The name of the virtual machine.
    :type vm_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def virtual_machines_power_off(request: web.Request, resource_group_name, vm_name, api_version, subscription_id) -> web.Response:
    """virtual_machines_power_off

    The operation to power off (stop) a virtual machine. The virtual machine can be restarted with the same provisioned resources. You are still charged for this virtual machine.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param vm_name: The name of the virtual machine.
    :type vm_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def virtual_machines_redeploy(request: web.Request, resource_group_name, vm_name, api_version, subscription_id) -> web.Response:
    """virtual_machines_redeploy

    Shuts down the virtual machine, moves it to a new node, and powers it back on.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param vm_name: The name of the virtual machine.
    :type vm_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def virtual_machines_restart(request: web.Request, resource_group_name, vm_name, api_version, subscription_id) -> web.Response:
    """virtual_machines_restart

    The operation to restart a virtual machine.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param vm_name: The name of the virtual machine.
    :type vm_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def virtual_machines_start(request: web.Request, resource_group_name, vm_name, api_version, subscription_id) -> web.Response:
    """virtual_machines_start

    The operation to start a virtual machine.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param vm_name: The name of the virtual machine.
    :type vm_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def virtual_machines_update(request: web.Request, resource_group_name, vm_name, api_version, subscription_id, parameters) -> web.Response:
    """virtual_machines_update

    The operation to update a virtual machine.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param vm_name: The name of the virtual machine.
    :type vm_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to the Update Virtual Machine operation.
    :type parameters: dict | bytes

    """
    parameters = VirtualMachineUpdate.from_dict(parameters)
    return web.Response(status=200)
