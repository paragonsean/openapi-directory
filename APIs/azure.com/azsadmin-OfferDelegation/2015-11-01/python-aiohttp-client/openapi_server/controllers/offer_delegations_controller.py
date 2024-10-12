from typing import List, Dict
from aiohttp import web

from openapi_server.models.offer_delegation import OfferDelegation
from openapi_server.models.offer_delegation_list import OfferDelegationList
from openapi_server import util


async def offer_delegations_create_or_update(request: web.Request, subscription_id, resource_group_name, offer, offer_delegation_name, api_version, new_offer_delegation) -> web.Response:
    """offer_delegations_create_or_update

    Create or update the offer delegation.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The resource group the resource is located under.
    :type resource_group_name: str
    :param offer: Name of an offer.
    :type offer: str
    :param offer_delegation_name: Name of a offer delegation.
    :type offer_delegation_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param new_offer_delegation: New offer delegation parameter.
    :type new_offer_delegation: dict | bytes

    """
    new_offer_delegation = OfferDelegation.from_dict(new_offer_delegation)
    return web.Response(status=200)


async def offer_delegations_delete(request: web.Request, subscription_id, resource_group_name, offer, offer_delegation_name, api_version) -> web.Response:
    """offer_delegations_delete

    Delete the specified offer delegation.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The resource group the resource is located under.
    :type resource_group_name: str
    :param offer: Name of an offer.
    :type offer: str
    :param offer_delegation_name: Name of a offer delegation.
    :type offer_delegation_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def offer_delegations_get(request: web.Request, subscription_id, resource_group_name, offer, offer_delegation_name, api_version) -> web.Response:
    """offer_delegations_get

    Get the specified offer delegation.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The resource group the resource is located under.
    :type resource_group_name: str
    :param offer: Name of an offer.
    :type offer: str
    :param offer_delegation_name: Name of a offer delegation.
    :type offer_delegation_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def offer_delegations_list(request: web.Request, subscription_id, resource_group_name, offer, api_version) -> web.Response:
    """offer_delegations_list

    Get the list of offer delegations.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The resource group the resource is located under.
    :type resource_group_name: str
    :param offer: Name of an offer.
    :type offer: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)
