from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.quote_data_shipping_method_interface import QuoteDataShippingMethodInterface
from openapi_server.models.quote_shipping_method_management_v1_estimate_by_address_id_post_request import QuoteShippingMethodManagementV1EstimateByAddressIdPostRequest
from openapi_server import util


async def negotiable_quote_shipping_method_management_v1_estimate_by_address_id_post(request: web.Request, cart_id, body=None) -> web.Response:
    """negotiable-carts/{cartId}/estimate-shipping-methods-by-address-id

    Estimate shipping

    :param cart_id: The shopping cart ID.
    :type cart_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = QuoteShippingMethodManagementV1EstimateByAddressIdPostRequest.from_dict(body)
    return web.Response(status=200)
