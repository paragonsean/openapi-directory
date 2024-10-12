from typing import List, Dict
from aiohttp import web

from openapi_server.models.pricing import Pricing
from openapi_server.models.pricing_list import PricingList
from openapi_server.models.pricings_list_default_response import PricingsListDefaultResponse
from openapi_server import util


async def pricings_get(request: web.Request, api_version, subscription_id, pricing_name) -> web.Response:
    """pricings_get

    Gets a provided Security Center pricing configuration in the subscription.

    :param api_version: API version for the operation
    :type api_version: str
    :param subscription_id: Azure subscription ID
    :type subscription_id: str
    :param pricing_name: name of the pricing configuration
    :type pricing_name: str

    """
    return web.Response(status=200)


async def pricings_list(request: web.Request, api_version, subscription_id) -> web.Response:
    """pricings_list

    Lists Security Center pricing configurations in the subscription.

    :param api_version: API version for the operation
    :type api_version: str
    :param subscription_id: Azure subscription ID
    :type subscription_id: str

    """
    return web.Response(status=200)


async def pricings_update(request: web.Request, api_version, subscription_id, pricing_name, pricing) -> web.Response:
    """pricings_update

    Updates a provided Security Center pricing configuration in the subscription.

    :param api_version: API version for the operation
    :type api_version: str
    :param subscription_id: Azure subscription ID
    :type subscription_id: str
    :param pricing_name: name of the pricing configuration
    :type pricing_name: str
    :param pricing: Pricing object
    :type pricing: dict | bytes

    """
    pricing = Pricing.from_dict(pricing)
    return web.Response(status=200)
