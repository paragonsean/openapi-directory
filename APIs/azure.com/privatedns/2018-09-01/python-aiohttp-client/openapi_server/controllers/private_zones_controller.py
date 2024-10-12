from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.private_zone import PrivateZone
from openapi_server.models.private_zone_list_result import PrivateZoneListResult
from openapi_server import util


async def private_zones_create_or_update(request: web.Request, resource_group_name, private_zone_name, api_version, subscription_id, parameters, if_match=None, if_none_match=None) -> web.Response:
    """private_zones_create_or_update

    Creates or updates a Private DNS zone. Does not modify Links to virtual networks or DNS records within the zone.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param private_zone_name: The name of the Private DNS zone (without a terminating dot).
    :type private_zone_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to the CreateOrUpdate operation.
    :type parameters: dict | bytes
    :param if_match: The ETag of the Private DNS zone. Omit this value to always overwrite the current zone. Specify the last-seen ETag value to prevent accidentally overwriting any concurrent changes.
    :type if_match: str
    :param if_none_match: Set to &#39;*&#39; to allow a new Private DNS zone to be created, but to prevent updating an existing zone. Other values will be ignored.
    :type if_none_match: str

    """
    parameters = PrivateZone.from_dict(parameters)
    return web.Response(status=200)


async def private_zones_delete(request: web.Request, resource_group_name, private_zone_name, api_version, subscription_id, if_match=None) -> web.Response:
    """private_zones_delete

    Deletes a Private DNS zone. WARNING: All DNS records in the zone will also be deleted. This operation cannot be undone. Private DNS zone cannot be deleted unless all virtual network links to it are removed.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param private_zone_name: The name of the Private DNS zone (without a terminating dot).
    :type private_zone_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param if_match: The ETag of the Private DNS zone. Omit this value to always delete the current zone. Specify the last-seen ETag value to prevent accidentally deleting any concurrent changes.
    :type if_match: str

    """
    return web.Response(status=200)


async def private_zones_get(request: web.Request, resource_group_name, private_zone_name, api_version, subscription_id) -> web.Response:
    """private_zones_get

    Gets a Private DNS zone. Retrieves the zone properties, but not the virtual networks links or the record sets within the zone.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param private_zone_name: The name of the Private DNS zone (without a terminating dot).
    :type private_zone_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def private_zones_list(request: web.Request, api_version, subscription_id, top=None) -> web.Response:
    """private_zones_list

    Lists the Private DNS zones in all resource groups in a subscription.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param top: The maximum number of Private DNS zones to return. If not specified, returns up to 100 zones.
    :type top: int

    """
    return web.Response(status=200)


async def private_zones_list_by_resource_group(request: web.Request, resource_group_name, api_version, subscription_id, top=None) -> web.Response:
    """private_zones_list_by_resource_group

    Lists the Private DNS zones within a resource group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param top: The maximum number of record sets to return. If not specified, returns up to 100 record sets.
    :type top: int

    """
    return web.Response(status=200)


async def private_zones_update(request: web.Request, resource_group_name, private_zone_name, api_version, subscription_id, parameters, if_match=None) -> web.Response:
    """private_zones_update

    Updates a Private DNS zone. Does not modify virtual network links or DNS records within the zone.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param private_zone_name: The name of the Private DNS zone (without a terminating dot).
    :type private_zone_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to the Update operation.
    :type parameters: dict | bytes
    :param if_match: The ETag of the Private DNS zone. Omit this value to always overwrite the current zone. Specify the last-seen ETag value to prevent accidentally overwriting any concurrent changes.
    :type if_match: str

    """
    parameters = PrivateZone.from_dict(parameters)
    return web.Response(status=200)
