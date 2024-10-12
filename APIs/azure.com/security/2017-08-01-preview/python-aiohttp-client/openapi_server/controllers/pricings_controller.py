from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.pricing import Pricing
from openapi_server.models.pricing_list import PricingList
from openapi_server import util


async def pricings_create_or_update_resource_group_pricing(request: web.Request, api_version, subscription_id, resource_group_name, pricing_name, pricing) -> web.Response:
    """pricings_create_or_update_resource_group_pricing

    Security pricing configuration in the resource group

    :param api_version: API version for the operation
    :type api_version: str
    :param subscription_id: Azure subscription ID
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the user&#39;s subscription. The name is case insensitive.
    :type resource_group_name: str
    :param pricing_name: name of the pricing configuration
    :type pricing_name: str
    :param pricing: Pricing object
    :type pricing: dict | bytes

    """
    pricing = Pricing.from_dict(pricing)
    return web.Response(status=200)


async def pricings_get_resource_group_pricing(request: web.Request, api_version, subscription_id, resource_group_name, pricing_name) -> web.Response:
    """pricings_get_resource_group_pricing

    Security pricing configuration in the resource group

    :param api_version: API version for the operation
    :type api_version: str
    :param subscription_id: Azure subscription ID
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the user&#39;s subscription. The name is case insensitive.
    :type resource_group_name: str
    :param pricing_name: name of the pricing configuration
    :type pricing_name: str

    """
    return web.Response(status=200)


async def pricings_get_subscription_pricing(request: web.Request, api_version, subscription_id, pricing_name) -> web.Response:
    """pricings_get_subscription_pricing

    Security pricing configuration in the subscriptionSecurity pricing configuration in the subscription

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

    Security pricing configurations in the subscription

    :param api_version: API version for the operation
    :type api_version: str
    :param subscription_id: Azure subscription ID
    :type subscription_id: str

    """
    return web.Response(status=200)


async def pricings_list_by_resource_group(request: web.Request, api_version, subscription_id, resource_group_name) -> web.Response:
    """pricings_list_by_resource_group

    Security pricing configurations in the resource group

    :param api_version: API version for the operation
    :type api_version: str
    :param subscription_id: Azure subscription ID
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the user&#39;s subscription. The name is case insensitive.
    :type resource_group_name: str

    """
    return web.Response(status=200)


async def pricings_update_subscription_pricing(request: web.Request, api_version, subscription_id, pricing_name, pricing) -> web.Response:
    """pricings_update_subscription_pricing

    Security pricing configuration in the subscription

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
