from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def numbers_cardinal_get(request: web.Request, number=None, language=None) -> web.Response:
    """numbers_cardinal_get

    Get the cardinal of the given number

    :param number: Number value
    :type number: int
    :param language: Language to use
    :type language: str

    """
    return web.Response(status=200)


async def numbers_currency_get(request: web.Request, number=None, language=None) -> web.Response:
    """numbers_currency_get

    Spells out the number as a currency

    :param number: Number to spell
    :type number: int
    :param language: Language to use
    :type language: str

    """
    return web.Response(status=200)


async def numbers_ordinal_get(request: web.Request, number=None) -> web.Response:
    """numbers_ordinal_get

    Get the ordinal of the given number

    :param number: Number value
    :type number: int

    """
    return web.Response(status=200)
