from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.peering import Peering
from openapi_server.models.peering_list_result import PeeringListResult
from openapi_server.models.resource_tags import ResourceTags
from openapi_server import util


async def peerings_create_or_update(request: web.Request, resource_group_name, peering_name, subscription_id, api_version, peering) -> web.Response:
    """peerings_create_or_update

    Creates a new peering or updates an existing peering with the specified name under the given subscription and resource group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param peering_name: The name of the peering.
    :type peering_name: str
    :param subscription_id: The Azure subscription ID.
    :type subscription_id: str
    :param api_version: The client API version.
    :type api_version: str
    :param peering: The properties needed to create or update a peering.
    :type peering: dict | bytes

    """
    peering = Peering.from_dict(peering)
    return web.Response(status=200)


async def peerings_delete(request: web.Request, resource_group_name, peering_name, subscription_id, api_version) -> web.Response:
    """peerings_delete

    Deletes an existing peering with the specified name under the given subscription and resource group.

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


async def peerings_get(request: web.Request, resource_group_name, peering_name, subscription_id, api_version) -> web.Response:
    """peerings_get

    Gets an existing peering with the specified name under the given subscription and resource group.

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


async def peerings_list_by_resource_group(request: web.Request, resource_group_name, subscription_id, api_version) -> web.Response:
    """peerings_list_by_resource_group

    Lists all of the peerings under the given subscription and resource group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param subscription_id: The Azure subscription ID.
    :type subscription_id: str
    :param api_version: The client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def peerings_list_by_subscription(request: web.Request, subscription_id, api_version) -> web.Response:
    """peerings_list_by_subscription

    Lists all of the peerings under the given subscription.

    :param subscription_id: The Azure subscription ID.
    :type subscription_id: str
    :param api_version: The client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def peerings_update(request: web.Request, resource_group_name, peering_name, subscription_id, api_version, tags) -> web.Response:
    """peerings_update

    Updates tags for a peering with the specified name under the given subscription and resource group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param peering_name: The name of the peering.
    :type peering_name: str
    :param subscription_id: The Azure subscription ID.
    :type subscription_id: str
    :param api_version: The client API version.
    :type api_version: str
    :param tags: The resource tags.
    :type tags: dict | bytes

    """
    tags = ResourceTags.from_dict(tags)
    return web.Response(status=200)
