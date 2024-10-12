from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def translate_ermahgerd_get(request: web.Request, text) -> web.Response:
    """translate_ermahgerd_get

    Translate from English to ERMAHGERD.

    :param text: Text to translate
    :type text: str

    """
    return web.Response(status=200)
