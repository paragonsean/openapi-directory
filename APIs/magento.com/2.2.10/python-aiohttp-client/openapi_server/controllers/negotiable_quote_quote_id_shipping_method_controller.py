from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.negotiable_quote_negotiable_quote_shipping_management_v1_set_shipping_method_put_request import NegotiableQuoteNegotiableQuoteShippingManagementV1SetShippingMethodPutRequest
from openapi_server import util


async def negotiable_quote_negotiable_quote_shipping_management_v1_set_shipping_method_put(request: web.Request, quote_id, body=None) -> web.Response:
    """negotiableQuote/{quoteId}/shippingMethod

    Updates the shipping method on a negotiable quote.

    :param quote_id: Negotiable Quote id
    :type quote_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = NegotiableQuoteNegotiableQuoteShippingManagementV1SetShippingMethodPutRequest.from_dict(body)
    return web.Response(status=200)
