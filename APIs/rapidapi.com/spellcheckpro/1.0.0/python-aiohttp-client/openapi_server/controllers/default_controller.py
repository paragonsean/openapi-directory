from typing import List, Dict
from aiohttp import web

from openapi_server.models.check_spelling_russian_request import CheckSpellingRussianRequest
from openapi_server import util


async def check_spelling_russian(request: web.Request, x_rapid_api_key=None, body=None) -> web.Response:
    """Check Spelling (Russian)

    Check Spelling (Russian)

    :param x_rapid_api_key: 
    :type x_rapid_api_key: str
    :param body: 
    :type body: dict | bytes

    """
    body = CheckSpellingRussianRequest.from_dict(body)
    return web.Response(status=200)
