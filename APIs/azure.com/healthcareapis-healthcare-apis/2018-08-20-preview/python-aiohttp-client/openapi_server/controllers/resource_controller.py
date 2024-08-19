from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_details import ErrorDetails
from openapi_server.models.operation_results_description import OperationResultsDescription
from openapi_server.models.services_description import ServicesDescription
from openapi_server.models.services_patch_description import ServicesPatchDescription
from openapi_server import util


async def operation_results_get(request: web.Request, api_version, subscription_id, location_name, operation_result_id) -> web.Response:
    """operation_results_get

    Get the operation result for a long running operation.

    :param api_version: The version of the API.
    :type api_version: str
    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param location_name: The location of the operation.
    :type location_name: str
    :param operation_result_id: The ID of the operation result to get.
    :type operation_result_id: str

    """
    return web.Response(status=200)


async def services_create_or_update(request: web.Request, api_version, subscription_id, resource_group_name, resource_name, service_description) -> web.Response:
    """services_create_or_update

    Create or update the metadata of a service instance.

    :param api_version: The version of the API.
    :type api_version: str
    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the service instance.
    :type resource_group_name: str
    :param resource_name: The name of the service instance.
    :type resource_name: str
    :param service_description: The service instance metadata.
    :type service_description: dict | bytes

    """
    service_description = ServicesDescription.from_dict(service_description)
    return web.Response(status=200)


async def services_delete(request: web.Request, api_version, subscription_id, resource_group_name, resource_name) -> web.Response:
    """services_delete

    Delete a service instance.

    :param api_version: The version of the API.
    :type api_version: str
    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the service instance.
    :type resource_group_name: str
    :param resource_name: The name of the service instance.
    :type resource_name: str

    """
    return web.Response(status=200)


async def services_get(request: web.Request, api_version, subscription_id, resource_group_name, resource_name) -> web.Response:
    """services_get

    Get the metadata of a service instance.

    :param api_version: The version of the API.
    :type api_version: str
    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the service instance.
    :type resource_group_name: str
    :param resource_name: The name of the service instance.
    :type resource_name: str

    """
    return web.Response(status=200)


async def services_update(request: web.Request, api_version, subscription_id, resource_group_name, resource_name, service_patch_description) -> web.Response:
    """services_update

    Update the metadata of a service instance.

    :param api_version: The version of the API.
    :type api_version: str
    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the service instance.
    :type resource_group_name: str
    :param resource_name: The name of the service instance.
    :type resource_name: str
    :param service_patch_description: The service instance metadata and security metadata.
    :type service_patch_description: dict | bytes

    """
    service_patch_description = ServicesPatchDescription.from_dict(service_patch_description)
    return web.Response(status=200)
