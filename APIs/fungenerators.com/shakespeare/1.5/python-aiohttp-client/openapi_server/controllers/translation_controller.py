from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def shakespeare_translate_get(request: web.Request, text) -> web.Response:
    """shakespeare_translate_get

    Translate from English to Shakespeare English.

    :param text: Text to translate to Shakespeare English.
    :type text: str

    """
    return web.Response(status=200)
