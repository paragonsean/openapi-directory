from typing import List, Dict
from aiohttp import web

from openapi_server.models.csrp_error import CSRPError
from openapi_server.models.patch_payload import PatchPayload
from openapi_server.models.virtual_machine import VirtualMachine
from openapi_server.models.virtual_machine_list_response import VirtualMachineListResponse
from openapi_server.models.virtual_machine_stop_mode import VirtualMachineStopMode
from openapi_server import util


async def virtual_machines_create_or_update(request: web.Request, subscription_id, resource_group_name, referer, virtual_machine_name, api_version, virtual_machine_request) -> web.Response:
    """Implements virtual machine PUT method

    Create Or Update Virtual Machine

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group
    :type resource_group_name: str
    :param referer: referer url
    :type referer: str
    :param virtual_machine_name: virtual machine name
    :type virtual_machine_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param virtual_machine_request: Create or Update Virtual Machine request
    :type virtual_machine_request: dict | bytes

    """
    virtual_machine_request = VirtualMachine.from_dict(virtual_machine_request)
    return web.Response(status=200)


async def virtual_machines_delete(request: web.Request, subscription_id, resource_group_name, referer, virtual_machine_name, api_version) -> web.Response:
    """Implements virtual machine DELETE method

    Delete virtual machine

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group
    :type resource_group_name: str
    :param referer: referer url
    :type referer: str
    :param virtual_machine_name: virtual machine name
    :type virtual_machine_name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def virtual_machines_get(request: web.Request, subscription_id, resource_group_name, virtual_machine_name, api_version) -> web.Response:
    """Implements virtual machine GET method

    Get virtual machine

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group
    :type resource_group_name: str
    :param virtual_machine_name: virtual machine name
    :type virtual_machine_name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def virtual_machines_list_by_resource_group(request: web.Request, subscription_id, resource_group_name, api_version, filter=None, top=None, skip_token=None) -> web.Response:
    """Implements list virtual machine within RG method

    Returns list of virtual machine within resource group

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group
    :type resource_group_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param filter: The filter to apply on the list operation
    :type filter: str
    :param top: The maximum number of record sets to return
    :type top: int
    :param skip_token: to be used by nextLink implementation
    :type skip_token: str

    """
    return web.Response(status=200)


async def virtual_machines_list_by_subscription(request: web.Request, subscription_id, api_version, filter=None, top=None, skip_token=None) -> web.Response:
    """Implements list virtual machine within subscription method

    Returns list virtual machine within subscription

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param api_version: Client API version.
    :type api_version: str
    :param filter: The filter to apply on the list operation
    :type filter: str
    :param top: The maximum number of record sets to return
    :type top: int
    :param skip_token: to be used by nextLink implementation
    :type skip_token: str

    """
    return web.Response(status=200)


async def virtual_machines_start(request: web.Request, subscription_id, resource_group_name, referer, virtual_machine_name, api_version) -> web.Response:
    """Implements a start method for a virtual machine

    Power on virtual machine

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group
    :type resource_group_name: str
    :param referer: referer url
    :type referer: str
    :param virtual_machine_name: virtual machine name
    :type virtual_machine_name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def virtual_machines_stop(request: web.Request, subscription_id, resource_group_name, referer, virtual_machine_name, api_version, mode=None, m=None) -> web.Response:
    """Implements shutdown, poweroff, and suspend method for a virtual machine

    Power off virtual machine, options: shutdown, poweroff, and suspend

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group
    :type resource_group_name: str
    :param referer: referer url
    :type referer: str
    :param virtual_machine_name: virtual machine name
    :type virtual_machine_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param mode: query stop mode parameter (reboot, shutdown, etc...)
    :type mode: str
    :param m: body stop mode parameter (reboot, shutdown, etc...)
    :type m: dict | bytes

    """
    m = VirtualMachineStopMode.from_dict(m)
    return web.Response(status=200)


async def virtual_machines_update(request: web.Request, subscription_id, resource_group_name, virtual_machine_name, api_version, virtual_machine_request) -> web.Response:
    """Implements virtual machine PATCH method

    Patch virtual machine properties

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group
    :type resource_group_name: str
    :param virtual_machine_name: virtual machine name
    :type virtual_machine_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param virtual_machine_request: Patch virtual machine request
    :type virtual_machine_request: dict | bytes

    """
    virtual_machine_request = PatchPayload.from_dict(virtual_machine_request)
    return web.Response(status=200)
