from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def numbers_numeral_chinese_get(request: web.Request, number=None) -> web.Response:
    """numbers_numeral_chinese_get

    Convert base 10 representation of a given number to chinese numeral.

    :param number: Number to convert
    :type number: int

    """
    return web.Response(status=200)


async def numbers_numeral_egyptian_get(request: web.Request, number=None) -> web.Response:
    """numbers_numeral_egyptian_get

    Convert base 10 representation of a given number to egyptian numeral.

    :param number: Number to convert
    :type number: int

    """
    return web.Response(status=200)


async def numbers_numeral_roman_get(request: web.Request, number=None) -> web.Response:
    """numbers_numeral_roman_get

    Convert base 10 representation of a given number to roman numeral.

    :param number: Number to convert
    :type number: int

    """
    return web.Response(status=200)
