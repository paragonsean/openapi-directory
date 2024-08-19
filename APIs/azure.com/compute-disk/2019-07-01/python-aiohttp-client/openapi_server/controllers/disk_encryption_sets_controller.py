from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.disk_encryption_set import DiskEncryptionSet
from openapi_server.models.disk_encryption_set_list import DiskEncryptionSetList
from openapi_server.models.disk_encryption_set_update import DiskEncryptionSetUpdate
from openapi_server import util


async def disk_encryption_sets_create_or_update(request: web.Request, subscription_id, resource_group_name, disk_encryption_set_name, api_version, disk_encryption_set) -> web.Response:
    """disk_encryption_sets_create_or_update

    Creates or updates a disk encryption set

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param disk_encryption_set_name: The name of the disk encryption set that is being created. The name can&#39;t be changed after the disk encryption set is created. Supported characters for the name are a-z, A-Z, 0-9 and _. The maximum name length is 80 characters.
    :type disk_encryption_set_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param disk_encryption_set: disk encryption set object supplied in the body of the Put disk encryption set operation.
    :type disk_encryption_set: dict | bytes

    """
    disk_encryption_set = DiskEncryptionSet.from_dict(disk_encryption_set)
    return web.Response(status=200)


async def disk_encryption_sets_delete(request: web.Request, subscription_id, resource_group_name, disk_encryption_set_name, api_version) -> web.Response:
    """disk_encryption_sets_delete

    Deletes a disk encryption set.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param disk_encryption_set_name: The name of the disk encryption set that is being created. The name can&#39;t be changed after the disk encryption set is created. Supported characters for the name are a-z, A-Z, 0-9 and _. The maximum name length is 80 characters.
    :type disk_encryption_set_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def disk_encryption_sets_get(request: web.Request, subscription_id, resource_group_name, disk_encryption_set_name, api_version) -> web.Response:
    """disk_encryption_sets_get

    Gets information about a disk encryption set.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param disk_encryption_set_name: The name of the disk encryption set that is being created. The name can&#39;t be changed after the disk encryption set is created. Supported characters for the name are a-z, A-Z, 0-9 and _. The maximum name length is 80 characters.
    :type disk_encryption_set_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def disk_encryption_sets_list(request: web.Request, subscription_id, api_version) -> web.Response:
    """disk_encryption_sets_list

    Lists all the disk encryption sets under a subscription.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def disk_encryption_sets_list_by_resource_group(request: web.Request, subscription_id, resource_group_name, api_version) -> web.Response:
    """disk_encryption_sets_list_by_resource_group

    Lists all the disk encryption sets under a resource group.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def disk_encryption_sets_update(request: web.Request, subscription_id, resource_group_name, disk_encryption_set_name, api_version, disk_encryption_set) -> web.Response:
    """disk_encryption_sets_update

    Updates (patches) a disk encryption set.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param disk_encryption_set_name: The name of the disk encryption set that is being created. The name can&#39;t be changed after the disk encryption set is created. Supported characters for the name are a-z, A-Z, 0-9 and _. The maximum name length is 80 characters.
    :type disk_encryption_set_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param disk_encryption_set: disk encryption set object supplied in the body of the Patch disk encryption set operation.
    :type disk_encryption_set: dict | bytes

    """
    disk_encryption_set = DiskEncryptionSetUpdate.from_dict(disk_encryption_set)
    return web.Response(status=200)
