from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def numbers_base_binary_get(request: web.Request, number, _from=None) -> web.Response:
    """numbers_base_binary_get

    Convert a given number to binary

    :param number: Number to convert to binary
    :type number: int
    :param _from: Base of the supplied number (Optional base 10 assumed by default)
    :type _from: int

    """
    return web.Response(status=200)


async def numbers_base_get(request: web.Request, number, to, _from=None) -> web.Response:
    """numbers_base_get

    Convert a given number from one base to another base

    :param number: Number to convert to the target base
    :type number: int
    :param to: Target base to convert to
    :type to: int
    :param _from: Base of the supplied number (Optional base 10 assumed by default)
    :type _from: int

    """
    return web.Response(status=200)


async def numbers_base_hex_get(request: web.Request, number, _from=None) -> web.Response:
    """numbers_base_hex_get

    Convert a given number to hexadecimal

    :param number: Number to convert to hex
    :type number: int
    :param _from: Base of the supplied number (Optional base 10 assumed by default)
    :type _from: int

    """
    return web.Response(status=200)


async def numbers_base_octal_get(request: web.Request, number, _from=None) -> web.Response:
    """numbers_base_octal_get

    Convert a given number to octal

    :param number: Number to convert to octal
    :type number: int
    :param _from: Base of the supplied number (Optional base 10 assumed by default)
    :type _from: int

    """
    return web.Response(status=200)
