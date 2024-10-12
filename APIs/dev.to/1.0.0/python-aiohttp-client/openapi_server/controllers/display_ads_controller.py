from typing import List, Dict
from aiohttp import web

from openapi_server.models.display_ad import DisplayAd
from openapi_server import util


async def api_display_ads_get(request: web.Request, ) -> web.Response:
    """display ads

    This endpoint allows the client to retrieve a list of all display ads.


    """
    return web.Response(status=200)


async def api_display_ads_id_get(request: web.Request, id) -> web.Response:
    """display ad

    This endpoint allows the client to retrieve a single display ad, via its id.

    :param id: The ID of the display ad.
    :type id: int

    """
    return web.Response(status=200)


async def api_display_ads_id_put(request: web.Request, id, body=None) -> web.Response:
    """display ads

    This endpoint allows the client to update the attributes of a single display ad, via its id.

    :param id: The ID of the display ad.
    :type id: int
    :param body: 
    :type body: list | bytes

    """
    body = [DisplayAd.from_dict(d) for d in body]
    return web.Response(status=200)


async def api_display_ads_id_unpublish_put(request: web.Request, id) -> web.Response:
    """unpublish

    This endpoint allows the client to remove a display ad from rotation by un-publishing it.

    :param id: The ID of the display ad to unpublish.
    :type id: int

    """
    return web.Response(status=200)


async def api_display_ads_post(request: web.Request, body=None) -> web.Response:
    """display ads

    This endpoint allows the client to create a new display ad.

    :param body: 
    :type body: list | bytes

    """
    body = [DisplayAd.from_dict(d) for d in body]
    return web.Response(status=200)
