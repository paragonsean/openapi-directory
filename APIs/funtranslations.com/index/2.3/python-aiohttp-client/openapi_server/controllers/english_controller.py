from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def translate_oldenglish_get(request: web.Request, text) -> web.Response:
    """translate_oldenglish_get

    Translate from English to Old English.

    :param text: Text to translate
    :type text: str

    """
    return web.Response(status=200)


async def translate_shakespeare_get(request: web.Request, text) -> web.Response:
    """translate_shakespeare_get

    Translate from English to Shakespeare English.

    :param text: Text to translate
    :type text: str

    """
    return web.Response(status=200)


async def translate_uk2us_get(request: web.Request, text) -> web.Response:
    """translate_uk2us_get

    Translate from UK English to US English.

    :param text: Text to translate
    :type text: str

    """
    return web.Response(status=200)


async def translate_us2uk_get(request: web.Request, text) -> web.Response:
    """translate_us2uk_get

    Translate from US English to UK English.

    :param text: Text to translate
    :type text: str

    """
    return web.Response(status=200)
