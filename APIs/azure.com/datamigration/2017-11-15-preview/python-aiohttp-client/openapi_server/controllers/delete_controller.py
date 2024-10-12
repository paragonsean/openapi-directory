from typing import List, Dict
from aiohttp import web

from openapi_server.models.operations_list_default_response import OperationsListDefaultResponse
from openapi_server import util


async def projects_delete_1(request: web.Request, subscription_id, group_name, service_name, project_name, api_version, delete_running_tasks=None) -> web.Response:
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


async def services_delete_1(request: web.Request, subscription_id, group_name, service_name, api_version, delete_running_tasks=None) -> web.Response:
    """Delete DMS Service Instance

    The services resource is the top-level resource that represents the Data Migration Service. The DELETE method deletes a service. Any running tasks will be canceled.

    :param subscription_id: Identifier of the subscription
    :type subscription_id: str
    :param group_name: Name of the resource group
    :type group_name: str
    :param service_name: Name of the service
    :type service_name: str
    :param api_version: Version of the API
    :type api_version: str
    :param delete_running_tasks: Delete the resource even if it contains running tasks
    :type delete_running_tasks: bool

    """
    return web.Response(status=200)


async def tasks_delete_1(request: web.Request, subscription_id, group_name, service_name, project_name, task_name, api_version, delete_running_tasks=None) -> web.Response:
    """Delete task

    The tasks resource is a nested, proxy-only resource representing work performed by a DMS instance. The DELETE method deletes a task, canceling it first if it&#39;s running.

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
    :param delete_running_tasks: Delete the resource even if it contains running tasks
    :type delete_running_tasks: bool

    """
    return web.Response(status=200)
