from typing import List, Dict
from aiohttp import web

from openapi_server.models.checkout_totals_information_management_v1_calculate_post_request import CheckoutTotalsInformationManagementV1CalculatePostRequest
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.quote_data_totals_interface import QuoteDataTotalsInterface
from openapi_server import util


async def checkout_totals_information_management_v1_calculate_post(request: web.Request, body=None) -> web.Response:
    """carts/mine/totals-information

    Calculate quote totals based on address and shipping method.

    :param body: 
    :type body: dict | bytes

    """
    body = CheckoutTotalsInformationManagementV1CalculatePostRequest.from_dict(body)
    return web.Response(status=200)
