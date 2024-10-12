from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def translate_klingon_get(request: web.Request, text) -> web.Response:
    """translate_klingon_get

    Translate from English to Startrek Klingon Language.

    :param text: Text to translate
    :type text: str

    """
    return web.Response(status=200)


async def translate_vulcan_get(request: web.Request, text) -> web.Response:
    """translate_vulcan_get

    Translate from English to Startrek Vulcan Language.

    :param text: Text to translate
    :type text: str

    """
    return web.Response(status=200)
