from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.quote_cart_repository_v1_save_put_request import QuoteCartRepositoryV1SavePutRequest
from openapi_server import util


async def negotiable_quote_negotiable_cart_repository_v1_save_put(request: web.Request, quote_id, body=None) -> web.Response:
    """negotiableQuote/{quoteId}

    Save quote

    :param quote_id: 
    :type quote_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = QuoteCartRepositoryV1SavePutRequest.from_dict(body)
    return web.Response(status=200)
