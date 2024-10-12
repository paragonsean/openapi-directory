from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.virtual_network_link import VirtualNetworkLink
from openapi_server.models.virtual_network_link_list_result import VirtualNetworkLinkListResult
from openapi_server import util


async def virtual_network_links_create_or_update(request: web.Request, resource_group_name, private_zone_name, virtual_network_link_name, api_version, subscription_id, parameters, if_match=None, if_none_match=None) -> web.Response:
    """virtual_network_links_create_or_update

    Creates or updates a virtual network link to the specified Private DNS zone.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param private_zone_name: The name of the Private DNS zone (without a terminating dot).
    :type private_zone_name: str
    :param virtual_network_link_name: The name of the virtual network link.
    :type virtual_network_link_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to the CreateOrUpdate operation.
    :type parameters: dict | bytes
    :param if_match: The ETag of the virtual network link to the Private DNS zone. Omit this value to always overwrite the current virtual network link. Specify the last-seen ETag value to prevent accidentally overwriting any concurrent changes.
    :type if_match: str
    :param if_none_match: Set to &#39;*&#39; to allow a new virtual network link to the Private DNS zone to be created, but to prevent updating an existing link. Other values will be ignored.
    :type if_none_match: str

    """
    parameters = VirtualNetworkLink.from_dict(parameters)
    return web.Response(status=200)


async def virtual_network_links_delete(request: web.Request, resource_group_name, private_zone_name, virtual_network_link_name, api_version, subscription_id, if_match=None) -> web.Response:
    """virtual_network_links_delete

    Deletes a virtual network link to the specified Private DNS zone. WARNING: In case of a registration virtual network, all auto-registered DNS records in the zone for the virtual network will also be deleted. This operation cannot be undone.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param private_zone_name: The name of the Private DNS zone (without a terminating dot).
    :type private_zone_name: str
    :param virtual_network_link_name: The name of the virtual network link.
    :type virtual_network_link_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param if_match: The ETag of the virtual network link to the Private DNS zone. Omit this value to always delete the current zone. Specify the last-seen ETag value to prevent accidentally deleting any concurrent changes.
    :type if_match: str

    """
    return web.Response(status=200)


async def virtual_network_links_get(request: web.Request, resource_group_name, private_zone_name, virtual_network_link_name, api_version, subscription_id) -> web.Response:
    """virtual_network_links_get

    Gets a virtual network link to the specified Private DNS zone.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param private_zone_name: The name of the Private DNS zone (without a terminating dot).
    :type private_zone_name: str
    :param virtual_network_link_name: The name of the virtual network link.
    :type virtual_network_link_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def virtual_network_links_list(request: web.Request, resource_group_name, private_zone_name, api_version, subscription_id, top=None) -> web.Response:
    """virtual_network_links_list

    Lists the virtual network links to the specified Private DNS zone.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param private_zone_name: The name of the Private DNS zone (without a terminating dot).
    :type private_zone_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param top: The maximum number of virtual network links to return. If not specified, returns up to 100 virtual network links.
    :type top: int

    """
    return web.Response(status=200)


async def virtual_network_links_update(request: web.Request, resource_group_name, private_zone_name, virtual_network_link_name, api_version, subscription_id, parameters, if_match=None) -> web.Response:
    """virtual_network_links_update

    Updates a virtual network link to the specified Private DNS zone.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param private_zone_name: The name of the Private DNS zone (without a terminating dot).
    :type private_zone_name: str
    :param virtual_network_link_name: The name of the virtual network link.
    :type virtual_network_link_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to the Update operation.
    :type parameters: dict | bytes
    :param if_match: The ETag of the virtual network link to the Private DNS zone. Omit this value to always overwrite the current virtual network link. Specify the last-seen ETag value to prevent accidentally overwriting any concurrent changes.
    :type if_match: str

    """
    parameters = VirtualNetworkLink.from_dict(parameters)
    return web.Response(status=200)
