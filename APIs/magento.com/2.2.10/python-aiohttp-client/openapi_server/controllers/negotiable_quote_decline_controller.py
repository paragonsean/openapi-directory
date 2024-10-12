from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.negotiable_quote_negotiable_quote_management_v1_decline_post_request import NegotiableQuoteNegotiableQuoteManagementV1DeclinePostRequest
from openapi_server import util


async def negotiable_quote_negotiable_quote_management_v1_decline_post(request: web.Request, body=None) -> web.Response:
    """negotiableQuote/decline

    Decline the B2B quote. All custom pricing will be removed from this quote. The buyer will be able to place an order using their standard catalog prices and discounts.

    :param body: 
    :type body: dict | bytes

    """
    body = NegotiableQuoteNegotiableQuoteManagementV1DeclinePostRequest.from_dict(body)
    return web.Response(status=200)
