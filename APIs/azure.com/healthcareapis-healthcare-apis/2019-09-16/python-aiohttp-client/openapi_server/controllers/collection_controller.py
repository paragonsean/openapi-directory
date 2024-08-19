from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_details import ErrorDetails
from openapi_server.models.services_description_list_result import ServicesDescriptionListResult
from openapi_server import util


async def services_list(request: web.Request, api_version, subscription_id) -> web.Response:
    """services_list

    Get all the service instances in a subscription.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: The subscription identifier.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def services_list_by_resource_group(request: web.Request, api_version, subscription_id, resource_group_name) -> web.Response:
    """services_list_by_resource_group

    Get all the service instances in a resource group.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the service instance.
    :type resource_group_name: str

    """
    return web.Response(status=200)
