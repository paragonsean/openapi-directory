from typing import List, Dict
from aiohttp import web

from openapi_server.models.applicable_schedule import ApplicableSchedule
from openapi_server.models.apply_artifacts_request import ApplyArtifactsRequest
from openapi_server.models.cloud_error import CloudError
from openapi_server.models.data_disk_properties import DataDiskProperties
from openapi_server.models.detach_data_disk_properties import DetachDataDiskProperties
from openapi_server.models.lab_virtual_machine import LabVirtualMachine
from openapi_server.models.lab_virtual_machine_fragment import LabVirtualMachineFragment
from openapi_server.models.lab_virtual_machine_list import LabVirtualMachineList
from openapi_server.models.rdp_connection import RdpConnection
from openapi_server.models.resize_lab_virtual_machine_properties import ResizeLabVirtualMachineProperties
from openapi_server import util


async def virtual_machines_add_data_disk(request: web.Request, subscription_id, resource_group_name, lab_name, name, api_version, data_disk_properties) -> web.Response:
    """virtual_machines_add_data_disk

    Attach a new or existing data disk to virtual machine. This operation can take a while to complete.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param name: The name of the virtual machine.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str
    :param data_disk_properties: Request body for adding a new or existing data disk to a virtual machine.
    :type data_disk_properties: dict | bytes

    """
    data_disk_properties = DataDiskProperties.from_dict(data_disk_properties)
    return web.Response(status=200)


async def virtual_machines_apply_artifacts(request: web.Request, subscription_id, resource_group_name, lab_name, name, api_version, apply_artifacts_request) -> web.Response:
    """virtual_machines_apply_artifacts

    Apply artifacts to virtual machine. This operation can take a while to complete.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param name: The name of the virtual machine.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str
    :param apply_artifacts_request: Request body for applying artifacts to a virtual machine.
    :type apply_artifacts_request: dict | bytes

    """
    apply_artifacts_request = ApplyArtifactsRequest.from_dict(apply_artifacts_request)
    return web.Response(status=200)


async def virtual_machines_claim(request: web.Request, subscription_id, resource_group_name, lab_name, name, api_version) -> web.Response:
    """virtual_machines_claim

    Take ownership of an existing virtual machine This operation can take a while to complete.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param name: The name of the virtual machine.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def virtual_machines_create_or_update(request: web.Request, subscription_id, resource_group_name, lab_name, name, api_version, lab_virtual_machine) -> web.Response:
    """virtual_machines_create_or_update

    Create or replace an existing virtual machine. This operation can take a while to complete.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param name: The name of the virtual machine.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str
    :param lab_virtual_machine: A virtual machine.
    :type lab_virtual_machine: dict | bytes

    """
    lab_virtual_machine = LabVirtualMachine.from_dict(lab_virtual_machine)
    return web.Response(status=200)


async def virtual_machines_delete(request: web.Request, subscription_id, resource_group_name, lab_name, name, api_version) -> web.Response:
    """virtual_machines_delete

    Delete virtual machine. This operation can take a while to complete.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param name: The name of the virtual machine.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def virtual_machines_detach_data_disk(request: web.Request, subscription_id, resource_group_name, lab_name, name, api_version, detach_data_disk_properties) -> web.Response:
    """virtual_machines_detach_data_disk

    Detach the specified disk from the virtual machine. This operation can take a while to complete.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param name: The name of the virtual machine.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str
    :param detach_data_disk_properties: Request body for detaching data disk from a virtual machine.
    :type detach_data_disk_properties: dict | bytes

    """
    detach_data_disk_properties = DetachDataDiskProperties.from_dict(detach_data_disk_properties)
    return web.Response(status=200)


async def virtual_machines_get(request: web.Request, subscription_id, resource_group_name, lab_name, name, api_version, expand=None) -> web.Response:
    """virtual_machines_get

    Get virtual machine.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param name: The name of the virtual machine.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str
    :param expand: Specify the $expand query. Example: &#39;properties($expand&#x3D;artifacts,computeVm,networkInterface,applicableSchedule)&#39;
    :type expand: str

    """
    return web.Response(status=200)


async def virtual_machines_get_rdp_file_contents(request: web.Request, subscription_id, resource_group_name, lab_name, name, api_version) -> web.Response:
    """virtual_machines_get_rdp_file_contents

    Gets a string that represents the contents of the RDP file for the virtual machine

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param name: The name of the virtual machine.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def virtual_machines_list(request: web.Request, subscription_id, resource_group_name, lab_name, api_version, expand=None, filter=None, top=None, orderby=None) -> web.Response:
    """virtual_machines_list

    List virtual machines in a given lab.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param expand: Specify the $expand query. Example: &#39;properties($expand&#x3D;artifacts,computeVm,networkInterface,applicableSchedule)&#39;
    :type expand: str
    :param filter: The filter to apply to the operation. Example: &#39;$filter&#x3D;contains(name,&#39;myName&#39;)
    :type filter: str
    :param top: The maximum number of resources to return from the operation. Example: &#39;$top&#x3D;10&#39;
    :type top: int
    :param orderby: The ordering expression for the results, using OData notation. Example: &#39;$orderby&#x3D;name desc&#39;
    :type orderby: str

    """
    return web.Response(status=200)


async def virtual_machines_list_applicable_schedules(request: web.Request, subscription_id, resource_group_name, lab_name, name, api_version) -> web.Response:
    """virtual_machines_list_applicable_schedules

    Lists the applicable start/stop schedules, if any.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param name: The name of the virtual machine.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def virtual_machines_redeploy(request: web.Request, subscription_id, resource_group_name, lab_name, name, api_version) -> web.Response:
    """virtual_machines_redeploy

    Redeploy a virtual machine This operation can take a while to complete.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param name: The name of the virtual machine.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def virtual_machines_resize(request: web.Request, subscription_id, resource_group_name, lab_name, name, api_version, resize_lab_virtual_machine_properties) -> web.Response:
    """virtual_machines_resize

    Resize Virtual Machine. This operation can take a while to complete.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param name: The name of the virtual machine.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str
    :param resize_lab_virtual_machine_properties: Request body for resizing a virtual machine.
    :type resize_lab_virtual_machine_properties: dict | bytes

    """
    resize_lab_virtual_machine_properties = ResizeLabVirtualMachineProperties.from_dict(resize_lab_virtual_machine_properties)
    return web.Response(status=200)


async def virtual_machines_restart(request: web.Request, subscription_id, resource_group_name, lab_name, name, api_version) -> web.Response:
    """virtual_machines_restart

    Restart a virtual machine. This operation can take a while to complete.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param name: The name of the virtual machine.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def virtual_machines_start(request: web.Request, subscription_id, resource_group_name, lab_name, name, api_version) -> web.Response:
    """virtual_machines_start

    Start a virtual machine. This operation can take a while to complete.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param name: The name of the virtual machine.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def virtual_machines_stop(request: web.Request, subscription_id, resource_group_name, lab_name, name, api_version) -> web.Response:
    """virtual_machines_stop

    Stop a virtual machine This operation can take a while to complete.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param name: The name of the virtual machine.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def virtual_machines_transfer_disks(request: web.Request, subscription_id, resource_group_name, lab_name, name, api_version) -> web.Response:
    """virtual_machines_transfer_disks

    Transfers all data disks attached to the virtual machine to be owned by the current user. This operation can take a while to complete.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param name: The name of the virtual machine.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def virtual_machines_un_claim(request: web.Request, subscription_id, resource_group_name, lab_name, name, api_version) -> web.Response:
    """virtual_machines_un_claim

    Release ownership of an existing virtual machine This operation can take a while to complete.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param name: The name of the virtual machine.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def virtual_machines_update(request: web.Request, subscription_id, resource_group_name, lab_name, name, api_version, lab_virtual_machine) -> web.Response:
    """virtual_machines_update

    Allows modifying tags of virtual machines. All other properties will be ignored.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param name: The name of the virtual machine.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str
    :param lab_virtual_machine: A virtual machine.
    :type lab_virtual_machine: dict | bytes

    """
    lab_virtual_machine = LabVirtualMachineFragment.from_dict(lab_virtual_machine)
    return web.Response(status=200)
