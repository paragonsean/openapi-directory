from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def fact_fod_categories_get(request: web.Request, ) -> web.Response:
    """fact_fod_categories_get

    Get the list of supported fact of the day categories.


    """
    return web.Response(status=200)


async def fact_fod_get(request: web.Request, category=None) -> web.Response:
    """fact_fod_get

    Get fact of the day for the given category.

    :param category: Category to get the fact of the day from. Must be one from the list returned from /fact/fod/categories
    :type category: str

    """
    return web.Response(status=200)
