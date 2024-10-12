from typing import List, Dict
from aiohttp import web

from openapi_server.models.allowed_connections_list import AllowedConnectionsList
from openapi_server.models.allowed_connections_resource import AllowedConnectionsResource
from openapi_server.models.cloud_error import CloudError
from openapi_server import util


async def allowed_connections_get(request: web.Request, subscription_id, resource_group_name, asc_location, connection_type, api_version) -> web.Response:
    """allowed_connections_get

    Gets the list of all possible traffic between resources for the subscription and location, based on connection type.

    :param subscription_id: Azure subscription ID
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the user&#39;s subscription. The name is case insensitive.
    :type resource_group_name: str
    :param asc_location: The location where ASC stores the data of the subscription. can be retrieved from Get locations
    :type asc_location: str
    :param connection_type: The type of allowed connections (Internal, External)
    :type connection_type: str
    :param api_version: API version for the operation
    :type api_version: str

    """
    return web.Response(status=200)


async def allowed_connections_list(request: web.Request, subscription_id, api_version) -> web.Response:
    """allowed_connections_list

    Gets the list of all possible traffic between resources for the subscription

    :param subscription_id: Azure subscription ID
    :type subscription_id: str
    :param api_version: API version for the operation
    :type api_version: str

    """
    return web.Response(status=200)


async def allowed_connections_list_by_home_region(request: web.Request, subscription_id, asc_location, api_version) -> web.Response:
    """allowed_connections_list_by_home_region

    Gets the list of all possible traffic between resources for the subscription and location.

    :param subscription_id: Azure subscription ID
    :type subscription_id: str
    :param asc_location: The location where ASC stores the data of the subscription. can be retrieved from Get locations
    :type asc_location: str
    :param api_version: API version for the operation
    :type api_version: str

    """
    return web.Response(status=200)
