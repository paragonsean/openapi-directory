from typing import List, Dict
from aiohttp import web

from openapi_server.models.delegated_provider_offer import DelegatedProviderOffer
from openapi_server.models.delegated_provider_offer_list import DelegatedProviderOfferList
from openapi_server import util


async def delegated_provider_offers_get(request: web.Request, subscription_id, delegated_provider_subscription_id, offer, api_version) -> web.Response:
    """delegated_provider_offers_get

    Get the specified delegated provider offer.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param delegated_provider_subscription_id: Delegated provider subscription identifier.
    :type delegated_provider_subscription_id: str
    :param offer: Name of an offer.
    :type offer: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def delegated_provider_offers_list(request: web.Request, subscription_id, delegated_provider_subscription_id, api_version) -> web.Response:
    """delegated_provider_offers_list

    Get the list of delegated provider offers.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param delegated_provider_subscription_id: Delegated provider subscription identifier.
    :type delegated_provider_subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)
