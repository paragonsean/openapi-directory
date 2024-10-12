from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.workspace import Workspace
from openapi_server.models.workspace_list_result import WorkspaceListResult
from openapi_server.models.workspace_update_parameters import WorkspaceUpdateParameters
from openapi_server import util


async def workspaces_create_or_update(request: web.Request, api_version, subscription_id, resource_group_name, account_name, workspace_name, parameters) -> web.Response:
    """workspaces_create_or_update

    Creates or updates a machine learning workspace with the specified parameters.

    :param api_version: The client API version.
    :type api_version: str
    :param subscription_id: The Microsoft Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group to which the machine learning team account belongs.
    :type resource_group_name: str
    :param account_name: The name of the machine learning team account.
    :type account_name: str
    :param workspace_name: The name of the machine learning team account workspace.
    :type workspace_name: str
    :param parameters: The parameters for creating or updating a machine learning workspace.
    :type parameters: dict | bytes

    """
    parameters = Workspace.from_dict(parameters)
    return web.Response(status=200)


async def workspaces_delete(request: web.Request, api_version, subscription_id, resource_group_name, account_name, workspace_name) -> web.Response:
    """workspaces_delete

    Deletes a machine learning workspace.

    :param api_version: The client API version.
    :type api_version: str
    :param subscription_id: The Microsoft Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group to which the machine learning team account belongs.
    :type resource_group_name: str
    :param account_name: The name of the machine learning team account.
    :type account_name: str
    :param workspace_name: The name of the machine learning team account workspace.
    :type workspace_name: str

    """
    return web.Response(status=200)


async def workspaces_get(request: web.Request, api_version, subscription_id, resource_group_name, account_name, workspace_name) -> web.Response:
    """workspaces_get

    Gets the properties of the specified machine learning workspace.

    :param api_version: The client API version.
    :type api_version: str
    :param subscription_id: The Microsoft Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group to which the machine learning team account belongs.
    :type resource_group_name: str
    :param account_name: The name of the machine learning team account.
    :type account_name: str
    :param workspace_name: The name of the machine learning team account workspace.
    :type workspace_name: str

    """
    return web.Response(status=200)


async def workspaces_list_by_accounts(request: web.Request, api_version, subscription_id, account_name, resource_group_name) -> web.Response:
    """workspaces_list_by_accounts

    Lists all the available machine learning workspaces under the specified team account.

    :param api_version: The client API version.
    :type api_version: str
    :param subscription_id: The Microsoft Azure subscription ID.
    :type subscription_id: str
    :param account_name: The name of the machine learning team account.
    :type account_name: str
    :param resource_group_name: The name of the resource group to which the machine learning team account belongs.
    :type resource_group_name: str

    """
    return web.Response(status=200)


async def workspaces_update(request: web.Request, api_version, subscription_id, resource_group_name, account_name, workspace_name, parameters) -> web.Response:
    """workspaces_update

    Updates a machine learning workspace with the specified parameters.

    :param api_version: The client API version.
    :type api_version: str
    :param subscription_id: The Microsoft Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group to which the machine learning team account belongs.
    :type resource_group_name: str
    :param account_name: The name of the machine learning team account.
    :type account_name: str
    :param workspace_name: The name of the machine learning team account workspace.
    :type workspace_name: str
    :param parameters: The parameters for updating a machine learning workspace.
    :type parameters: dict | bytes

    """
    parameters = WorkspaceUpdateParameters.from_dict(parameters)
    return web.Response(status=200)
