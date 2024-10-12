from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def translate_brooklyn_get(request: web.Request, text) -> web.Response:
    """translate_brooklyn_get

    Translate from English to Brooklyn Speak.

    :param text: Text to translate
    :type text: str

    """
    return web.Response(status=200)


async def translate_cockney_get(request: web.Request, text) -> web.Response:
    """translate_cockney_get

    Translate from English to Cockney Speak.

    :param text: Text to translate
    :type text: str

    """
    return web.Response(status=200)


async def translate_jive_get(request: web.Request, text) -> web.Response:
    """translate_jive_get

    Translate from normal English to Jive Speak.

    :param text: Text to translate
    :type text: str

    """
    return web.Response(status=200)


async def translate_valspeak_get(request: web.Request, text) -> web.Response:
    """translate_valspeak_get

    Translate from English to Valley Speak.

    :param text: Text to translate
    :type text: str

    """
    return web.Response(status=200)
