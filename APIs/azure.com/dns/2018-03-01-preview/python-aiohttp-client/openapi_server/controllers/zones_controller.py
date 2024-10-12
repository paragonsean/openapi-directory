from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.zone import Zone
from openapi_server.models.zone_list_result import ZoneListResult
from openapi_server.models.zone_update import ZoneUpdate
from openapi_server import util


async def zones_create_or_update(request: web.Request, resource_group_name, zone_name, api_version, subscription_id, parameters, if_match=None, if_none_match=None) -> web.Response:
    """zones_create_or_update

    Creates or updates a DNS zone. Does not modify DNS records within the zone.

    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param zone_name: The name of the DNS zone (without a terminating dot).
    :type zone_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param parameters: Parameters supplied to the CreateOrUpdate operation.
    :type parameters: dict | bytes
    :param if_match: The etag of the DNS zone. Omit this value to always overwrite the current zone. Specify the last-seen etag value to prevent accidentally overwriting any concurrent changes.
    :type if_match: str
    :param if_none_match: Set to &#39;*&#39; to allow a new DNS zone to be created, but to prevent updating an existing zone. Other values will be ignored.
    :type if_none_match: str

    """
    parameters = Zone.from_dict(parameters)
    return web.Response(status=200)


async def zones_delete(request: web.Request, resource_group_name, zone_name, api_version, subscription_id, if_match=None) -> web.Response:
    """zones_delete

    Deletes a DNS zone. WARNING: All DNS records in the zone will also be deleted. This operation cannot be undone.

    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param zone_name: The name of the DNS zone (without a terminating dot).
    :type zone_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param if_match: The etag of the DNS zone. Omit this value to always delete the current zone. Specify the last-seen etag value to prevent accidentally deleting any concurrent changes.
    :type if_match: str

    """
    return web.Response(status=200)


async def zones_get(request: web.Request, resource_group_name, zone_name, api_version, subscription_id) -> web.Response:
    """zones_get

    Gets a DNS zone. Retrieves the zone properties, but not the record sets within the zone.

    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param zone_name: The name of the DNS zone (without a terminating dot).
    :type zone_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def zones_list(request: web.Request, api_version, subscription_id, top=None) -> web.Response:
    """zones_list

    Lists the DNS zones in all resource groups in a subscription.

    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param top: The maximum number of DNS zones to return. If not specified, returns up to 100 zones.
    :type top: int

    """
    return web.Response(status=200)


async def zones_list_by_resource_group(request: web.Request, resource_group_name, api_version, subscription_id, top=None) -> web.Response:
    """zones_list_by_resource_group

    Lists the DNS zones within a resource group.

    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param top: The maximum number of record sets to return. If not specified, returns up to 100 record sets.
    :type top: int

    """
    return web.Response(status=200)


async def zones_update(request: web.Request, resource_group_name, zone_name, api_version, subscription_id, parameters, if_match=None) -> web.Response:
    """zones_update

    Updates a DNS zone. Does not modify DNS records within the zone.

    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param zone_name: The name of the DNS zone (without a terminating dot).
    :type zone_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param parameters: Parameters supplied to the Update operation.
    :type parameters: dict | bytes
    :param if_match: The etag of the DNS zone. Omit this value to always overwrite the current zone. Specify the last-seen etag value to prevent accidentally overwriting any concurrent changes.
    :type if_match: str

    """
    parameters = ZoneUpdate.from_dict(parameters)
    return web.Response(status=200)
