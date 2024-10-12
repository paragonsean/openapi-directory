from typing import List, Dict
from aiohttp import web

from openapi_server.models.locations_get200_response import LocationsGet200Response
from openapi_server.models.locations_id_get200_response import LocationsIdGet200Response
from openapi_server import util


async def locations_get(request: web.Request, name=None) -> web.Response:
    """Get all Locations

    Returns all Location objects.

    :param name: Can be used to filter Locations by their name. The response will only contain the Location matching the specified name.
    :type name: str

    """
    return web.Response(status=200)


async def locations_id_get(request: web.Request, id) -> web.Response:
    """Get a Location

    Returns a specific Location object.

    :param id: ID of Location
    :type id: int

    """
    return web.Response(status=200)
