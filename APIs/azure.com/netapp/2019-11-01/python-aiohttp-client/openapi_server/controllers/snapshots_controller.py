from typing import List, Dict
from aiohttp import web

from openapi_server.models.snapshot import Snapshot
from openapi_server.models.snapshots_list import SnapshotsList
from openapi_server import util


async def snapshots_create(request: web.Request, subscription_id, resource_group_name, account_name, pool_name, volume_name, snapshot_name, api_version, body) -> web.Response:
    """Create a snapshot

    Create the specified snapshot within the given volume

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
    :param snapshot_name: The name of the mount target
    :type snapshot_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param body: Snapshot object supplied in the body of the operation.
    :type body: dict | bytes

    """
    body = Snapshot.from_dict(body)
    return web.Response(status=200)


async def snapshots_delete(request: web.Request, subscription_id, resource_group_name, account_name, pool_name, volume_name, snapshot_name, api_version) -> web.Response:
    """Delete a snapshot

    Delete snapshot

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
    :param snapshot_name: The name of the mount target
    :type snapshot_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def snapshots_get(request: web.Request, subscription_id, resource_group_name, account_name, pool_name, volume_name, snapshot_name, api_version) -> web.Response:
    """Describe a snapshot

    Get details of the specified snapshot

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
    :param snapshot_name: The name of the mount target
    :type snapshot_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def snapshots_list(request: web.Request, subscription_id, resource_group_name, account_name, pool_name, volume_name, api_version) -> web.Response:
    """Describe all snapshots

    List all snapshots associated with the volume

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


async def snapshots_update(request: web.Request, subscription_id, resource_group_name, account_name, pool_name, volume_name, snapshot_name, api_version, body) -> web.Response:
    """Update a snapshot

    Patch a snapshot

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
    :param snapshot_name: The name of the mount target
    :type snapshot_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param body: Snapshot object supplied in the body of the operation.
    :type body: 

    """
    return web.Response(status=200)
