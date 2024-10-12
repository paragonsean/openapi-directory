from typing import List, Dict
from aiohttp import web

from openapi_server.models.suggest_request import SuggestRequest
from openapi_server.models.suggest_result import SuggestResult
from openapi_server import util


async def get_suggestions(request: web.Request, body, max_results=None) -> web.Response:
    """Query diagnostic engine for related symptoms

    Suggests possible symptoms based on provided patient information.

    :param body: 
    :type body: dict | bytes
    :param max_results: maximum number of results
    :type max_results: int

    """
    body = SuggestRequest.from_dict(body)
    return web.Response(status=200)
