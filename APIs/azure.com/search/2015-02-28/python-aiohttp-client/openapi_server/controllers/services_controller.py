from typing import List, Dict
from aiohttp import web

from openapi_server.models.search_service_create_or_update_parameters import SearchServiceCreateOrUpdateParameters
from openapi_server.models.search_service_list_result import SearchServiceListResult
from openapi_server.models.search_service_resource import SearchServiceResource
from openapi_server import util


async def services_create_or_update(request: web.Request, resource_group_name, service_name, api_version, subscription_id, parameters) -> web.Response:
    """services_create_or_update

    Creates or updates a Search service in the given resource group. If the Search service already exists, all properties will be updated with the given values.

    :param resource_group_name: The name of the resource group within the current subscription.
    :type resource_group_name: str
    :param service_name: The name of the Search service to create or update.
    :type service_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: The properties to set or update on the Search service.
    :type parameters: dict | bytes

    """
    parameters = SearchServiceCreateOrUpdateParameters.from_dict(parameters)
    return web.Response(status=200)


async def services_delete(request: web.Request, resource_group_name, service_name, api_version, subscription_id) -> web.Response:
    """services_delete

    Deletes a Search service in the given resource group, along with its associated resources.

    :param resource_group_name: The name of the resource group within the current subscription.
    :type resource_group_name: str
    :param service_name: The name of the Search service to delete.
    :type service_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def services_list(request: web.Request, resource_group_name, api_version, subscription_id) -> web.Response:
    """services_list

    Returns a list of all Search services in the given resource group.

    :param resource_group_name: The name of the resource group within the current subscription.
    :type resource_group_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)
