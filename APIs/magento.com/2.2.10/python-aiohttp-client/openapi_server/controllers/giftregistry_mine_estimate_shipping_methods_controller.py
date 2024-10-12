from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.gift_registry_shipping_method_management_v1_estimate_by_registry_id_post_request import GiftRegistryShippingMethodManagementV1EstimateByRegistryIdPostRequest
from openapi_server.models.quote_data_shipping_method_interface import QuoteDataShippingMethodInterface
from openapi_server import util


async def gift_registry_shipping_method_management_v1_estimate_by_registry_id_post(request: web.Request, body=None) -> web.Response:
    """giftregistry/mine/estimate-shipping-methods

    Estimate shipping

    :param body: 
    :type body: dict | bytes

    """
    body = GiftRegistryShippingMethodManagementV1EstimateByRegistryIdPostRequest.from_dict(body)
    return web.Response(status=200)
