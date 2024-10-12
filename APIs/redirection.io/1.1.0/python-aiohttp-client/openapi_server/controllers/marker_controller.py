from typing import List, Dict
from aiohttp import web

from openapi_server.models.marker import Marker
from openapi_server.models.marker_write import MarkerWrite
from openapi_server import util


async def delete_marker_item(request: web.Request, id) -> web.Response:
    """Removes the Marker resource.

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def get_marker_item(request: web.Request, id) -> web.Response:
    """Retrieves a Marker resource.

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def post_marker_collection(request: web.Request, marker=None) -> web.Response:
    """Creates a Marker resource.

    

    :param marker: The new Marker resource
    :type marker: dict | bytes

    """
    marker = MarkerWrite.from_dict(marker)
    return web.Response(status=200)


async def put_marker_item(request: web.Request, id, marker=None) -> web.Response:
    """Replaces the Marker resource.

    

    :param id: 
    :type id: str
    :param marker: The updated Marker resource
    :type marker: dict | bytes

    """
    marker = Marker.from_dict(marker)
    return web.Response(status=200)
