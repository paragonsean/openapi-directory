from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.workspace import Workspace
from openapi_server.models.workspace_keys_response import WorkspaceKeysResponse
from openapi_server.models.workspace_list_result import WorkspaceListResult
from openapi_server.models.workspace_update_parameters import WorkspaceUpdateParameters
from openapi_server import util


async def workspaces_create_or_update(request: web.Request, api_version, subscription_id, resource_group_name, workspace_name, parameters) -> web.Response:
    """workspaces_create_or_update

    Creates or updates a workspace with the specified parameters.

    :param api_version: The client API version.
    :type api_version: str
    :param subscription_id: The Microsoft Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group to which the machine learning workspace belongs.
    :type resource_group_name: str
    :param workspace_name: The name of the machine learning workspace.
    :type workspace_name: str
    :param parameters: The parameters for creating or updating a machine learning workspace.
    :type parameters: dict | bytes

    """
    parameters = Workspace.from_dict(parameters)
    return web.Response(status=200)


async def workspaces_delete(request: web.Request, api_version, subscription_id, resource_group_name, workspace_name) -> web.Response:
    """workspaces_delete

    Deletes a machine learning workspace.

    :param api_version: The client API version.
    :type api_version: str
    :param subscription_id: The Microsoft Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group to which the machine learning workspace belongs.
    :type resource_group_name: str
    :param workspace_name: The name of the machine learning workspace.
    :type workspace_name: str

    """
    return web.Response(status=200)


async def workspaces_get(request: web.Request, api_version, subscription_id, resource_group_name, workspace_name) -> web.Response:
    """workspaces_get

    Gets the properties of the specified machine learning workspace.

    :param api_version: The client API version.
    :type api_version: str
    :param subscription_id: The Microsoft Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group to which the machine learning workspace belongs.
    :type resource_group_name: str
    :param workspace_name: The name of the machine learning workspace.
    :type workspace_name: str

    """
    return web.Response(status=200)


async def workspaces_list(request: web.Request, api_version, subscription_id) -> web.Response:
    """workspaces_list

    Lists all the available machine learning workspaces under the specified subscription.

    :param api_version: The client API version.
    :type api_version: str
    :param subscription_id: The Microsoft Azure subscription ID.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def workspaces_list_by_resource_group(request: web.Request, api_version, subscription_id, resource_group_name) -> web.Response:
    """workspaces_list_by_resource_group

    Lists all the available machine learning workspaces under the specified resource group.

    :param api_version: The client API version.
    :type api_version: str
    :param subscription_id: The Microsoft Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group to which the machine learning workspace belongs.
    :type resource_group_name: str

    """
    return web.Response(status=200)


async def workspaces_list_workspace_keys(request: web.Request, api_version, subscription_id, workspace_name, resource_group_name) -> web.Response:
    """workspaces_list_workspace_keys

    List the authorization keys associated with this workspace.

    :param api_version: The client API version.
    :type api_version: str
    :param subscription_id: The Microsoft Azure subscription ID.
    :type subscription_id: str
    :param workspace_name: The name of the machine learning workspace.
    :type workspace_name: str
    :param resource_group_name: The name of the resource group to which the machine learning workspace belongs.
    :type resource_group_name: str

    """
    return web.Response(status=200)


async def workspaces_resync_storage_keys(request: web.Request, api_version, subscription_id, workspace_name, resource_group_name) -> web.Response:
    """workspaces_resync_storage_keys

    Resync storage keys associated with this workspace.

    :param api_version: The client API version.
    :type api_version: str
    :param subscription_id: The Microsoft Azure subscription ID.
    :type subscription_id: str
    :param workspace_name: The name of the machine learning workspace.
    :type workspace_name: str
    :param resource_group_name: The name of the resource group to which the machine learning workspace belongs.
    :type resource_group_name: str

    """
    return web.Response(status=200)


async def workspaces_update(request: web.Request, api_version, subscription_id, resource_group_name, workspace_name, parameters) -> web.Response:
    """workspaces_update

    Updates a machine learning workspace with the specified parameters.

    :param api_version: The client API version.
    :type api_version: str
    :param subscription_id: The Microsoft Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group to which the machine learning workspace belongs.
    :type resource_group_name: str
    :param workspace_name: The name of the machine learning workspace.
    :type workspace_name: str
    :param parameters: The parameters for updating a machine learning workspace.
    :type parameters: dict | bytes

    """
    parameters = WorkspaceUpdateParameters.from_dict(parameters)
    return web.Response(status=200)
