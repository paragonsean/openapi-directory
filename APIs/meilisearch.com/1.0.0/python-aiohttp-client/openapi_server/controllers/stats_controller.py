from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def global_stats(request: web.Request, ) -> web.Response:
    """Global stats

    Global stats


    """
    return web.Response(status=200)


async def health(request: web.Request, ) -> web.Response:
    """Health

    Health


    """
    return web.Response(status=200)


async def stats_of_an_index(request: web.Request, ) -> web.Response:
    """Stats of an index

    Stats of an index


    """
    return web.Response(status=200)


async def version(request: web.Request, ) -> web.Response:
    """Version

    Version


    """
    return web.Response(status=200)
