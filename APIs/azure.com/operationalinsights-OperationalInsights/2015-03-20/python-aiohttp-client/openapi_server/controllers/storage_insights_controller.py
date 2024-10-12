from typing import List, Dict
from aiohttp import web

from openapi_server.models.storage_insight import StorageInsight
from openapi_server.models.storage_insight_list_result import StorageInsightListResult
from openapi_server import util


async def storage_insights_create_or_update(request: web.Request, resource_group_name, workspace_name, storage_insight_name, api_version, subscription_id, parameters) -> web.Response:
    """storage_insights_create_or_update

    Create or update a storage insight.

    :param resource_group_name: The Resource Group name.
    :type resource_group_name: str
    :param workspace_name: The Log Analytics Workspace name.
    :type workspace_name: str
    :param storage_insight_name: Name of the storageInsightsConfigs resource
    :type storage_insight_name: str
    :param api_version: The client API version.
    :type api_version: str
    :param subscription_id: The Subscription ID.
    :type subscription_id: str
    :param parameters: The parameters required to create or update a storage insight.
    :type parameters: dict | bytes

    """
    parameters = StorageInsight.from_dict(parameters)
    return web.Response(status=200)


async def storage_insights_delete(request: web.Request, resource_group_name, workspace_name, storage_insight_name, api_version, subscription_id) -> web.Response:
    """storage_insights_delete

    Deletes a storageInsightsConfigs resource

    :param resource_group_name: The Resource Group name.
    :type resource_group_name: str
    :param workspace_name: The Log Analytics Workspace name.
    :type workspace_name: str
    :param storage_insight_name: Name of the storageInsightsConfigs resource
    :type storage_insight_name: str
    :param api_version: The client API version.
    :type api_version: str
    :param subscription_id: The Subscription ID.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def storage_insights_get(request: web.Request, resource_group_name, workspace_name, storage_insight_name, api_version, subscription_id) -> web.Response:
    """storage_insights_get

    Gets a storage insight instance.

    :param resource_group_name: The Resource Group name.
    :type resource_group_name: str
    :param workspace_name: The Log Analytics Workspace name.
    :type workspace_name: str
    :param storage_insight_name: Name of the storageInsightsConfigs resource
    :type storage_insight_name: str
    :param api_version: The client API version.
    :type api_version: str
    :param subscription_id: The Subscription ID.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def storage_insights_list_by_workspace(request: web.Request, resource_group_name, workspace_name, api_version, subscription_id) -> web.Response:
    """storage_insights_list_by_workspace

    Lists the storage insight instances within a workspace

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
