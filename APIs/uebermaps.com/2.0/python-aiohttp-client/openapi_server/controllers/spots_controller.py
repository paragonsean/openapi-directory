from typing import List, Dict
from aiohttp import web

from openapi_server.models.spot import Spot
from openapi_server.models.spot_editable import SpotEditable
from openapi_server import util


async def maps_id_spots_get(request: web.Request, id, order=None) -> web.Response:
    """List spots for a given map

    List spots for a given map.

    :param id: Id of map
    :type id: int
    :param order: Order of spots
    :type order: str

    """
    return web.Response(status=200)


async def maps_id_spots_post(request: web.Request, id, spot) -> web.Response:
    """Create spot

    Create spot. Wrap parameters in [spot]. To add a spot picture pass a base64 encoded string to [spot][picture].

    :param id: Id of map
    :type id: int
    :param spot: spot attributes
    :type spot: dict | bytes

    """
    spot = SpotEditable.from_dict(spot)
    return web.Response(status=200)


async def maps_map_id_spots_id_get(request: web.Request, id, map_id) -> web.Response:
    """Get spot

    Get basic information about a spot

    :param id: Id of spot
    :type id: int
    :param map_id: Id of map
    :type map_id: int

    """
    return web.Response(status=200)


async def spots_get(request: web.Request, order=None) -> web.Response:
    """List your own spots

    List your own spots.

    :param order: Order of spots
    :type order: str

    """
    return web.Response(status=200)


async def spots_id_delete(request: web.Request, id) -> web.Response:
    """Delete spot

    Delete spot.

    :param id: spot id
    :type id: int

    """
    return web.Response(status=200)


async def spots_id_patch(request: web.Request, id, spot=None) -> web.Response:
    """Update spot

    Update spot. Wrap parameters in [spot]. To update the spot picture pass a base64 encoded string to [spot][picture].

    :param id: spot id
    :type id: int
    :param spot: spot attributes
    :type spot: dict | bytes

    """
    spot = SpotEditable.from_dict(spot)
    return web.Response(status=200)
