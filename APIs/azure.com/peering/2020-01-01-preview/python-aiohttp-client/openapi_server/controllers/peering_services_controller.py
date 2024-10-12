from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.peering_service import PeeringService
from openapi_server.models.peering_service_list_result import PeeringServiceListResult
from openapi_server.models.resource_tags import ResourceTags
from openapi_server import util


async def peering_services_create_or_update(request: web.Request, resource_group_name, peering_service_name, subscription_id, api_version, peering_service) -> web.Response:
    """peering_services_create_or_update

    Creates a new peering service or updates an existing peering with the specified name under the given subscription and resource group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param peering_service_name: The name of the peering service.
    :type peering_service_name: str
    :param subscription_id: The Azure subscription ID.
    :type subscription_id: str
    :param api_version: The client API version.
    :type api_version: str
    :param peering_service: The properties needed to create or update a peering service.
    :type peering_service: dict | bytes

    """
    peering_service = PeeringService.from_dict(peering_service)
    return web.Response(status=200)


async def peering_services_delete(request: web.Request, resource_group_name, peering_service_name, subscription_id, api_version) -> web.Response:
    """peering_services_delete

    Deletes an existing peering service with the specified name under the given subscription and resource group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param peering_service_name: The name of the peering service.
    :type peering_service_name: str
    :param subscription_id: The Azure subscription ID.
    :type subscription_id: str
    :param api_version: The client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def peering_services_get(request: web.Request, resource_group_name, peering_service_name, subscription_id, api_version) -> web.Response:
    """peering_services_get

    Gets an existing peering service with the specified name under the given subscription and resource group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param peering_service_name: The name of the peering.
    :type peering_service_name: str
    :param subscription_id: The Azure subscription ID.
    :type subscription_id: str
    :param api_version: The client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def peering_services_list_by_resource_group(request: web.Request, resource_group_name, subscription_id, api_version) -> web.Response:
    """peering_services_list_by_resource_group

    Lists all of the peering services under the given subscription and resource group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param subscription_id: The Azure subscription ID.
    :type subscription_id: str
    :param api_version: The client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def peering_services_list_by_subscription(request: web.Request, subscription_id, api_version) -> web.Response:
    """peering_services_list_by_subscription

    Lists all of the peerings under the given subscription.

    :param subscription_id: The Azure subscription ID.
    :type subscription_id: str
    :param api_version: The client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def peering_services_update(request: web.Request, resource_group_name, peering_service_name, subscription_id, api_version, tags) -> web.Response:
    """peering_services_update

    Updates tags for a peering service with the specified name under the given subscription and resource group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param peering_service_name: The name of the peering service.
    :type peering_service_name: str
    :param subscription_id: The Azure subscription ID.
    :type subscription_id: str
    :param api_version: The client API version.
    :type api_version: str
    :param tags: The resource tags.
    :type tags: dict | bytes

    """
    tags = ResourceTags.from_dict(tags)
    return web.Response(status=200)
