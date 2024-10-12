from typing import List, Dict
from aiohttp import web

from openapi_server.models.mount_target_list import MountTargetList
from openapi_server import util


async def mount_targets_list(request: web.Request, subscription_id, resource_group_name, account_name, pool_name, volume_name, api_version) -> web.Response:
    """Describe all mount targets

    List all mount targets associated with the volume

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
