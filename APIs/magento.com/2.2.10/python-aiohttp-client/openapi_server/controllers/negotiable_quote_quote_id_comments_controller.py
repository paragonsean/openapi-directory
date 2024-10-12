from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.negotiable_quote_data_comment_interface import NegotiableQuoteDataCommentInterface
from openapi_server import util


async def negotiable_quote_comment_locator_v1_get_list_for_quote_get(request: web.Request, quote_id) -> web.Response:
    """negotiableQuote/{quoteId}/comments

    Returns comments for a specified negotiable quote.

    :param quote_id: Negotiable Quote ID.
    :type quote_id: int

    """
    return web.Response(status=200)
