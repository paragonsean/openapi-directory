from typing import List, Dict
from aiohttp import web

from openapi_server.models.album import Album
from openapi_server.models.create_album_alt1_request import CreateAlbumAlt1Request
from openapi_server.models.edit_album_alt1_request import EditAlbumAlt1Request
from openapi_server.models.legacy_error import LegacyError
from openapi_server import util


async def create_album(request: web.Request, user_id, body) -> web.Response:
    """Create an album

    

    :param user_id: The ID of the user.
    :type user_id: 
    :param body: 
    :type body: dict | bytes

    """
    body = CreateAlbumAlt1Request.from_dict(body)
    return web.Response(status=200)


async def create_album_alt1(request: web.Request, body) -> web.Response:
    """Create an album

    

    :param body: 
    :type body: dict | bytes

    """
    body = CreateAlbumAlt1Request.from_dict(body)
    return web.Response(status=200)


async def delete_album(request: web.Request, album_id, user_id) -> web.Response:
    """Delete an album

    

    :param album_id: The ID of the album.
    :type album_id: 
    :param user_id: The ID of the user.
    :type user_id: 

    """
    return web.Response(status=200)


async def delete_album_alt1(request: web.Request, album_id) -> web.Response:
    """Delete an album

    

    :param album_id: The ID of the album.
    :type album_id: 

    """
    return web.Response(status=200)


async def edit_album(request: web.Request, album_id, user_id, body=None) -> web.Response:
    """Edit an album

    

    :param album_id: The ID of the album.
    :type album_id: 
    :param user_id: The ID of the user.
    :type user_id: 
    :param body: 
    :type body: dict | bytes

    """
    body = EditAlbumAlt1Request.from_dict(body)
    return web.Response(status=200)


async def edit_album_alt1(request: web.Request, album_id, body=None) -> web.Response:
    """Edit an album

    

    :param album_id: The ID of the album.
    :type album_id: 
    :param body: 
    :type body: dict | bytes

    """
    body = EditAlbumAlt1Request.from_dict(body)
    return web.Response(status=200)


async def get_album(request: web.Request, album_id, user_id) -> web.Response:
    """Get a specific album

    

    :param album_id: The ID of the album.
    :type album_id: 
    :param user_id: The ID of the user.
    :type user_id: 

    """
    return web.Response(status=200)


async def get_album_alt1(request: web.Request, album_id) -> web.Response:
    """Get a specific album

    

    :param album_id: The ID of the album.
    :type album_id: 

    """
    return web.Response(status=200)


async def get_albums(request: web.Request, user_id, direction=None, page=None, per_page=None, query=None, sort=None) -> web.Response:
    """Get all the albums that belong to a user

    

    :param user_id: The ID of the user.
    :type user_id: 
    :param direction: The sort direction of the results.
    :type direction: str
    :param page: The page number of the results to show.
    :type page: 
    :param per_page: The number of items to show on each page of results, up to a maximum of 100.
    :type per_page: 
    :param query: The search query to use to filter the results.
    :type query: str
    :param sort: The way to sort the results.
    :type sort: str

    """
    return web.Response(status=200)


async def get_albums_alt1(request: web.Request, direction=None, page=None, per_page=None, query=None, sort=None) -> web.Response:
    """Get all the albums that belong to a user

    

    :param direction: The sort direction of the results.
    :type direction: str
    :param page: The page number of the results to show.
    :type page: 
    :param per_page: The number of items to show on each page of results, up to a maximum of 100.
    :type per_page: 
    :param query: The search query to use to filter the results.
    :type query: str
    :param sort: The way to sort the results.
    :type sort: str

    """
    return web.Response(status=200)
