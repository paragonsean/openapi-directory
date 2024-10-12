from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.project import Project
from openapi_server.models.project_list_result import ProjectListResult
from openapi_server.models.project_update_parameters import ProjectUpdateParameters
from openapi_server import util


async def projects_create_or_update(request: web.Request, api_version, subscription_id, resource_group_name, account_name, workspace_name, project_name, parameters) -> web.Response:
    """projects_create_or_update

    Creates or updates a project with the specified parameters.

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
    :param project_name: The name of the machine learning project under a team account workspace.
    :type project_name: str
    :param parameters: The parameters for creating or updating a project.
    :type parameters: dict | bytes

    """
    parameters = Project.from_dict(parameters)
    return web.Response(status=200)


async def projects_delete(request: web.Request, api_version, subscription_id, resource_group_name, account_name, workspace_name, project_name) -> web.Response:
    """projects_delete

    Deletes a project.

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
    :param project_name: The name of the machine learning project under a team account workspace.
    :type project_name: str

    """
    return web.Response(status=200)


async def projects_get(request: web.Request, api_version, subscription_id, resource_group_name, account_name, workspace_name, project_name) -> web.Response:
    """projects_get

    Gets the properties of the specified machine learning project.

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
    :param project_name: The name of the machine learning project under a team account workspace.
    :type project_name: str

    """
    return web.Response(status=200)


async def projects_list_by_workspace(request: web.Request, api_version, subscription_id, account_name, workspace_name, resource_group_name) -> web.Response:
    """projects_list_by_workspace

    Lists all the available machine learning projects under the specified workspace.

    :param api_version: The client API version.
    :type api_version: str
    :param subscription_id: The Microsoft Azure subscription ID.
    :type subscription_id: str
    :param account_name: The name of the machine learning team account.
    :type account_name: str
    :param workspace_name: The name of the machine learning team account workspace.
    :type workspace_name: str
    :param resource_group_name: The name of the resource group to which the machine learning team account belongs.
    :type resource_group_name: str

    """
    return web.Response(status=200)


async def projects_update(request: web.Request, api_version, subscription_id, resource_group_name, account_name, workspace_name, project_name, parameters) -> web.Response:
    """projects_update

    Updates a project with the specified parameters.

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
    :param project_name: The name of the machine learning project under a team account workspace.
    :type project_name: str
    :param parameters: The parameters for updating a machine learning team account.
    :type parameters: dict | bytes

    """
    parameters = ProjectUpdateParameters.from_dict(parameters)
    return web.Response(status=200)
