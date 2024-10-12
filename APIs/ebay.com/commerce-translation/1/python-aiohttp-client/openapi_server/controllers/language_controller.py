from typing import List, Dict
from aiohttp import web

from openapi_server.models.translate400_response import Translate400Response
from openapi_server.models.translate_request import TranslateRequest
from openapi_server.models.translate_response import TranslateResponse
from openapi_server import util


async def translate(request: web.Request, body) -> web.Response:
    """translate

    Translates input text inot a given language.

    :param body: 
    :type body: dict | bytes

    """
    body = TranslateRequest.from_dict(body)
    return web.Response(status=200)
