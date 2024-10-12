from typing import List, Dict
from aiohttp import web

from openapi_server.models.ai_alpha_search_messages200_response import AiAlphaSearchMessages200Response
from openapi_server.models.search_request import SearchRequest
from openapi_server import util


async def ai_alpha_search_messages(request: web.Request, body) -> web.Response:
    """ai_alpha_search_messages

    Search for messages matching a query

    :param body: 
    :type body: dict | bytes

    """
    body = SearchRequest.from_dict(body)
    return web.Response(status=200)
