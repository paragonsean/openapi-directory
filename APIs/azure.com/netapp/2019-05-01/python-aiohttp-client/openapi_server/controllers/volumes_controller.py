from typing import List, Dict
from aiohttp import web

from openapi_server.models.volume import Volume
from openapi_server.models.volume_list import VolumeList
from openapi_server.models.volume_patch import VolumePatch
from openapi_server import util


async def volumes_create_or_update(request: web.Request, subscription_id, resource_group_name, account_name, pool_name, volume_name, api_version, body) -> web.Response:
    """Create or Update a volume

    Create or update the specified volume within the capacity pool

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param account_name: The name of the NetApp account
    :type account_name: str
    :param pool_name: The name of the capacity pool
    :type pool_name: str
    :param volume_name: The name of the volume
    :type volume_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param body: Volume object supplied in the body of the operation.
    :type body: dict | bytes

    """
    body = Volume.from_dict(body)
    return web.Response(status=200)


async def volumes_delete(request: web.Request, subscription_id, resource_group_name, account_name, pool_name, volume_name, api_version) -> web.Response:
    """Delete a volume

    Delete the specified volume

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param account_name: The name of the NetApp account
    :type account_name: str
    :param pool_name: The name of the capacity pool
    :type pool_name: str
    :param volume_name: The name of the volume
    :type volume_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def volumes_get(request: web.Request, subscription_id, resource_group_name, account_name, pool_name, volume_name, api_version) -> web.Response:
    """Describe a volume

    Get the details of the specified volume

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param account_name: The name of the NetApp account
    :type account_name: str
    :param pool_name: The name of the capacity pool
    :type pool_name: str
    :param volume_name: The name of the volume
    :type volume_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def volumes_list(request: web.Request, subscription_id, resource_group_name, account_name, pool_name, api_version) -> web.Response:
    """Describe all volumes

    List all volumes within the capacity pool

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param account_name: The name of the NetApp account
    :type account_name: str
    :param pool_name: The name of the capacity pool
    :type pool_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def volumes_update(request: web.Request, subscription_id, resource_group_name, account_name, pool_name, volume_name, api_version, body) -> web.Response:
    """Update a volume

    Patch the specified volume

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param account_name: The name of the NetApp account
    :type account_name: str
    :param pool_name: The name of the capacity pool
    :type pool_name: str
    :param volume_name: The name of the volume
    :type volume_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param body: Volume object supplied in the body of the operation.
    :type body: dict | bytes

    """
    body = VolumePatch.from_dict(body)
    return web.Response(status=200)
