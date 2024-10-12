from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.negotiable_quote_negotiable_quote_management_v1_admin_send_post_request import NegotiableQuoteNegotiableQuoteManagementV1AdminSendPostRequest
from openapi_server import util


async def negotiable_quote_negotiable_quote_management_v1_admin_send_post(request: web.Request, body=None) -> web.Response:
    """negotiableQuote/submitToCustomer

    Submit the B2B quote to the customer. The quote status for the customer will be changed to &#39;Updated&#39;, and the customer can work with the quote.

    :param body: 
    :type body: dict | bytes

    """
    body = NegotiableQuoteNegotiableQuoteManagementV1AdminSendPostRequest.from_dict(body)
    return web.Response(status=200)
