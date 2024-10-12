from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def categories_flat_get(request: web.Request, ) -> web.Response:
    """categories_flat_get

    


    """
    return web.Response(status=200)


async def categories_get(request: web.Request, ) -> web.Response:
    """List of supported product categories

    List of supported product categories


    """
    return web.Response(status=200)


async def categories_product_type_category_get(request: web.Request, product_type, category) -> web.Response:
    """Get subcategory details

    Get subcategory details

    :param product_type: 
    :type product_type: str
    :param category: 
    :type category: str

    """
    return web.Response(status=200)


async def categories_taxonomy_get(request: web.Request, ) -> web.Response:
    """Full taxonomy tree of categories including middle categories

    Full taxonomy tree of categories including middle categories


    """
    return web.Response(status=200)


async def categories_uuid_get(request: web.Request, uuid) -> web.Response:
    """Get category details

    Get category details

    :param uuid: 
    :type uuid: str

    """
    return web.Response(status=200)
