from typing import List, Dict
from aiohttp import web

from openapi_server.models.near_earth_object import NearEarthObject
from openapi_server import util


async def browse_near_earth_objects(request: web.Request, page=None, size=None) -> web.Response:
    """Browse the Near Earth Objects service

    Retieve a paginated list of Near Earth Objects

    :param page: page
    :type page: int
    :param size: size
    :type size: int

    """
    return web.Response(status=200)


async def retrieve_near_earth_object_by_id(request: web.Request, asteroid_id) -> web.Response:
    """Find Near Earth Objects by id

    Retrieve a Near Earth Objects with a given id

    :param asteroid_id: ID of Near Earth Object - (ex: 3729835)
    :type asteroid_id: str

    """
    return web.Response(status=200)
