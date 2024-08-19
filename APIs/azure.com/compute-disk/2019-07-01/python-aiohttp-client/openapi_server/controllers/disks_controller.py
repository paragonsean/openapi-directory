from typing import List, Dict
from aiohttp import web

from openapi_server.models.access_uri import AccessUri
from openapi_server.models.disk import Disk
from openapi_server.models.disk_list import DiskList
from openapi_server.models.disk_update import DiskUpdate
from openapi_server.models.grant_access_data import GrantAccessData
from openapi_server import util


async def disks_create_or_update(request: web.Request, subscription_id, resource_group_name, disk_name, api_version, disk) -> web.Response:
    """disks_create_or_update

    Creates or updates a disk.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param disk_name: The name of the managed disk that is being created. The name can&#39;t be changed after the disk is created. Supported characters for the name are a-z, A-Z, 0-9 and _. The maximum name length is 80 characters.
    :type disk_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param disk: Disk object supplied in the body of the Put disk operation.
    :type disk: dict | bytes

    """
    disk = Disk.from_dict(disk)
    return web.Response(status=200)


async def disks_delete(request: web.Request, subscription_id, resource_group_name, disk_name, api_version) -> web.Response:
    """disks_delete

    Deletes a disk.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param disk_name: The name of the managed disk that is being created. The name can&#39;t be changed after the disk is created. Supported characters for the name are a-z, A-Z, 0-9 and _. The maximum name length is 80 characters.
    :type disk_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def disks_get(request: web.Request, subscription_id, resource_group_name, disk_name, api_version) -> web.Response:
    """disks_get

    Gets information about a disk.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param disk_name: The name of the managed disk that is being created. The name can&#39;t be changed after the disk is created. Supported characters for the name are a-z, A-Z, 0-9 and _. The maximum name length is 80 characters.
    :type disk_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def disks_grant_access(request: web.Request, subscription_id, resource_group_name, disk_name, api_version, grant_access_data) -> web.Response:
    """disks_grant_access

    Grants access to a disk.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param disk_name: The name of the managed disk that is being created. The name can&#39;t be changed after the disk is created. Supported characters for the name are a-z, A-Z, 0-9 and _. The maximum name length is 80 characters.
    :type disk_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param grant_access_data: Access data object supplied in the body of the get disk access operation.
    :type grant_access_data: dict | bytes

    """
    grant_access_data = GrantAccessData.from_dict(grant_access_data)
    return web.Response(status=200)


async def disks_list(request: web.Request, subscription_id, api_version) -> web.Response:
    """disks_list

    Lists all the disks under a subscription.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def disks_list_by_resource_group(request: web.Request, subscription_id, resource_group_name, api_version) -> web.Response:
    """disks_list_by_resource_group

    Lists all the disks under a resource group.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def disks_revoke_access(request: web.Request, subscription_id, resource_group_name, disk_name, api_version) -> web.Response:
    """disks_revoke_access

    Revokes access to a disk.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param disk_name: The name of the managed disk that is being created. The name can&#39;t be changed after the disk is created. Supported characters for the name are a-z, A-Z, 0-9 and _. The maximum name length is 80 characters.
    :type disk_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def disks_update(request: web.Request, subscription_id, resource_group_name, disk_name, api_version, disk) -> web.Response:
    """disks_update

    Updates (patches) a disk.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param disk_name: The name of the managed disk that is being created. The name can&#39;t be changed after the disk is created. Supported characters for the name are a-z, A-Z, 0-9 and _. The maximum name length is 80 characters.
    :type disk_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param disk: Disk object supplied in the body of the Patch disk operation.
    :type disk: dict | bytes

    """
    disk = DiskUpdate.from_dict(disk)
    return web.Response(status=200)
