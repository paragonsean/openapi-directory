from typing import List, Dict
from aiohttp import web

from openapi_server.models.data_export import DataExport
from openapi_server.models.data_export_list_result import DataExportListResult
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def data_export_create_or_update(request: web.Request, subscription_id, resource_group_name, workspace_name, data_export_name, api_version, parameters) -> web.Response:
    """data_export_create_or_update

    Create or update a data export.

    :param subscription_id: The workspace&#39;s resource subscription ID.
    :type subscription_id: str
    :param resource_group_name: The workspace&#39;s resource group name.
    :type resource_group_name: str
    :param workspace_name: The Log Analytics workspace name.
    :type workspace_name: str
    :param data_export_name: The data export rule name.
    :type data_export_name: str
    :param api_version: The client API version.
    :type api_version: str
    :param parameters: The parameters required to create or update a data export.
    :type parameters: dict | bytes

    """
    parameters = DataExport.from_dict(parameters)
    return web.Response(status=200)


async def data_export_delete(request: web.Request, subscription_id, resource_group_name, workspace_name, data_export_name, api_version) -> web.Response:
    """data_export_delete

    Deletes the specified data export in a given workspace..

    :param subscription_id: The workspace&#39;s resource subscription ID.
    :type subscription_id: str
    :param resource_group_name: The workspace&#39;s resource group name.
    :type resource_group_name: str
    :param workspace_name: The Log Analytics workspace name.
    :type workspace_name: str
    :param data_export_name: The data export rule name.
    :type data_export_name: str
    :param api_version: The client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def data_export_get(request: web.Request, subscription_id, resource_group_name, workspace_name, data_export_name, api_version) -> web.Response:
    """data_export_get

    Gets a data export instance.

    :param subscription_id: The workspace&#39;s resource subscription ID.
    :type subscription_id: str
    :param resource_group_name: The workspace&#39;s resource group name.
    :type resource_group_name: str
    :param workspace_name: The Log Analytics workspace name.
    :type workspace_name: str
    :param data_export_name: The data export rule name.
    :type data_export_name: str
    :param api_version: The client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def data_export_list_by_workspace(request: web.Request, subscription_id, resource_group_name, workspace_name, api_version) -> web.Response:
    """data_export_list_by_workspace

    Lists the data export instances within a workspace.

    :param subscription_id: The workspace&#39;s resource subscription ID.
    :type subscription_id: str
    :param resource_group_name: The workspace&#39;s resource group name.
    :type resource_group_name: str
    :param workspace_name: The Log Analytics workspace name.
    :type workspace_name: str
    :param api_version: The client API version.
    :type api_version: str

    """
    return web.Response(status=200)
