from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.temando_shipping_quote_cart_checkout_field_management_v1_save_checkout_fields_post_request import TemandoShippingQuoteCartCheckoutFieldManagementV1SaveCheckoutFieldsPostRequest
from openapi_server import util


async def temando_shipping_quote_guest_cart_checkout_field_management_v1_save_checkout_fields_post(request: web.Request, cart_id, body=None) -> web.Response:
    """guest-carts/{cartId}/checkout-fields

    

    :param cart_id: 
    :type cart_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = TemandoShippingQuoteCartCheckoutFieldManagementV1SaveCheckoutFieldsPostRequest.from_dict(body)
    return web.Response(status=200)
