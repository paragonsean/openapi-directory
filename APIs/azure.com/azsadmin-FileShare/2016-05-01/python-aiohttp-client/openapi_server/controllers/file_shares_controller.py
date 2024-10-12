from typing import List, Dict
from aiohttp import web

from openapi_server.models.file_share import FileShare
from openapi_server.models.file_share_list import FileShareList
from openapi_server import util


async def file_shares_get(request: web.Request, subscription_id, resource_group_name, location, file_share, api_version) -> web.Response:
    """file_shares_get

    Returns the requested fabric file share.

    :param subscription_id: Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Name of the resource group.
    :type resource_group_name: str
    :param location: Location of the resource.
    :type location: str
    :param file_share: Fabric file share name.
    :type file_share: str
    :param api_version: Client API Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def file_shares_list(request: web.Request, subscription_id, resource_group_name, location, api_version, filter=None) -> web.Response:
    """file_shares_list

    Returns a list of all fabric file shares at a certain location.

    :param subscription_id: Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Name of the resource group.
    :type resource_group_name: str
    :param location: Location of the resource.
    :type location: str
    :param api_version: Client API Version.
    :type api_version: str
    :param filter: OData filter parameter.
    :type filter: str

    """
    return web.Response(status=200)
