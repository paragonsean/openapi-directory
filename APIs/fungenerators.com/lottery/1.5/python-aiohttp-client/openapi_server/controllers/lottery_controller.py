from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def lottery_countries_get(request: web.Request, ) -> web.Response:
    """lottery_countries_get

    Get the complete list of countries supported in the number generation API.


    """
    return web.Response(status=200)


async def lottery_draw_get(request: web.Request, game, count=None) -> web.Response:
    """lottery_draw_get

    Generate random draw for a given lottery game.

    :param game: Lottery Game Name
    :type game: str
    :param count: Number of draws (max 5 per request)
    :type count: int

    """
    return web.Response(status=200)


async def lottery_supported_get(request: web.Request, country) -> web.Response:
    """lottery_supported_get

    Get the list of supported lottery games supported in the given country.

    :param country: Country Name
    :type country: str

    """
    return web.Response(status=200)
