from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def translate_quneya_get(request: web.Request, text) -> web.Response:
    """translate_quneya_get

    Translate from English to Elvish Quenya Language.

    :param text: Text to translate
    :type text: str

    """
    return web.Response(status=200)


async def translate_sindarin_get(request: web.Request, text) -> web.Response:
    """translate_sindarin_get

    Translate from English to Elvish Sindarin Language.

    :param text: Text to translate
    :type text: str

    """
    return web.Response(status=200)
