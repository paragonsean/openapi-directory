from typing import List, Dict
from aiohttp import web

from openapi_server.models.resource_health_metadata import ResourceHealthMetadata
from openapi_server.models.resource_health_metadata_collection import ResourceHealthMetadataCollection
from openapi_server.models.resource_health_metadata_list_default_response import ResourceHealthMetadataListDefaultResponse
from openapi_server import util


async def resource_health_metadata_get_by_site(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Gets the category of ResourceHealthMetadata to use for the given site

    Description for Gets the category of ResourceHealthMetadata to use for the given site

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def resource_health_metadata_get_by_site_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version) -> web.Response:
    """Gets the category of ResourceHealthMetadata to use for the given site

    Description for Gets the category of ResourceHealthMetadata to use for the given site

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param slot: Name of web app slot. If not specified then will default to production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def resource_health_metadata_list(request: web.Request, subscription_id, api_version) -> web.Response:
    """List all ResourceHealthMetadata for all sites in the subscription.

    Description for List all ResourceHealthMetadata for all sites in the subscription.

    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def resource_health_metadata_list_by_resource_group(request: web.Request, resource_group_name, subscription_id, api_version) -> web.Response:
    """List all ResourceHealthMetadata for all sites in the resource group in the subscription.

    Description for List all ResourceHealthMetadata for all sites in the resource group in the subscription.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def resource_health_metadata_list_by_site(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Gets the category of ResourceHealthMetadata to use for the given site as a collection

    Description for Gets the category of ResourceHealthMetadata to use for the given site as a collection

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of web app.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def resource_health_metadata_list_by_site_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version) -> web.Response:
    """Gets the category of ResourceHealthMetadata to use for the given site as a collection

    Description for Gets the category of ResourceHealthMetadata to use for the given site as a collection

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of web app.
    :type name: str
    :param slot: Name of web app slot. If not specified then will default to production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)
