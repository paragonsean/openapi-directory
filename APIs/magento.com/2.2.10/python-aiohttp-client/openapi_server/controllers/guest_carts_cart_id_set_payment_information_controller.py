from typing import List, Dict
from aiohttp import web

from openapi_server.models.checkout_guest_payment_information_management_v1_save_payment_information_and_place_order_post_request import CheckoutGuestPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPostRequest
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def checkout_guest_payment_information_management_v1_save_payment_information_post(request: web.Request, cart_id, body=None) -> web.Response:
    """guest-carts/{cartId}/set-payment-information

    Set payment information for a specified cart.

    :param cart_id: 
    :type cart_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CheckoutGuestPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPostRequest.from_dict(body)
    return web.Response(status=200)
