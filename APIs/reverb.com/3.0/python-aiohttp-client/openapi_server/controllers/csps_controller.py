from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def csps_categories_get(request: web.Request, ) -> web.Response:
    """csps_categories_get

    


    """
    return web.Response(status=200)


async def csps_find_get(request: web.Request, id=None, slug=None) -> web.Response:
    """Show comparison shopping page

    Show comparison shopping page

    :param id: ID of the comparison shopping page
    :type id: str
    :param slug: Slug of the comparison shopping page
    :type slug: str

    """
    return web.Response(status=200)


async def csps_get(request: web.Request, ) -> web.Response:
    """Returns a set of comparison shopping pages based on the current params

    Returns a set of comparison shopping pages based on the current params


    """
    return web.Response(status=200)


async def csps_id_get(request: web.Request, id) -> web.Response:
    """csps_id_get

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)
