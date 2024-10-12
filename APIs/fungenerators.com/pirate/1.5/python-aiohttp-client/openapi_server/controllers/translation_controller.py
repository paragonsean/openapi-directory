from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def pirate_translate_get(request: web.Request, text) -> web.Response:
    """pirate_translate_get

    Translate from English to pirate.

    :param text: Text to translate to pirate lingo.
    :type text: str

    """
    return web.Response(status=200)
