from typing import List, Dict
from aiohttp import web

from openapi_server.models.operations_list200_response import OperationsList200Response
from openapi_server.models.operations_list_default_response import OperationsListDefaultResponse
from openapi_server.models.projects_get200_response import ProjectsGet200Response
from openapi_server.models.projects_list200_response import ProjectsList200Response
from openapi_server.models.resource_skus_list_skus200_response import ResourceSkusListSkus200Response
from openapi_server.models.services_get200_response import ServicesGet200Response
from openapi_server.models.services_list200_response import ServicesList200Response
from openapi_server.models.services_list_skus200_response import ServicesListSkus200Response
from openapi_server.models.tasks_get200_response import TasksGet200Response
from openapi_server.models.tasks_list200_response import TasksList200Response
from openapi_server.models.usages_list200_response import UsagesList200Response
from openapi_server import util


async def operations_list_0(request: web.Request, api_version) -> web.Response:
    """Get available resource provider actions (operations)

    Lists all available actions exposed by the Data Migration Service resource provider.

    :param api_version: Version of the API
    :type api_version: str

    """
    return web.Response(status=200)


async def projects_get_1(request: web.Request, subscription_id, group_name, service_name, project_name, api_version) -> web.Response:
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


async def projects_list_1(request: web.Request, subscription_id, group_name, service_name, api_version) -> web.Response:
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


async def resource_skus_list_skus_0(request: web.Request, subscription_id, api_version) -> web.Response:
    """Get supported SKUs

    The skus action returns the list of SKUs that DMS supports.

    :param subscription_id: Identifier of the subscription
    :type subscription_id: str
    :param api_version: Version of the API
    :type api_version: str

    """
    return web.Response(status=200)


async def services_get_1(request: web.Request, subscription_id, group_name, service_name, api_version) -> web.Response:
    """Get DMS Service Instance

    The services resource is the top-level resource that represents the Data Migration Service. The GET method retrieves information about a service instance.

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


async def services_list_1(request: web.Request, subscription_id, api_version) -> web.Response:
    """Get services in subscription

    The services resource is the top-level resource that represents the Data Migration Service. This method returns a list of service resources in a subscription.

    :param subscription_id: Identifier of the subscription
    :type subscription_id: str
    :param api_version: Version of the API
    :type api_version: str

    """
    return web.Response(status=200)


async def services_list_by_resource_group_1(request: web.Request, subscription_id, group_name, api_version) -> web.Response:
    """Get services in resource group

    The Services resource is the top-level resource that represents the Data Migration Service. This method returns a list of service resources in a resource group.

    :param subscription_id: Identifier of the subscription
    :type subscription_id: str
    :param group_name: Name of the resource group
    :type group_name: str
    :param api_version: Version of the API
    :type api_version: str

    """
    return web.Response(status=200)


async def services_list_skus_1(request: web.Request, subscription_id, group_name, service_name, api_version) -> web.Response:
    """Get compatible SKUs

    The services resource is the top-level resource that represents the Data Migration Service. The skus action returns the list of SKUs that a service resource can be updated to.

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


async def tasks_get_1(request: web.Request, subscription_id, group_name, service_name, project_name, task_name, api_version, expand=None) -> web.Response:
    """Get task information

    The tasks resource is a nested, proxy-only resource representing work performed by a DMS instance. The GET method retrieves information about a task.

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
    :param expand: Expand the response
    :type expand: str

    """
    return web.Response(status=200)


async def tasks_list_1(request: web.Request, subscription_id, group_name, service_name, project_name, api_version, task_type=None) -> web.Response:
    """Get tasks in a service

    The services resource is the top-level resource that represents the Data Migration Service. This method returns a list of tasks owned by a service resource. Some tasks may have a status of Unknown, which indicates that an error occurred while querying the status of that task.

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
    :param task_type: Filter tasks by task type
    :type task_type: str

    """
    return web.Response(status=200)


async def usages_list_0(request: web.Request, subscription_id, location, api_version) -> web.Response:
    """Get resource quotas and usage information

    This method returns region-specific quotas and resource usage information for the Data Migration Service.

    :param subscription_id: Identifier of the subscription
    :type subscription_id: str
    :param location: The Azure region of the operation
    :type location: str
    :param api_version: Version of the API
    :type api_version: str

    """
    return web.Response(status=200)
