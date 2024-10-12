from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.temando_shipping_quote_cart_delivery_option_management_v1_save_post_request import TemandoShippingQuoteCartDeliveryOptionManagementV1SavePostRequest
from openapi_server import util


async def temando_shipping_quote_cart_delivery_option_management_v1_save_post(request: web.Request, body=None) -> web.Response:
    """carts/mine/delivery-option

    Handle selected delivery option.

    :param body: 
    :type body: dict | bytes

    """
    body = TemandoShippingQuoteCartDeliveryOptionManagementV1SavePostRequest.from_dict(body)
    return web.Response(status=200)
