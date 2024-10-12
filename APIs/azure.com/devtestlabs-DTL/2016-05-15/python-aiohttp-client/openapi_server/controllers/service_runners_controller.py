from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.response_with_continuation_service_runner import ResponseWithContinuationServiceRunner
from openapi_server.models.service_runner import ServiceRunner
from openapi_server import util


async def service_runners_create_or_update(request: web.Request, subscription_id, resource_group_name, lab_name, name, api_version, service_runner) -> web.Response:
    """service_runners_create_or_update

    Create or replace an existing Service runner.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param name: The name of the service runner.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str
    :param service_runner: A container for a managed identity to execute DevTest lab services.
    :type service_runner: dict | bytes

    """
    service_runner = ServiceRunner.from_dict(service_runner)
    return web.Response(status=200)


async def service_runners_delete(request: web.Request, subscription_id, resource_group_name, lab_name, name, api_version) -> web.Response:
    """service_runners_delete

    Delete service runner.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param name: The name of the service runner.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def service_runners_get(request: web.Request, subscription_id, resource_group_name, lab_name, name, api_version) -> web.Response:
    """service_runners_get

    Get service runner.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param name: The name of the service runner.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def service_runners_list(request: web.Request, subscription_id, resource_group_name, lab_name, api_version, filter=None, top=None, orderby=None) -> web.Response:
    """service_runners_list

    List service runners in a given lab.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param filter: The filter to apply to the operation.
    :type filter: str
    :param top: The maximum number of resources to return from the operation.
    :type top: int
    :param orderby: The ordering expression for the results, using OData notation.
    :type orderby: str

    """
    return web.Response(status=200)
