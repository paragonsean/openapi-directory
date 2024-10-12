from typing import List, Dict
from aiohttp import web

from openapi_server.models.checkout_totals_information_management_v1_calculate_post_request import CheckoutTotalsInformationManagementV1CalculatePostRequest
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.quote_data_totals_interface import QuoteDataTotalsInterface
from openapi_server import util


async def v1_carts_cart_id_totals_information_post(request: web.Request, cart_id, body=None) -> web.Response:
    """carts/{cartId}/totals-information

    Calculate quote totals based on address and shipping method.

    :param cart_id: 
    :type cart_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = CheckoutTotalsInformationManagementV1CalculatePostRequest.from_dict(body)
    return web.Response(status=200)
