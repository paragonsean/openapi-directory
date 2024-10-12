from typing import List, Dict
from aiohttp import web

from openapi_server.models.apply_artifacts_request import ApplyArtifactsRequest
from openapi_server.models.cloud_error import CloudError
from openapi_server.models.lab_virtual_machine import LabVirtualMachine
from openapi_server.models.response_with_continuation_lab_virtual_machine import ResponseWithContinuationLabVirtualMachine
from openapi_server import util


async def virtual_machine_apply_artifacts(request: web.Request, subscription_id, resource_group_name, lab_name, name, api_version, apply_artifacts_request) -> web.Response:
    """virtual_machine_apply_artifacts

    Apply artifacts to Lab VM. This operation can take a while to complete.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param name: The name of the virtual Machine.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str
    :param apply_artifacts_request: 
    :type apply_artifacts_request: dict | bytes

    """
    apply_artifacts_request = ApplyArtifactsRequest.from_dict(apply_artifacts_request)
    return web.Response(status=200)


async def virtual_machine_create_or_update_resource(request: web.Request, subscription_id, resource_group_name, lab_name, name, api_version, lab_virtual_machine) -> web.Response:
    """virtual_machine_create_or_update_resource

    Create or replace an existing Virtual Machine. This operation can take a while to complete.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param name: The name of the virtual Machine.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str
    :param lab_virtual_machine: 
    :type lab_virtual_machine: dict | bytes

    """
    lab_virtual_machine = LabVirtualMachine.from_dict(lab_virtual_machine)
    return web.Response(status=200)


async def virtual_machine_delete_resource(request: web.Request, subscription_id, resource_group_name, lab_name, name, api_version) -> web.Response:
    """virtual_machine_delete_resource

    Delete virtual machine. This operation can take a while to complete.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param name: The name of the virtual Machine.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def virtual_machine_get_resource(request: web.Request, subscription_id, resource_group_name, lab_name, name, api_version) -> web.Response:
    """virtual_machine_get_resource

    Get virtual machine.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param name: The name of the virtual Machine.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def virtual_machine_list(request: web.Request, subscription_id, resource_group_name, lab_name, api_version, filter=None, top=None, order_by=None) -> web.Response:
    """virtual_machine_list

    List virtual machines.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param filter: The filter to apply on the operation.
    :type filter: str
    :param top: 
    :type top: int
    :param order_by: 
    :type order_by: str

    """
    return web.Response(status=200)


async def virtual_machine_patch_resource(request: web.Request, subscription_id, resource_group_name, lab_name, name, api_version, lab_virtual_machine) -> web.Response:
    """virtual_machine_patch_resource

    Modify properties of virtual machines.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param name: The name of the virtual Machine.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str
    :param lab_virtual_machine: 
    :type lab_virtual_machine: dict | bytes

    """
    lab_virtual_machine = LabVirtualMachine.from_dict(lab_virtual_machine)
    return web.Response(status=200)


async def virtual_machine_start(request: web.Request, subscription_id, resource_group_name, lab_name, name, api_version) -> web.Response:
    """virtual_machine_start

    Start a Lab VM. This operation can take a while to complete.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param name: The name of the virtual Machine.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def virtual_machine_stop(request: web.Request, subscription_id, resource_group_name, lab_name, name, api_version) -> web.Response:
    """virtual_machine_stop

    Stop a Lab VM. This operation can take a while to complete.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param name: The name of the virtual Machine.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)
