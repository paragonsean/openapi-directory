from typing import List, Dict
from aiohttp import web

from openapi_server.models.map import Map
from openapi_server.models.respot import Respot
from openapi_server import util


async def maps_id_respots_get(request: web.Request, id) -> web.Response:
    """List respots of a map

    List respots of a map.

    :param id: Map Id
    :type id: int

    """
    return web.Response(status=200)


async def maps_map_id_spots_spot_id_respot_delete(request: web.Request, map_id, spot_id) -> web.Response:
    """Delete respot from map by spot id

    Delete respot from map by spot id.

    :param map_id: Map Id
    :type map_id: int
    :param spot_id: Spot Id
    :type spot_id: int

    """
    return web.Response(status=200)


async def respot_maps_get(request: web.Request, ) -> web.Response:
    """List maps that user can respot to

    List maps that user can respot to.


    """
    return web.Response(status=200)


async def respots_id_delete(request: web.Request, id) -> web.Response:
    """Delete respot

    Delete respot.

    :param id: Respot Id
    :type id: int

    """
    return web.Response(status=200)


async def respots_id_get(request: web.Request, id) -> web.Response:
    """Get respot

    Get basic information about a respot

    :param id: Id of respot
    :type id: int

    """
    return web.Response(status=200)


async def spots_id_respots_post(request: web.Request, id, map_id) -> web.Response:
    """Respot a spot onto a map

    Respot a spot onto a map.

    :param id: Spot Id
    :type id: int
    :param map_id: Map Id
    :type map_id: 

    """
    return web.Response(status=200)
