from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.playlist import Playlist
from openapi_server.models.playlists_get200_response import PlaylistsGet200Response
from openapi_server import util


async def playlists_get(request: web.Request, start=None, end=None, show_id=None, persona_id=None, count=None, page=None, fields=None, expand=None) -> web.Response:
    """Returns playlists optionally filtered by {start} and/or {end} datetimes

    Get Playlists optionally filtered by a datetime range. Only past Playlists will be returned (with allowed tolerance equals 1 hour in future).  Ordered chronologically from newest to oldest. 

    :param start: The datetime starting from items must be returned. Maximum 1 hour in future. 
    :type start: str
    :param end: The ending datetime. Maximum 1 hour in future. 
    :type end: str
    :param show_id: Filter by show
    :type show_id: int
    :param persona_id: Filter by persona
    :type persona_id: int
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


async def playlists_id_get(request: web.Request, id, fields=None, expand=None) -> web.Response:
    """Get a Playlist by id

    The response object represents the playlist specified by {id}.  Status 404 is returned if a playlist with {id} does not exist or if it does but starts in the future (with allowed tolerance equals 1 hour in future). 

    :param id: 
    :type id: int
    :param fields: Allows to select only needed fields
    :type fields: List[str]
    :param expand: Allows to select extra fields
    :type expand: List[str]

    """
    return web.Response(status=200)
