from typing import List, Dict
from aiohttp import web

from openapi_server.models.operations_list_default_response import OperationsListDefaultResponse
from openapi_server.models.projects_get200_response import ProjectsGet200Response
from openapi_server.models.projects_list200_response import ProjectsList200Response
from openapi_server import util


async def projects_create_or_update(request: web.Request, subscription_id, group_name, service_name, project_name, api_version, parameters) -> web.Response:
    """Create or update project

    The project resource is a nested resource representing a stored migration project. The PUT method creates a new project or updates an existing one.

    :param subscription_id: Identifier of the subscription
    :type subscription_id: str
    :param group_name: Name of the resource group
    :type group_name: str
    :param service_name: Name of the service
    :type service_name: str
    :param project_name: Name of the project
    :type project_name: str
    :param api_version: Version of the API
    :type api_version: str
    :param parameters: Information about the project
    :type parameters: dict | bytes

    """
    parameters = ProjectsGet200Response.from_dict(parameters)
    return web.Response(status=200)


async def projects_delete(request: web.Request, subscription_id, group_name, service_name, project_name, api_version, delete_running_tasks=None) -> web.Response:
    """Delete project

    The project resource is a nested resource representing a stored migration project. The DELETE method deletes a project.

    :param subscription_id: Identifier of the subscription
    :type subscription_id: str
    :param group_name: Name of the resource group
    :type group_name: str
    :param service_name: Name of the service
    :type service_name: str
    :param project_name: Name of the project
    :type project_name: str
    :param api_version: Version of the API
    :type api_version: str
    :param delete_running_tasks: Delete the resource even if it contains running tasks
    :type delete_running_tasks: bool

    """
    return web.Response(status=200)


async def projects_get(request: web.Request, subscription_id, group_name, service_name, project_name, api_version) -> web.Response:
    """Get project information

    The project resource is a nested resource representing a stored migration project. The GET method retrieves information about a project.

    :param subscription_id: Identifier of the subscription
    :type subscription_id: str
    :param group_name: Name of the resource group
    :type group_name: str
    :param service_name: Name of the service
    :type service_name: str
    :param project_name: Name of the project
    :type project_name: str
    :param api_version: Version of the API
    :type api_version: str

    """
    return web.Response(status=200)


async def projects_list(request: web.Request, subscription_id, group_name, service_name, api_version) -> web.Response:
    """Get projects in a service

    The project resource is a nested resource representing a stored migration project. This method returns a list of projects owned by a service resource.

    :param subscription_id: Identifier of the subscription
    :type subscription_id: str
    :param group_name: Name of the resource group
    :type group_name: str
    :param service_name: Name of the service
    :type service_name: str
    :param api_version: Version of the API
    :type api_version: str

    """
    return web.Response(status=200)


async def projects_update(request: web.Request, subscription_id, group_name, service_name, project_name, api_version, parameters) -> web.Response:
    """Update project

    The project resource is a nested resource representing a stored migration project. The PATCH method updates an existing project.

    :param subscription_id: Identifier of the subscription
    :type subscription_id: str
    :param group_name: Name of the resource group
    :type group_name: str
    :param service_name: Name of the service
    :type service_name: str
    :param project_name: Name of the project
    :type project_name: str
    :param api_version: Version of the API
    :type api_version: str
    :param parameters: Information about the project
    :type parameters: dict | bytes

    """
    parameters = ProjectsGet200Response.from_dict(parameters)
    return web.Response(status=200)
