from typing import List, Dict
from aiohttp import web

from openapi_server.models.offer import Offer
from openapi_server.models.offer_list import OfferList
from openapi_server import util


async def delegated_provider_offers_get(request: web.Request, delegated_provider_id, offer_name, api_version) -> web.Response:
    """delegated_provider_offers_get

    Get the specified offer for the delegated provider.

    :param delegated_provider_id: Id of the delegated provider.
    :type delegated_provider_id: str
    :param offer_name: Name of the offer.
    :type offer_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def delegated_provider_offers_list(request: web.Request, delegated_provider_id, api_version) -> web.Response:
    """delegated_provider_offers_list

    Get the list of offers for the specified delegated provider.

    :param delegated_provider_id: Id of the delegated provider.
    :type delegated_provider_id: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)
