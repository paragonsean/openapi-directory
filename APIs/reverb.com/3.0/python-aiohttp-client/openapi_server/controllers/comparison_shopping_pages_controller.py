from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def comparison_shopping_pages_find_get(request: web.Request, id=None, slug=None) -> web.Response:
    """Show comparison shopping page

    Show comparison shopping page

    :param id: ID of the comparison shopping page
    :type id: str
    :param slug: Slug of the comparison shopping page
    :type slug: str

    """
    return web.Response(status=200)


async def comparison_shopping_pages_get(request: web.Request, ) -> web.Response:
    """Returns a set of comparison shopping pages based on the current params

    Returns a set of comparison shopping pages based on the current params


    """
    return web.Response(status=200)


async def comparison_shopping_pages_id_get(request: web.Request, id) -> web.Response:
    """comparison_shopping_pages_id_get

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def comparison_shopping_pages_id_listings_get(request: web.Request, id, condition, page=None, per_page=None, offset=None) -> web.Response:
    """Return new or used listings for a comparison shopping page

    Return new or used listings for a comparison shopping page

    :param id: 
    :type id: str
    :param condition: Condition of the listing
    :type condition: str
    :param page: 
    :type page: int
    :param per_page: 
    :type per_page: int
    :param offset: 
    :type offset: int

    """
    return web.Response(status=200)


async def comparison_shopping_pages_id_reviews_get(request: web.Request, id) -> web.Response:
    """View reviews of a comparison shopping page

    View reviews of a comparison shopping page

    :param id: 
    :type id: str

    """
    return web.Response(status=200)
