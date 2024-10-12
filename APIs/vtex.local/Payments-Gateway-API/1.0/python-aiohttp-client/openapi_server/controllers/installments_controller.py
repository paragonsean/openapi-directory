from typing import List, Dict
from aiohttp import web

from openapi_server.models.invalid_request_value import InvalidRequestValue
from openapi_server.models.valid_request import ValidRequest
from openapi_server import util


async def installmentsoptions(request: web.Request, request_value, x_provider_api_app_key, x_provider_api_app_token, content_type, accept, request_sales_channel=None, request_payment_details_0_id=None, request_payment_details_0_value=None, request_payment_details_0_bin=None) -> web.Response:
    """Installments options

    Returns the best installment options according to the informed params.

    :param request_value: 
    :type request_value: int
    :param x_provider_api_app_key: The AppKey configured by the merchant (optional configuration)
    :type x_provider_api_app_key: str
    :param x_provider_api_app_token: The AppToken configured by the merchant (optional configuration)
    :type x_provider_api_app_token: str
    :param content_type: The Media type of the body of the request.  Default value for payment provider protocol is application/json
    :type content_type: str
    :param accept: Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    :type accept: str
    :param request_sales_channel: 
    :type request_sales_channel: int
    :param request_payment_details_0_id: 
    :type request_payment_details_0_id: int
    :param request_payment_details_0_value: 
    :type request_payment_details_0_value: int
    :param request_payment_details_0_bin: 
    :type request_payment_details_0_bin: int

    """
    return web.Response(status=200)
