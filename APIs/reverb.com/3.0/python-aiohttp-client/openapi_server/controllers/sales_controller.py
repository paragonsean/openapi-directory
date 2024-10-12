from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def sales_reverb_get(request: web.Request, ) -> web.Response:
    """View upcoming and live Reverb official sales.

    View upcoming and live Reverb official sales.


    """
    return web.Response(status=200)


async def sales_sale_id_listings_delete(request: web.Request, sale_id) -> web.Response:
    """Remove a listing from a sale

    Remove a listing from a sale

    :param sale_id: 
    :type sale_id: str

    """
    return web.Response(status=200)


async def sales_sale_id_listings_post(request: web.Request, sale_id) -> web.Response:
    """Add listings to a sale

    Add listings to a sale

    :param sale_id: 
    :type sale_id: str

    """
    return web.Response(status=200)


async def sales_seller_get(request: web.Request, ) -> web.Response:
    """View your created sales.

    View your created sales.


    """
    return web.Response(status=200)


async def sales_slug_get(request: web.Request, slug) -> web.Response:
    """sales_slug_get

    

    :param slug: 
    :type slug: str

    """
    return web.Response(status=200)
