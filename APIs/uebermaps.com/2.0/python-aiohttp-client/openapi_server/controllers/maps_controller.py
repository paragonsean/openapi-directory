from typing import List, Dict
from aiohttp import web

from openapi_server.models.map import Map
from openapi_server.models.map_editable import MapEditable
from openapi_server.models.map_with_relation import MapWithRelation
from openapi_server import util


async def maps_get(request: web.Request, ) -> web.Response:
    """List your own maps

    List your own maps.


    """
    return web.Response(status=200)


async def maps_id_delete(request: web.Request, id) -> web.Response:
    """Delete map

    Delete map.

    :param id: map id
    :type id: int

    """
    return web.Response(status=200)


async def maps_id_get(request: web.Request, id) -> web.Response:
    """Get map

    Get basic information about a map

    :param id: Id of map
    :type id: int

    """
    return web.Response(status=200)


async def maps_id_patch(request: web.Request, id, map=None) -> web.Response:
    """Update map

    Update map. Wrap map parameters in [map]. To update the map header picture pass a base64 encoded string to [map][picture].

    :param id: map id
    :type id: int
    :param map: map settings attributes
    :type map: dict | bytes

    """
    map = MapEditable.from_dict(map)
    return web.Response(status=200)


async def maps_post(request: web.Request, map=None) -> web.Response:
    """Create map

    Create map. Wrap map parameters in [map]. To add a map header picture pass a base64 encoded string to [map][picture].

    :param map: map attributes
    :type map: dict | bytes

    """
    map = MapEditable.from_dict(map)
    return web.Response(status=200)


async def users_user_id_maps_get(request: web.Request, user_id) -> web.Response:
    """List maps for a given user

    List maps for a given user.

    :param user_id: Id of user
    :type user_id: int

    """
    return web.Response(status=200)
