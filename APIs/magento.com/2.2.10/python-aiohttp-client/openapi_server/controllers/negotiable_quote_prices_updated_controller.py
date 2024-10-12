from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.negotiable_quote_negotiable_quote_price_management_v1_prices_updated_post_request import NegotiableQuoteNegotiableQuotePriceManagementV1PricesUpdatedPostRequest
from openapi_server import util


async def negotiable_quote_negotiable_quote_price_management_v1_prices_updated_post(request: web.Request, body=None) -> web.Response:
    """negotiableQuote/pricesUpdated

    Refreshes item prices, taxes, discounts, cart rules in the negotiable quote as per the latest changes in the catalog / shared catalog and in the price rules. Depending on the negotiable quote state and totals, all or just some of quote numbers will be recalculated. &#39;Update Prices&#39; parameter forces refresh on any quote that is not locked for admin user, including the quotes with a negotiated price. The request can be applied to one or more quotes at the same time.

    :param body: 
    :type body: dict | bytes

    """
    body = NegotiableQuoteNegotiableQuotePriceManagementV1PricesUpdatedPostRequest.from_dict(body)
    return web.Response(status=200)
