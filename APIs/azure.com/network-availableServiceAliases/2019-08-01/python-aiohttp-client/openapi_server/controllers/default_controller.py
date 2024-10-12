from typing import List, Dict
from aiohttp import web

from openapi_server.models.available_service_aliases_result import AvailableServiceAliasesResult
from openapi_server import util


async def available_service_aliases_list(request: web.Request, location, subscription_id, api_version) -> web.Response:
    """available_service_aliases_list

    Gets all available service aliases for this subscription in this region.

    :param location: The location.
    :type location: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def available_service_aliases_list_by_resource_group(request: web.Request, resource_group_name, location, subscription_id, api_version) -> web.Response:
    """available_service_aliases_list_by_resource_group

    Gets all available service aliases for this resource group in this region.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param location: The location.
    :type location: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)
