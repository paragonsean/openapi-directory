from typing import List, Dict
from aiohttp import web

from openapi_server.models.saved_search import SavedSearch
from openapi_server.models.saved_searches_list_result import SavedSearchesListResult
from openapi_server import util


async def saved_searches_create_or_update(request: web.Request, subscription_id, resource_group_name, workspace_name, saved_search_id, api_version, parameters) -> web.Response:
    """saved_searches_create_or_update

    Creates or updates a saved search for a given workspace.

    :param subscription_id: The Subscription ID.
    :type subscription_id: str
    :param resource_group_name: The Resource Group name.
    :type resource_group_name: str
    :param workspace_name: The Log Analytics Workspace name.
    :type workspace_name: str
    :param saved_search_id: The id of the saved search.
    :type saved_search_id: str
    :param api_version: The client API version.
    :type api_version: str
    :param parameters: The parameters required to save a search.
    :type parameters: dict | bytes

    """
    parameters = SavedSearch.from_dict(parameters)
    return web.Response(status=200)


async def saved_searches_delete(request: web.Request, subscription_id, resource_group_name, workspace_name, saved_search_id, api_version) -> web.Response:
    """saved_searches_delete

    Deletes the specified saved search in a given workspace.

    :param subscription_id: The Subscription ID.
    :type subscription_id: str
    :param resource_group_name: The Resource Group name.
    :type resource_group_name: str
    :param workspace_name: The Log Analytics Workspace name.
    :type workspace_name: str
    :param saved_search_id: The id of the saved search.
    :type saved_search_id: str
    :param api_version: The client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def saved_searches_get(request: web.Request, subscription_id, resource_group_name, workspace_name, saved_search_id, api_version) -> web.Response:
    """saved_searches_get

    Gets the specified saved search for a given workspace.

    :param subscription_id: The Subscription ID.
    :type subscription_id: str
    :param resource_group_name: The Resource Group name.
    :type resource_group_name: str
    :param workspace_name: The Log Analytics Workspace name.
    :type workspace_name: str
    :param saved_search_id: The id of the saved search.
    :type saved_search_id: str
    :param api_version: The client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def saved_searches_list_by_workspace(request: web.Request, resource_group_name, workspace_name, api_version, subscription_id) -> web.Response:
    """saved_searches_list_by_workspace

    Gets the saved searches for a given Log Analytics Workspace

    :param resource_group_name: The Resource Group name.
    :type resource_group_name: str
    :param workspace_name: The Log Analytics Workspace name.
    :type workspace_name: str
    :param api_version: The client API version.
    :type api_version: str
    :param subscription_id: The Subscription ID.
    :type subscription_id: str

    """
    return web.Response(status=200)
