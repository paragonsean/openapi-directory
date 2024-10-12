from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.peering_registered_asn import PeeringRegisteredAsn
from openapi_server.models.peering_registered_asn_list_result import PeeringRegisteredAsnListResult
from openapi_server import util


async def registered_asns_create_or_update(request: web.Request, resource_group_name, peering_name, registered_asn_name, subscription_id, api_version, registered_asn) -> web.Response:
    """registered_asns_create_or_update

    Creates a new registered ASN with the specified name under the given subscription, resource group and peering.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param peering_name: The name of the peering.
    :type peering_name: str
    :param registered_asn_name: The name of the ASN.
    :type registered_asn_name: str
    :param subscription_id: The Azure subscription ID.
    :type subscription_id: str
    :param api_version: The client API version.
    :type api_version: str
    :param registered_asn: The properties needed to create a registered ASN.
    :type registered_asn: dict | bytes

    """
    registered_asn = PeeringRegisteredAsn.from_dict(registered_asn)
    return web.Response(status=200)


async def registered_asns_delete(request: web.Request, resource_group_name, peering_name, registered_asn_name, subscription_id, api_version) -> web.Response:
    """registered_asns_delete

    Deletes an existing registered ASN with the specified name under the given subscription, resource group and peering.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param peering_name: The name of the peering.
    :type peering_name: str
    :param registered_asn_name: The name of the registered ASN.
    :type registered_asn_name: str
    :param subscription_id: The Azure subscription ID.
    :type subscription_id: str
    :param api_version: The client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def registered_asns_get(request: web.Request, resource_group_name, peering_name, registered_asn_name, subscription_id, api_version) -> web.Response:
    """registered_asns_get

    Gets an existing registered ASN with the specified name under the given subscription, resource group and peering.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param peering_name: The name of the peering.
    :type peering_name: str
    :param registered_asn_name: The name of the registered ASN.
    :type registered_asn_name: str
    :param subscription_id: The Azure subscription ID.
    :type subscription_id: str
    :param api_version: The client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def registered_asns_list_by_peering(request: web.Request, resource_group_name, peering_name, subscription_id, api_version) -> web.Response:
    """registered_asns_list_by_peering

    Lists all registered ASNs under the given subscription, resource group and peering.

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
