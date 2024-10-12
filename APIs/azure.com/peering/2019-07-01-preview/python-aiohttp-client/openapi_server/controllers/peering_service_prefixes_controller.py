from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.peering_service_prefix import PeeringServicePrefix
from openapi_server.models.peering_service_prefix_list_result import PeeringServicePrefixListResult
from openapi_server import util


async def peering_service_prefixes_create_or_update(request: web.Request, resource_group_name, peering_service_name, prefix_name, subscription_id, api_version, peering_service_prefix) -> web.Response:
    """peering_service_prefixes_create_or_update

    Creates or updates the peering prefix.

    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param peering_service_name: The peering service name.
    :type peering_service_name: str
    :param prefix_name: The prefix name
    :type prefix_name: str
    :param subscription_id: The Azure subscription ID.
    :type subscription_id: str
    :param api_version: The client API version.
    :type api_version: str
    :param peering_service_prefix: The IP prefix for an peering
    :type peering_service_prefix: dict | bytes

    """
    peering_service_prefix = PeeringServicePrefix.from_dict(peering_service_prefix)
    return web.Response(status=200)


async def peering_service_prefixes_delete(request: web.Request, resource_group_name, peering_service_name, prefix_name, subscription_id, api_version) -> web.Response:
    """peering_service_prefixes_delete

    removes the peering prefix.

    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param peering_service_name: The peering service name.
    :type peering_service_name: str
    :param prefix_name: The prefix name
    :type prefix_name: str
    :param subscription_id: The Azure subscription ID.
    :type subscription_id: str
    :param api_version: The client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def peering_service_prefixes_get(request: web.Request, resource_group_name, peering_service_name, prefix_name, subscription_id, api_version) -> web.Response:
    """peering_service_prefixes_get

    Gets the peering service prefix.

    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param peering_service_name: The peering service name.
    :type peering_service_name: str
    :param prefix_name: The prefix name.
    :type prefix_name: str
    :param subscription_id: The Azure subscription ID.
    :type subscription_id: str
    :param api_version: The client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def prefixes_list_by_peering_service(request: web.Request, resource_group_name, peering_service_name, subscription_id, api_version) -> web.Response:
    """prefixes_list_by_peering_service

    Lists the peerings prefix in the resource group.

    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param peering_service_name: The peering service name.
    :type peering_service_name: str
    :param subscription_id: The Azure subscription ID.
    :type subscription_id: str
    :param api_version: The client API version.
    :type api_version: str

    """
    return web.Response(status=200)
