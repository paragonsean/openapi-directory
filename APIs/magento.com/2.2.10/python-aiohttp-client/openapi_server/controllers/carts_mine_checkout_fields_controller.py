from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.temando_shipping_quote_cart_checkout_field_management_v1_save_checkout_fields_post_request import TemandoShippingQuoteCartCheckoutFieldManagementV1SaveCheckoutFieldsPostRequest
from openapi_server import util


async def temando_shipping_quote_cart_checkout_field_management_v1_save_checkout_fields_post(request: web.Request, body=None) -> web.Response:
    """carts/mine/checkout-fields

    

    :param body: 
    :type body: dict | bytes

    """
    body = TemandoShippingQuoteCartCheckoutFieldManagementV1SaveCheckoutFieldsPostRequest.from_dict(body)
    return web.Response(status=200)
