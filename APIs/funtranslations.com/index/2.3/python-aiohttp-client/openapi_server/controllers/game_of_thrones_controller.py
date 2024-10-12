from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def translate_dothraki_get(request: web.Request, text) -> web.Response:
    """translate_dothraki_get

    Translate from English to Dothraki.

    :param text: Text to translate
    :type text: str

    """
    return web.Response(status=200)


async def translate_valyrian_get(request: web.Request, text) -> web.Response:
    """translate_valyrian_get

    Translate from English to Valyrian.

    :param text: Text to translate
    :type text: str

    """
    return web.Response(status=200)
