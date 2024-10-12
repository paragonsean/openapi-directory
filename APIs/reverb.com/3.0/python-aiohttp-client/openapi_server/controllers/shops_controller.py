from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def shops_id_storefronts_get(request: web.Request, id) -> web.Response:
    """Get storefront details on a shop.

    Get storefront details on a shop.

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def shops_shop_id_shipping_profiles_get(request: web.Request, shop_id) -> web.Response:
    """List of shipping profiles for your shop

    List of shipping profiles for your shop

    :param shop_id: 
    :type shop_id: str

    """
    return web.Response(status=200)


async def shops_slug_feedback_buyer_get(request: web.Request, slug) -> web.Response:
    """Get seller&#39;s feedback as a buyer

    Get seller&#39;s feedback as a buyer

    :param slug: 
    :type slug: str

    """
    return web.Response(status=200)


async def shops_slug_feedback_get(request: web.Request, slug) -> web.Response:
    """Get seller&#39;s feedback

    Get seller&#39;s feedback

    :param slug: 
    :type slug: str

    """
    return web.Response(status=200)


async def shops_slug_feedback_seller_get(request: web.Request, slug) -> web.Response:
    """Get seller&#39;s feedback as a seller

    Get seller&#39;s feedback as a seller

    :param slug: 
    :type slug: str

    """
    return web.Response(status=200)


async def shops_slug_get(request: web.Request, slug, include_listing_count=None) -> web.Response:
    """Get details on a shop.

    Get details on a shop.

    :param slug: 
    :type slug: str
    :param include_listing_count: Include the live listing count in the response.
    :type include_listing_count: bool

    """
    return web.Response(status=200)
