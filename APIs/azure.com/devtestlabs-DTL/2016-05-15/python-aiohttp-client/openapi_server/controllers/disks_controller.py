from typing import List, Dict
from aiohttp import web

from openapi_server.models.attach_disk_properties import AttachDiskProperties
from openapi_server.models.cloud_error import CloudError
from openapi_server.models.detach_disk_properties import DetachDiskProperties
from openapi_server.models.disk import Disk
from openapi_server.models.response_with_continuation_disk import ResponseWithContinuationDisk
from openapi_server import util


async def disks_attach(request: web.Request, subscription_id, resource_group_name, lab_name, user_name, name, api_version, attach_disk_properties) -> web.Response:
    """disks_attach

    Attach and create the lease of the disk to the virtual machine. This operation can take a while to complete.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param user_name: The name of the user profile.
    :type user_name: str
    :param name: The name of the disk.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str
    :param attach_disk_properties: Properties of the disk to attach.
    :type attach_disk_properties: dict | bytes

    """
    attach_disk_properties = AttachDiskProperties.from_dict(attach_disk_properties)
    return web.Response(status=200)


async def disks_create_or_update(request: web.Request, subscription_id, resource_group_name, lab_name, user_name, name, api_version, disk) -> web.Response:
    """disks_create_or_update

    Create or replace an existing disk. This operation can take a while to complete.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param user_name: The name of the user profile.
    :type user_name: str
    :param name: The name of the disk.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str
    :param disk: A Disk.
    :type disk: dict | bytes

    """
    disk = Disk.from_dict(disk)
    return web.Response(status=200)


async def disks_delete(request: web.Request, subscription_id, resource_group_name, lab_name, user_name, name, api_version) -> web.Response:
    """disks_delete

    Delete disk. This operation can take a while to complete.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param user_name: The name of the user profile.
    :type user_name: str
    :param name: The name of the disk.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def disks_detach(request: web.Request, subscription_id, resource_group_name, lab_name, user_name, name, api_version, detach_disk_properties) -> web.Response:
    """disks_detach

    Detach and break the lease of the disk attached to the virtual machine. This operation can take a while to complete.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param user_name: The name of the user profile.
    :type user_name: str
    :param name: The name of the disk.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str
    :param detach_disk_properties: Properties of the disk to detach.
    :type detach_disk_properties: dict | bytes

    """
    detach_disk_properties = DetachDiskProperties.from_dict(detach_disk_properties)
    return web.Response(status=200)


async def disks_get(request: web.Request, subscription_id, resource_group_name, lab_name, user_name, name, api_version, expand=None) -> web.Response:
    """disks_get

    Get disk.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param user_name: The name of the user profile.
    :type user_name: str
    :param name: The name of the disk.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str
    :param expand: Specify the $expand query. Example: &#39;properties($select&#x3D;diskType)&#39;
    :type expand: str

    """
    return web.Response(status=200)


async def disks_list(request: web.Request, subscription_id, resource_group_name, lab_name, user_name, api_version, expand=None, filter=None, top=None, orderby=None) -> web.Response:
    """disks_list

    List disks in a given user profile.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param user_name: The name of the user profile.
    :type user_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param expand: Specify the $expand query. Example: &#39;properties($select&#x3D;diskType)&#39;
    :type expand: str
    :param filter: The filter to apply to the operation.
    :type filter: str
    :param top: The maximum number of resources to return from the operation.
    :type top: int
    :param orderby: The ordering expression for the results, using OData notation.
    :type orderby: str

    """
    return web.Response(status=200)
