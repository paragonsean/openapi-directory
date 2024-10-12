from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.peer_asn import PeerAsn
from openapi_server.models.peer_asn_list_result import PeerAsnListResult
from openapi_server import util


async def peer_asns_create_or_update(request: web.Request, peer_asn_name, subscription_id, api_version, peer_asn) -> web.Response:
    """peer_asns_create_or_update

    Creates a new peer ASN or updates an existing peer ASN with the specified name under the given subscription.

    :param peer_asn_name: The peer ASN name.
    :type peer_asn_name: str
    :param subscription_id: The Azure subscription ID.
    :type subscription_id: str
    :param api_version: The client API version.
    :type api_version: str
    :param peer_asn: The peer ASN.
    :type peer_asn: dict | bytes

    """
    peer_asn = PeerAsn.from_dict(peer_asn)
    return web.Response(status=200)


async def peer_asns_delete(request: web.Request, peer_asn_name, subscription_id, api_version) -> web.Response:
    """peer_asns_delete

    Deletes an existing peer ASN with the specified name under the given subscription.

    :param peer_asn_name: The peer ASN name.
    :type peer_asn_name: str
    :param subscription_id: The Azure subscription ID.
    :type subscription_id: str
    :param api_version: The client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def peer_asns_get(request: web.Request, peer_asn_name, subscription_id, api_version) -> web.Response:
    """peer_asns_get

    Gets the peer ASN with the specified name under the given subscription.

    :param peer_asn_name: The peer ASN name.
    :type peer_asn_name: str
    :param subscription_id: The Azure subscription ID.
    :type subscription_id: str
    :param api_version: The client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def peer_asns_list_by_subscription(request: web.Request, subscription_id, api_version) -> web.Response:
    """peer_asns_list_by_subscription

    Lists all of the peer ASNs under the given subscription.

    :param subscription_id: The Azure subscription ID.
    :type subscription_id: str
    :param api_version: The client API version.
    :type api_version: str

    """
    return web.Response(status=200)
