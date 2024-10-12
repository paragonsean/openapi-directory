from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def translate_piglatin_get(request: web.Request, text) -> web.Response:
    """translate_piglatin_get

    Translate from English to Pig Latin.

    :param text: Text to translate
    :type text: str

    """
    return web.Response(status=200)
