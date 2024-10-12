from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.negotiable_quote_negotiable_quote_management_v1_create_post_request import NegotiableQuoteNegotiableQuoteManagementV1CreatePostRequest
from openapi_server import util


async def negotiable_quote_negotiable_quote_management_v1_create_post(request: web.Request, body=None) -> web.Response:
    """negotiableQuote/request

    Create a B2B quote based on a regular Magento quote. If the B2B quote requires a shipping address (for negotiation or tax calculations), add it to the regular quote before you create a B2B quote.

    :param body: 
    :type body: dict | bytes

    """
    body = NegotiableQuoteNegotiableQuoteManagementV1CreatePostRequest.from_dict(body)
    return web.Response(status=200)
