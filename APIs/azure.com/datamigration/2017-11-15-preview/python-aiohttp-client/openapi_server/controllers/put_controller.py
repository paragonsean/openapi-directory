from typing import List, Dict
from aiohttp import web

from openapi_server.models.operations_list_default_response import OperationsListDefaultResponse
from openapi_server.models.projects_get200_response import ProjectsGet200Response
from openapi_server.models.services_get200_response import ServicesGet200Response
from openapi_server.models.tasks_get200_response import TasksGet200Response
from openapi_server import util


async def projects_create_or_update_1(request: web.Request, subscription_id, group_name, service_name, project_name, api_version, parameters) -> web.Response:
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


async def services_create_or_update_1(request: web.Request, subscription_id, group_name, service_name, api_version, parameters) -> web.Response:
    """Create or update DMS Instance

    The services resource is the top-level resource that represents the Data Migration Service. The PUT method creates a new service or updates an existing one. When a service is updated, existing child resources (i.e. tasks) are unaffected. Services currently support a single kind, \&quot;vm\&quot;, which refers to a VM-based service, although other kinds may be added in the future. This method can change the kind, SKU, and network of the service, but if tasks are currently running (i.e. the service is busy), this will fail with 400 Bad Request (\&quot;ServiceIsBusy\&quot;). The provider will reply when successful with 200 OK or 201 Created. Long-running operations use the provisioningState property.

    :param subscription_id: Identifier of the subscription
    :type subscription_id: str
    :param group_name: Name of the resource group
    :type group_name: str
    :param service_name: Name of the service
    :type service_name: str
    :param api_version: Version of the API
    :type api_version: str
    :param parameters: Information about the service
    :type parameters: dict | bytes

    """
    parameters = ServicesGet200Response.from_dict(parameters)
    return web.Response(status=200)


async def tasks_create_or_update_1(request: web.Request, subscription_id, group_name, service_name, project_name, task_name, api_version, parameters) -> web.Response:
    """Create or update task

    The tasks resource is a nested, proxy-only resource representing work performed by a DMS instance. The PUT method creates a new task or updates an existing one, although since tasks have no mutable custom properties, there is little reason to update an exising one.

    :param subscription_id: Identifier of the subscription
    :type subscription_id: str
    :param group_name: Name of the resource group
    :type group_name: str
    :param service_name: Name of the service
    :type service_name: str
    :param project_name: Name of the project
    :type project_name: str
    :param task_name: Name of the Task
    :type task_name: str
    :param api_version: Version of the API
    :type api_version: str
    :param parameters: Information about the task
    :type parameters: dict | bytes

    """
    parameters = TasksGet200Response.from_dict(parameters)
    return web.Response(status=200)
