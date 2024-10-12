from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.spin import Spin
from openapi_server.models.spins_get200_response import SpinsGet200Response
from openapi_server.models.validation_error import ValidationError
from openapi_server import util


async def spins_get(request: web.Request, start=None, end=None, playlist_id=None, show_id=None, count=None, page=None, fields=None, expand=None) -> web.Response:
    """Returns spins optionally filtered by {start} and/or {end} datetimes

    Get Spins optionally filtered by a datetime range. Only past Spins will be returned. 

    :param start: The datetime starting from items must be returned. 
    :type start: str
    :param end: The ending datetime. 
    :type end: str
    :param playlist_id: Filter by playlist
    :type playlist_id: int
    :param show_id: Filter by show
    :type show_id: int
    :param count: Amount of items to return
    :type count: int
    :param page: Offset, used together with count
    :type page: int
    :param fields: Allows to select only needed fields
    :type fields: List[str]
    :param expand: Allows to select extra fields
    :type expand: List[str]

    """
    start = util.deserialize_datetime(start)
    end = util.deserialize_datetime(end)
    return web.Response(status=200)


async def spins_id_get(request: web.Request, id, fields=None, expand=None) -> web.Response:
    """Get a Spin by id

    

    :param id: 
    :type id: int
    :param fields: Allows to select only needed fields
    :type fields: List[str]
    :param expand: Allows to select extra fields
    :type expand: List[str]

    """
    return web.Response(status=200)


async def spins_post(request: web.Request, artist, song, composer=None, duration=None, genre=None, isrc=None, label=None, live=None, release=None, start=None) -> web.Response:
    """Log a Spin

    An endpoint for automation systems to log spins into the spin table.

    :param artist: 
    :type artist: str
    :param song: 
    :type song: str
    :param composer: 
    :type composer: str
    :param duration: 
    :type duration: int
    :param genre: 
    :type genre: str
    :param isrc: 
    :type isrc: str
    :param label: 
    :type label: str
    :param live: Only when automation params are configured with the \\\&quot;Pass through\\\&quot; mode. Enables \\\&quot;live assist\\\&quot; mode. Default mode is \\\&quot;full automation\\\&quot;. 
    :type live: bool
    :param release: 
    :type release: str
    :param start: 
    :type start: str

    """
    start = util.deserialize_datetime(start)
    return web.Response(status=200)
