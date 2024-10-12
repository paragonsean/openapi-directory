from typing import List, Dict
from aiohttp import web

from openapi_server.models.available_delegations_result import AvailableDelegationsResult
from openapi_server import util


async def available_delegations_list(request: web.Request, location, api_version, subscription_id) -> web.Response:
    """available_delegations_list

    Gets all of the available subnet delegations for this subscription in this region.

    :param location: The location of the subnet.
    :type location: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def available_resource_group_delegations_list(request: web.Request, location, resource_group_name, subscription_id, api_version) -> web.Response:
    """available_resource_group_delegations_list

    Gets all of the available subnet delegations for this resource group in this region.

    :param location: The location of the domain name.
    :type location: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)
