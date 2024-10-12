from typing import List, Dict
from aiohttp import web

from openapi_server.models.checkout_data_payment_details_interface import CheckoutDataPaymentDetailsInterface
from openapi_server.models.checkout_guest_payment_information_management_v1_save_payment_information_and_place_order_post_request import CheckoutGuestPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPostRequest
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def checkout_guest_payment_information_management_v1_get_payment_information_get(request: web.Request, cart_id) -> web.Response:
    """guest-carts/{cartId}/payment-information

    Get payment information

    :param cart_id: 
    :type cart_id: str

    """
    return web.Response(status=200)


async def checkout_guest_payment_information_management_v1_save_payment_information_and_place_order_post(request: web.Request, cart_id, body=None) -> web.Response:
    """guest-carts/{cartId}/payment-information

    Set payment information and place order for a specified cart.

    :param cart_id: 
    :type cart_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CheckoutGuestPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPostRequest.from_dict(body)
    return web.Response(status=200)
