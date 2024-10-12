from typing import List, Dict
from aiohttp import web

from openapi_server.models.bill_pay_request import BillPayRequest
from openapi_server.models.bill_pay_response import BillPayResponse
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def is_routing_valid_post(request: web.Request, bill_pay_request=None) -> web.Response:
    """Bill Payment Validator service returns the processing status for a potential RPPS transaction

    Bill Payment Validator performs real time transaction validation against the specified Biller ID&#39;s account masks, account check digits and all other registered RPPS processing parameters.

    :param bill_pay_request: Contains the details of the get PAR API request message.
    :type bill_pay_request: dict | bytes

    """
    bill_pay_request = BillPayRequest.from_dict(bill_pay_request)
    return web.Response(status=200)
