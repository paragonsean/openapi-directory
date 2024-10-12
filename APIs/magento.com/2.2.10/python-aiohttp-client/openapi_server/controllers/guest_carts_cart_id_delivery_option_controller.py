from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.temando_shipping_quote_cart_delivery_option_management_v1_save_post_request import TemandoShippingQuoteCartDeliveryOptionManagementV1SavePostRequest
from openapi_server import util


async def temando_shipping_quote_guest_cart_delivery_option_management_v1_save_post(request: web.Request, cart_id, body=None) -> web.Response:
    """guest-carts/{cartId}/delivery-option

    Handle selected delivery option.

    :param cart_id: The shopping cart ID.
    :type cart_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = TemandoShippingQuoteCartDeliveryOptionManagementV1SavePostRequest.from_dict(body)
    return web.Response(status=200)
