from typing import List, Dict
from aiohttp import web

from openapi_server.models.data_source import DataSource
from openapi_server.models.data_source_list_result import DataSourceListResult
from openapi_server import util


async def data_sources_create_or_update(request: web.Request, resource_group_name, workspace_name, data_source_name, api_version, subscription_id, parameters) -> web.Response:
    """data_sources_create_or_update

    Create or update a data source.

    :param resource_group_name: The name of the resource group to get. The name is case insensitive.
    :type resource_group_name: str
    :param workspace_name: Name of the Log Analytics Workspace that will contain the datasource
    :type workspace_name: str
    :param data_source_name: The name of the datasource resource.
    :type data_source_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: The parameters required to create or update a datasource.
    :type parameters: dict | bytes

    """
    parameters = DataSource.from_dict(parameters)
    return web.Response(status=200)


async def data_sources_delete(request: web.Request, resource_group_name, workspace_name, data_source_name, api_version, subscription_id) -> web.Response:
    """data_sources_delete

    Deletes a data source instance.

    :param resource_group_name: The name of the resource group to get. The name is case insensitive.
    :type resource_group_name: str
    :param workspace_name: Name of the Log Analytics Workspace that contains the datasource.
    :type workspace_name: str
    :param data_source_name: Name of the datasource.
    :type data_source_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def data_sources_get(request: web.Request, resource_group_name, workspace_name, data_source_name, api_version, subscription_id) -> web.Response:
    """data_sources_get

    Gets a datasource instance.

    :param resource_group_name: The name of the resource group to get. The name is case insensitive.
    :type resource_group_name: str
    :param workspace_name: Name of the Log Analytics Workspace that contains the datasource.
    :type workspace_name: str
    :param data_source_name: Name of the datasource
    :type data_source_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def data_sources_list_by_workspace(request: web.Request, resource_group_name, workspace_name, filter, api_version, subscription_id, skiptoken=None) -> web.Response:
    """data_sources_list_by_workspace

    Gets the first page of data source instances in a workspace with the link to the next page.

    :param resource_group_name: The name of the resource group to get. The name is case insensitive.
    :type resource_group_name: str
    :param workspace_name: The workspace that contains the data sources.
    :type workspace_name: str
    :param filter: The filter to apply on the operation.
    :type filter: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param skiptoken: Starting point of the collection of data source instances.
    :type skiptoken: str

    """
    return web.Response(status=200)
