from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def airports_options(request: web.Request, ) -> web.Response:
    """CORS support

    Enable CORS by returning correct headers 


    """
    return web.Response(status=200)


async def cities_findcitiesfromlatlong_options(request: web.Request, ) -> web.Response:
    """CORS support

    Enable CORS by returning correct headers 


    """
    return web.Response(status=200)


async def cities_findcitiesfromtext_options(request: web.Request, ) -> web.Response:
    """CORS support

    Enable CORS by returning correct headers 


    """
    return web.Response(status=200)


async def cities_significant_options(request: web.Request, ) -> web.Response:
    """CORS support

    Enable CORS by returning correct headers 


    """
    return web.Response(status=200)


async def continents_options(request: web.Request, ) -> web.Response:
    """CORS support

    Enable CORS by returning correct headers 


    """
    return web.Response(status=200)


async def countries_options(request: web.Request, ) -> web.Response:
    """CORS support

    Enable CORS by returning correct headers 


    """
    return web.Response(status=200)


async def distance_options(request: web.Request, ) -> web.Response:
    """CORS support

    Enable CORS by returning correct headers 


    """
    return web.Response(status=200)


async def elevation_options(request: web.Request, ) -> web.Response:
    """CORS support

    Enable CORS by returning correct headers 


    """
    return web.Response(status=200)


async def sun_positions_options(request: web.Request, ) -> web.Response:
    """CORS support

    Enable CORS by returning correct headers 


    """
    return web.Response(status=200)


async def timezone_options(request: web.Request, ) -> web.Response:
    """CORS support

    Enable CORS by returning correct headers 


    """
    return web.Response(status=200)
