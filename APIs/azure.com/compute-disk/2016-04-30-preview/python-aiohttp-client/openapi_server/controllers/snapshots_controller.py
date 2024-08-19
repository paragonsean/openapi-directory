from typing import List, Dict
from aiohttp import web

from openapi_server.models.access_uri import AccessUri
from openapi_server.models.grant_access_data import GrantAccessData
from openapi_server.models.operation_status_response import OperationStatusResponse
from openapi_server.models.snapshot import Snapshot
from openapi_server.models.snapshot_list import SnapshotList
from openapi_server.models.snapshot_update import SnapshotUpdate
from openapi_server import util


async def snapshots_create_or_update(request: web.Request, subscription_id, resource_group_name, snapshot_name, api_version, snapshot) -> web.Response:
    """snapshots_create_or_update

    Creates or updates a snapshot.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param snapshot_name: The name of the snapshot within the given subscription and resource group.
    :type snapshot_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param snapshot: Snapshot object supplied in the body of the Put disk operation.
    :type snapshot: dict | bytes

    """
    snapshot = Snapshot.from_dict(snapshot)
    return web.Response(status=200)


async def snapshots_delete(request: web.Request, subscription_id, resource_group_name, snapshot_name, api_version) -> web.Response:
    """snapshots_delete

    Deletes a snapshot.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param snapshot_name: The name of the snapshot within the given subscription and resource group.
    :type snapshot_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def snapshots_get(request: web.Request, subscription_id, resource_group_name, snapshot_name, api_version) -> web.Response:
    """snapshots_get

    Gets information about a snapshot.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param snapshot_name: The name of the snapshot within the given subscription and resource group.
    :type snapshot_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def snapshots_grant_access(request: web.Request, subscription_id, resource_group_name, snapshot_name, api_version, grant_access_data) -> web.Response:
    """snapshots_grant_access

    Grants access to a snapshot.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param snapshot_name: The name of the snapshot within the given subscription and resource group.
    :type snapshot_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param grant_access_data: Access data object supplied in the body of the get snapshot access operation.
    :type grant_access_data: dict | bytes

    """
    grant_access_data = GrantAccessData.from_dict(grant_access_data)
    return web.Response(status=200)


async def snapshots_list(request: web.Request, subscription_id, api_version) -> web.Response:
    """snapshots_list

    Lists snapshots under a subscription.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def snapshots_list_by_resource_group(request: web.Request, subscription_id, resource_group_name, api_version) -> web.Response:
    """snapshots_list_by_resource_group

    Lists snapshots under a resource group.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def snapshots_revoke_access(request: web.Request, subscription_id, resource_group_name, snapshot_name, api_version) -> web.Response:
    """snapshots_revoke_access

    Revokes access to a snapshot.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param snapshot_name: The name of the snapshot within the given subscription and resource group.
    :type snapshot_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def snapshots_update(request: web.Request, subscription_id, resource_group_name, snapshot_name, api_version, snapshot) -> web.Response:
    """snapshots_update

    Updates (patches) a snapshot.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param snapshot_name: The name of the snapshot within the given subscription and resource group.
    :type snapshot_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param snapshot: Snapshot object supplied in the body of the Patch snapshot operation.
    :type snapshot: dict | bytes

    """
    snapshot = SnapshotUpdate.from_dict(snapshot)
    return web.Response(status=200)
