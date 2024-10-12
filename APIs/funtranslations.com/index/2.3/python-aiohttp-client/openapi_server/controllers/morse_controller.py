from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def translate_morse2english_get(request: web.Request, text) -> web.Response:
    """translate_morse2english_get

    Translate from Morse code to English.

    :param text: Text to translate
    :type text: str

    """
    return web.Response(status=200)


async def translate_morse_audio_get(request: web.Request, text, speed, tone) -> web.Response:
    """translate_morse_audio_get

    Translate from English to morse code and get the result as an audio file.

    :param text: Text to translate
    :type text: str
    :param speed: Audio Speed (Words/Minute)
    :type speed: int
    :param tone: Audio Tone Frequency(Hz)
    :type tone: int

    """
    return web.Response(status=200)


async def translate_morse_get(request: web.Request, text) -> web.Response:
    """translate_morse_get

    Translate from English to morse code.

    :param text: Text to translate
    :type text: str

    """
    return web.Response(status=200)
