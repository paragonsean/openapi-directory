from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.peering_service_prefix import PeeringServicePrefix
from openapi_server.models.peering_service_prefix_list_result import PeeringServicePrefixListResult
from openapi_server import util


async def prefixes_create_or_update(request: web.Request, resource_group_name, peering_service_name, prefix_name, subscription_id, api_version, peering_service_prefix) -> web.Response:
    """prefixes_create_or_update

    Creates a new prefix with the specified name under the given subscription, resource group and peering service.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param peering_service_name: The name of the peering service.
    :type peering_service_name: str
    :param prefix_name: The name of the prefix.
    :type prefix_name: str
    :param subscription_id: The Azure subscription ID.
    :type subscription_id: str
    :param api_version: The client API version.
    :type api_version: str
    :param peering_service_prefix: The properties needed to create a prefix.
    :type peering_service_prefix: dict | bytes

    """
    peering_service_prefix = PeeringServicePrefix.from_dict(peering_service_prefix)
    return web.Response(status=200)


async def prefixes_delete(request: web.Request, resource_group_name, peering_service_name, prefix_name, subscription_id, api_version) -> web.Response:
    """prefixes_delete

    Deletes an existing prefix with the specified name under the given subscription, resource group and peering service.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param peering_service_name: The name of the peering service.
    :type peering_service_name: str
    :param prefix_name: The name of the prefix.
    :type prefix_name: str
    :param subscription_id: The Azure subscription ID.
    :type subscription_id: str
    :param api_version: The client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def prefixes_get(request: web.Request, resource_group_name, peering_service_name, prefix_name, subscription_id, api_version, expand=None) -> web.Response:
    """prefixes_get

    Gets an existing prefix with the specified name under the given subscription, resource group and peering service.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param peering_service_name: The name of the peering service.
    :type peering_service_name: str
    :param prefix_name: The name of the prefix.
    :type prefix_name: str
    :param subscription_id: The Azure subscription ID.
    :type subscription_id: str
    :param api_version: The client API version.
    :type api_version: str
    :param expand: The properties to be expanded.
    :type expand: str

    """
    return web.Response(status=200)


async def prefixes_list_by_peering_service(request: web.Request, resource_group_name, peering_service_name, subscription_id, api_version, expand=None) -> web.Response:
    """prefixes_list_by_peering_service

    Lists all prefixes under the given subscription, resource group and peering service.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param peering_service_name: The name of the peering service.
    :type peering_service_name: str
    :param subscription_id: The Azure subscription ID.
    :type subscription_id: str
    :param api_version: The client API version.
    :type api_version: str
    :param expand: The properties to be expanded.
    :type expand: str

    """
    return web.Response(status=200)
