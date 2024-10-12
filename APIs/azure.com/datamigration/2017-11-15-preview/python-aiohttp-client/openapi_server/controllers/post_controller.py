from typing import List, Dict
from aiohttp import web

from openapi_server.models.operations_list_default_response import OperationsListDefaultResponse
from openapi_server.models.services_check_name_availability200_response import ServicesCheckNameAvailability200Response
from openapi_server.models.services_check_name_availability_request import ServicesCheckNameAvailabilityRequest
from openapi_server.models.services_check_status200_response import ServicesCheckStatus200Response
from openapi_server.models.tasks_get200_response import TasksGet200Response
from openapi_server import util


async def services_check_children_name_availability_0(request: web.Request, subscription_id, group_name, api_version, service_name, parameters) -> web.Response:
    """Check nested resource name validity and availability

    This method checks whether a proposed nested resource name is valid and available.

    :param subscription_id: Identifier of the subscription
    :type subscription_id: str
    :param group_name: Name of the resource group
    :type group_name: str
    :param api_version: Version of the API
    :type api_version: str
    :param service_name: Name of the service
    :type service_name: str
    :param parameters: Requested name to validate
    :type parameters: dict | bytes

    """
    parameters = ServicesCheckNameAvailabilityRequest.from_dict(parameters)
    return web.Response(status=200)


async def services_check_name_availability_0(request: web.Request, subscription_id, api_version, location, parameters) -> web.Response:
    """Check name validity and availability

    This method checks whether a proposed top-level resource name is valid and available.

    :param subscription_id: Identifier of the subscription
    :type subscription_id: str
    :param api_version: Version of the API
    :type api_version: str
    :param location: The Azure region of the operation
    :type location: str
    :param parameters: Requested name to validate
    :type parameters: dict | bytes

    """
    parameters = ServicesCheckNameAvailabilityRequest.from_dict(parameters)
    return web.Response(status=200)


async def services_check_status_1(request: web.Request, subscription_id, group_name, service_name, api_version) -> web.Response:
    """Check service health status

    The services resource is the top-level resource that represents the Data Migration Service. This action performs a health check and returns the status of the service and virtual machine size.

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


async def services_start_1(request: web.Request, subscription_id, group_name, service_name, api_version) -> web.Response:
    """Start service

    The services resource is the top-level resource that represents the Data Migration Service. This action starts the service and the service can be used for data migration.

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


async def services_stop_1(request: web.Request, subscription_id, group_name, service_name, api_version) -> web.Response:
    """Stop service

    The services resource is the top-level resource that represents the Data Migration Service. This action stops the service and the service cannot be used for data migration. The service owner won&#39;t be billed when the service is stopped.

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


async def tasks_cancel_1(request: web.Request, subscription_id, group_name, service_name, project_name, task_name, api_version) -> web.Response:
    """Cancel a task

    The tasks resource is a nested, proxy-only resource representing work performed by a DMS instance. This method cancels a task if it&#39;s currently queued or running.

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

    """
    return web.Response(status=200)
