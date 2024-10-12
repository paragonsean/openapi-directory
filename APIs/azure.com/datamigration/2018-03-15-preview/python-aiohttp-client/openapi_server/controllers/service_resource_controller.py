from typing import List, Dict
from aiohttp import web

from openapi_server.models.operations_list_default_response import OperationsListDefaultResponse
from openapi_server.models.services_check_status200_response import ServicesCheckStatus200Response
from openapi_server.models.services_get200_response import ServicesGet200Response
from openapi_server.models.services_list200_response import ServicesList200Response
from openapi_server.models.services_list_skus200_response import ServicesListSkus200Response
from openapi_server.models.tasks_list200_response import TasksList200Response
from openapi_server import util


async def services_check_status(request: web.Request, subscription_id, group_name, service_name, api_version) -> web.Response:
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


async def services_create_or_update(request: web.Request, subscription_id, group_name, service_name, api_version, parameters) -> web.Response:
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


async def services_delete(request: web.Request, subscription_id, group_name, service_name, api_version, delete_running_tasks=None) -> web.Response:
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


async def services_get(request: web.Request, subscription_id, group_name, service_name, api_version) -> web.Response:
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


async def services_list(request: web.Request, subscription_id, api_version) -> web.Response:
    """Get services in subscription

    The services resource is the top-level resource that represents the Data Migration Service. This method returns a list of service resources in a subscription.

    :param subscription_id: Identifier of the subscription
    :type subscription_id: str
    :param api_version: Version of the API
    :type api_version: str

    """
    return web.Response(status=200)


async def services_list_by_resource_group(request: web.Request, subscription_id, group_name, api_version) -> web.Response:
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


async def services_list_skus(request: web.Request, subscription_id, group_name, service_name, api_version) -> web.Response:
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


async def services_start(request: web.Request, subscription_id, group_name, service_name, api_version) -> web.Response:
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


async def services_stop(request: web.Request, subscription_id, group_name, service_name, api_version) -> web.Response:
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


async def services_update(request: web.Request, subscription_id, group_name, service_name, api_version, parameters) -> web.Response:
    """Create or update DMS Service Instance

    The services resource is the top-level resource that represents the Data Migration Service. The PATCH method updates an existing service. This method can change the kind, SKU, and network of the service, but if tasks are currently running (i.e. the service is busy), this will fail with 400 Bad Request (\&quot;ServiceIsBusy\&quot;).

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


async def tasks_list(request: web.Request, subscription_id, group_name, service_name, project_name, api_version, task_type=None) -> web.Response:
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
