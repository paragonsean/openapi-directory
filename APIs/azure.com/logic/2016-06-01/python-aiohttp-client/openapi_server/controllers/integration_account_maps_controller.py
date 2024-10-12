from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_callback_url_parameters import GetCallbackUrlParameters
from openapi_server.models.integration_account_map import IntegrationAccountMap
from openapi_server.models.integration_account_map_list_result import IntegrationAccountMapListResult
from openapi_server.models.workflow_trigger_callback_url import WorkflowTriggerCallbackUrl
from openapi_server import util


async def maps_create_or_update(request: web.Request, subscription_id, resource_group_name, integration_account_name, map_name, api_version, map) -> web.Response:
    """maps_create_or_update

    Creates or updates an integration account map.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param integration_account_name: The integration account name.
    :type integration_account_name: str
    :param map_name: The integration account map name.
    :type map_name: str
    :param api_version: The API version.
    :type api_version: str
    :param map: The integration account map.
    :type map: dict | bytes

    """
    map = IntegrationAccountMap.from_dict(map)
    return web.Response(status=200)


async def maps_delete(request: web.Request, subscription_id, resource_group_name, integration_account_name, map_name, api_version) -> web.Response:
    """maps_delete

    Deletes an integration account map.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param integration_account_name: The integration account name.
    :type integration_account_name: str
    :param map_name: The integration account map name.
    :type map_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def maps_get(request: web.Request, subscription_id, resource_group_name, integration_account_name, map_name, api_version) -> web.Response:
    """maps_get

    Gets an integration account map.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param integration_account_name: The integration account name.
    :type integration_account_name: str
    :param map_name: The integration account map name.
    :type map_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def maps_list_by_integration_accounts(request: web.Request, subscription_id, resource_group_name, integration_account_name, api_version, top=None, filter=None) -> web.Response:
    """maps_list_by_integration_accounts

    Gets a list of integration account maps.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param integration_account_name: The integration account name.
    :type integration_account_name: str
    :param api_version: The API version.
    :type api_version: str
    :param top: The number of items to be included in the result.
    :type top: int
    :param filter: The filter to apply on the operation. Options for filters include: MapType.
    :type filter: str

    """
    return web.Response(status=200)


async def maps_list_content_callback_url(request: web.Request, subscription_id, resource_group_name, integration_account_name, map_name, api_version, list_content_callback_url) -> web.Response:
    """maps_list_content_callback_url

    Get the content callback url.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param integration_account_name: The integration account name.
    :type integration_account_name: str
    :param map_name: The integration account map name.
    :type map_name: str
    :param api_version: The API version.
    :type api_version: str
    :param list_content_callback_url: 
    :type list_content_callback_url: dict | bytes

    """
    list_content_callback_url = GetCallbackUrlParameters.from_dict(list_content_callback_url)
    return web.Response(status=200)
