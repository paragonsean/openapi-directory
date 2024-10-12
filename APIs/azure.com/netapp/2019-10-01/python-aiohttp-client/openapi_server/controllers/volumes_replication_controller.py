from typing import List, Dict
from aiohttp import web

from openapi_server.models.authorize_request import AuthorizeRequest
from openapi_server.models.replication_status import ReplicationStatus
from openapi_server import util


async def volumes_authorize_replication(request: web.Request, subscription_id, resource_group_name, account_name, pool_name, volume_name, api_version, body) -> web.Response:
    """Authorize source volume replication

    Authorize the replication connection on the source volume

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
    :param body: authorize request object supplied in the body of the operation.
    :type body: dict | bytes

    """
    body = AuthorizeRequest.from_dict(body)
    return web.Response(status=200)


async def volumes_break_replication(request: web.Request, subscription_id, resource_group_name, account_name, pool_name, volume_name, api_version) -> web.Response:
    """Break volume replication

    Break the replication connection on the destination volume

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


async def volumes_delete_replication(request: web.Request, subscription_id, resource_group_name, account_name, pool_name, volume_name, api_version) -> web.Response:
    """Delete volume replication

    Delete the replication connection on the destination volume, and send release to the source replication

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


async def volumes_replication_status(request: web.Request, subscription_id, resource_group_name, account_name, pool_name, volume_name, api_version) -> web.Response:
    """Get volume replication status

    Get the status of the replication

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


async def volumes_resync_replication(request: web.Request, subscription_id, resource_group_name, account_name, pool_name, volume_name, api_version) -> web.Response:
    """Resync volume replication

    Resync the connection on the destination volume. If the operation is ran on the source volume it will reverse-resync the connection and sync from source to destination.

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
