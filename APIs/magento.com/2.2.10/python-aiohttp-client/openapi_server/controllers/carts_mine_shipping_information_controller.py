from typing import List, Dict
from aiohttp import web

from openapi_server.models.checkout_data_payment_details_interface import CheckoutDataPaymentDetailsInterface
from openapi_server.models.checkout_shipping_information_management_v1_save_address_information_post_request import CheckoutShippingInformationManagementV1SaveAddressInformationPostRequest
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def checkout_shipping_information_management_v1_save_address_information_post(request: web.Request, body=None) -> web.Response:
    """carts/mine/shipping-information

    

    :param body: 
    :type body: dict | bytes

    """
    body = CheckoutShippingInformationManagementV1SaveAddressInformationPostRequest.from_dict(body)
    return web.Response(status=200)
