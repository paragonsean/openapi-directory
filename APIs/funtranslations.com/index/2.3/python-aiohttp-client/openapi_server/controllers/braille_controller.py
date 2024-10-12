from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def translate_braille_dots_get(request: web.Request, text) -> web.Response:
    """translate_braille_dots_get

    Use this to see which dots are enabled for each Braille letters. This is highly educational (to see which dots are enabled) and can potentially drive a non braille display which works on individual dots.

    :param text: Text to translate
    :type text: str

    """
    return web.Response(status=200)


async def translate_braille_get(request: web.Request, text) -> web.Response:
    """translate_braille_get

    Translate from English to Braille. This is what you use if you have a braille display. This API translates the English text into characters that a braille display understands and you can feed the translated text directly to the display.

    :param text: Text to translate
    :type text: str

    """
    return web.Response(status=200)


async def translate_braille_html_get(request: web.Request, text) -> web.Response:
    """translate_braille_html_get

    Translate from English to Braille Image characters. This is probably what you want to use if you are displaying braille in a browser.

    :param text: Text to translate
    :type text: str

    """
    return web.Response(status=200)


async def translate_braille_image_get(request: web.Request, text) -> web.Response:
    """translate_braille_image_get

    Translate from English to Braille image characters. This is probably what you want to use if you are displaying braille in a browser.

    :param text: Text to translate
    :type text: str

    """
    return web.Response(status=200)


async def translate_braille_unicode_get(request: web.Request, text) -> web.Response:
    """translate_braille_unicode_get

    Translate from English to Braille Unicode characters.

    :param text: Text to translate
    :type text: str

    """
    return web.Response(status=200)
