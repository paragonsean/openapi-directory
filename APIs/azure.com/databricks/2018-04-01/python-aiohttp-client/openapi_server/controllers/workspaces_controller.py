from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.workspace import Workspace
from openapi_server.models.workspace_list_result import WorkspaceListResult
from openapi_server.models.workspace_update import WorkspaceUpdate
from openapi_server import util


async def workspaces_create_or_update(request: web.Request, resource_group_name, workspace_name, api_version, subscription_id, parameters) -> web.Response:
    """workspaces_create_or_update

    Creates a new workspace.

    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param workspace_name: The name of the workspace.
    :type workspace_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param parameters: Parameters supplied to the create or update a workspace.
    :type parameters: dict | bytes

    """
    parameters = Workspace.from_dict(parameters)
    return web.Response(status=200)


async def workspaces_delete(request: web.Request, resource_group_name, workspace_name, api_version, subscription_id) -> web.Response:
    """workspaces_delete

    Deletes the workspace.

    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param workspace_name: The name of the workspace.
    :type workspace_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def workspaces_get(request: web.Request, resource_group_name, workspace_name, api_version, subscription_id) -> web.Response:
    """workspaces_get

    Gets the workspace.

    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param workspace_name: The name of the workspace.
    :type workspace_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def workspaces_list_by_resource_group(request: web.Request, resource_group_name, api_version, subscription_id) -> web.Response:
    """workspaces_list_by_resource_group

    Gets all the workspaces within a resource group.

    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def workspaces_list_by_subscription(request: web.Request, api_version, subscription_id) -> web.Response:
    """workspaces_list_by_subscription

    Gets all the workspaces within a subscription.

    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def workspaces_update(request: web.Request, resource_group_name, workspace_name, api_version, subscription_id, parameters) -> web.Response:
    """workspaces_update

    Updates a workspace.

    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param workspace_name: The name of the workspace.
    :type workspace_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param parameters: The update to the workspace.
    :type parameters: dict | bytes

    """
    parameters = WorkspaceUpdate.from_dict(parameters)
    return web.Response(status=200)
