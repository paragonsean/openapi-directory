from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.peering_registered_prefix import PeeringRegisteredPrefix
from openapi_server.models.peering_registered_prefix_list_result import PeeringRegisteredPrefixListResult
from openapi_server import util


async def registered_prefixes_create_or_update(request: web.Request, resource_group_name, peering_name, registered_prefix_name, subscription_id, api_version, registered_prefix) -> web.Response:
    """registered_prefixes_create_or_update

    Creates a new registered prefix with the specified name under the given subscription, resource group and peering.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param peering_name: The name of the peering.
    :type peering_name: str
    :param registered_prefix_name: The name of the registered prefix.
    :type registered_prefix_name: str
    :param subscription_id: The Azure subscription ID.
    :type subscription_id: str
    :param api_version: The client API version.
    :type api_version: str
    :param registered_prefix: The properties needed to create a registered prefix.
    :type registered_prefix: dict | bytes

    """
    registered_prefix = PeeringRegisteredPrefix.from_dict(registered_prefix)
    return web.Response(status=200)


async def registered_prefixes_delete(request: web.Request, resource_group_name, peering_name, registered_prefix_name, subscription_id, api_version) -> web.Response:
    """registered_prefixes_delete

    Deletes an existing registered prefix with the specified name under the given subscription, resource group and peering.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param peering_name: The name of the peering.
    :type peering_name: str
    :param registered_prefix_name: The name of the registered prefix.
    :type registered_prefix_name: str
    :param subscription_id: The Azure subscription ID.
    :type subscription_id: str
    :param api_version: The client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def registered_prefixes_get(request: web.Request, resource_group_name, peering_name, registered_prefix_name, subscription_id, api_version) -> web.Response:
    """registered_prefixes_get

    Gets an existing registered prefix with the specified name under the given subscription, resource group and peering.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param peering_name: The name of the peering.
    :type peering_name: str
    :param registered_prefix_name: The name of the registered prefix.
    :type registered_prefix_name: str
    :param subscription_id: The Azure subscription ID.
    :type subscription_id: str
    :param api_version: The client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def registered_prefixes_list_by_peering(request: web.Request, resource_group_name, peering_name, subscription_id, api_version) -> web.Response:
    """registered_prefixes_list_by_peering

    Lists all registered prefixes under the given subscription, resource group and peering.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param peering_name: The name of the peering.
    :type peering_name: str
    :param subscription_id: The Azure subscription ID.
    :type subscription_id: str
    :param api_version: The client API version.
    :type api_version: str

    """
    return web.Response(status=200)
