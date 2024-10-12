from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.topology_list import TopologyList
from openapi_server.models.topology_resource import TopologyResource
from openapi_server import util


async def topology_get(request: web.Request, subscription_id, resource_group_name, asc_location, topology_resource_name, api_version) -> web.Response:
    """topology_get

    Gets a specific topology component.

    :param subscription_id: Azure subscription ID
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the user&#39;s subscription. The name is case insensitive.
    :type resource_group_name: str
    :param asc_location: The location where ASC stores the data of the subscription. can be retrieved from Get locations
    :type asc_location: str
    :param topology_resource_name: Name of a topology resources collection.
    :type topology_resource_name: str
    :param api_version: API version for the operation
    :type api_version: str

    """
    return web.Response(status=200)


async def topology_list(request: web.Request, subscription_id, api_version) -> web.Response:
    """topology_list

    Gets a list that allows to build a topology view of a subscription.

    :param subscription_id: Azure subscription ID
    :type subscription_id: str
    :param api_version: API version for the operation
    :type api_version: str

    """
    return web.Response(status=200)


async def topology_list_by_home_region(request: web.Request, subscription_id, asc_location, api_version) -> web.Response:
    """topology_list_by_home_region

    Gets a list that allows to build a topology view of a subscription and location.

    :param subscription_id: Azure subscription ID
    :type subscription_id: str
    :param asc_location: The location where ASC stores the data of the subscription. can be retrieved from Get locations
    :type asc_location: str
    :param api_version: API version for the operation
    :type api_version: str

    """
    return web.Response(status=200)
